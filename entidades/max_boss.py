import math
import random
import pygame
from entidades.inimigo import Inimigo
from entidades.projetil import Projetil
from sistema.configuracoes import TAMANHO_PERSONAGEM


class ProjetilFusoHorario(Projetil):
    """Projétil 'Lança de Fusos Horários' (Attack 1)."""

    def __init__(self, x, y, velocidade_x, velocidade_y):
        super().__init__(
            x=x,
            y=y,
            largura=20,
            altura=20,
            velocidade_x=velocidade_x,
            velocidade_y=velocidade_y,
            cor=(0, 180, 255),
            dano=12,
        )

    def desenhar(self, superficie, camera_x, camera_y):
        pos_x = self.rect.x - camera_x
        pos_y = self.rect.y - camera_y

        pygame.draw.circle(
            superficie, (120, 220, 255), (pos_x + 10, pos_y + 10), 10
        )
        pygame.draw.circle(
            superficie, (255, 255, 255), (pos_x + 10, pos_y + 10), 5
        )


class RochaTectonica(Projetil):
    """Projeção de rocha gerada pelo 'Impacto Tectônico' (Attack 2)."""

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            largura=32,
            altura=48,
            velocidade_x=0,
            velocidade_y=0,
            cor=(140, 70, 20),
            dano=22,
        )
        self.tempo_vida = 0.9
        self.timer = 0.0

    def atualizar(self, dt, mapa):
        self.timer += dt
        if self.timer >= self.tempo_vida:
            self.ativo = False
        super().atualizar(dt, mapa)

    def desenhar(self, superficie, camera_x, camera_y):
        pos_x = self.rect.x - camera_x
        pos_y = self.rect.y - camera_y

        pontos = [
            (pos_x, pos_y + self.rect.height),
            (pos_x + self.rect.width // 2, pos_y),
            (pos_x + self.rect.width, pos_y + self.rect.height),
        ]
        pygame.draw.polygon(superficie, (160, 85, 45), pontos)
        pygame.draw.polygon(superficie, (90, 45, 20), pontos, 2)


class MaxBoss(Inimigo):
    """Boss Max com mecânicas e animações extraídas da Sprite Sheet."""

    def __init__(self, x, y, caminho_spritesheet="recursos/imagens/max_spritesheet.png"):
        super().__init__(
            x=x,
            y=y,
            largura=TAMANHO_PERSONAGEM * 2,
            altura=TAMANHO_PERSONAGEM * 2,
            vida_maxima=300,
            velocidade=2.8,
            dano_contato=15,
            cor=(220, 50, 50),
        )

        self.nome = "Professor Max"
        self.estado = "idle"  # idle, walk, jump, lanca_fusos, impacto_tectonico, ciclone, knockback
        self.tempo_estado = 0.0
        self.timer_ataque = 0.0
        self.cooldown_ataque = 2.0
        self.direcao_olhar = -1
        self.ataque_executado = False

        # Mapeamento das 7 linhas da Sprite Sheet
        self.animacoes = {
            "idle": [],
            "walk": [],
            "jump": [],
            "lanca_fusos": [],
            "impacto_tectonico": [],
            "ciclone": [],
            "knockback": [],
        }

        self.frame_atual = 0
        self.timer_animacao = 0.0
        self.taxa_animacao = 0.12

        self._carregar_spritesheet(caminho_spritesheet)

    def _carregar_spritesheet(self, caminho):
        """Recorta as 7 linhas × 6 colunas da imagem do Boss."""
        try:
            sheet = pygame.image.load(caminho).convert_alpha()
            colunas = 6
            linhas = 7

            largura_fatia = sheet.get_width() // colunas
            altura_fatia = sheet.get_height() // linhas

            ordem_linhas = [
                "idle",
                "walk",
                "jump",
                "lanca_fusos",
                "impacto_tectonico",
                "ciclone",
                "knockback",
            ]

            for index_linha, nome_anim in enumerate(ordem_linhas):
                for col in range(colunas):
                    rect_corte = pygame.Rect(
                        col * largura_fatia,
                        index_linha * altura_fatia,
                        largura_fatia,
                        altura_fatia,
                    )
                    sub_surface = sheet.subsurface(rect_corte)
                    frame_escalado = pygame.transform.scale(
                        sub_surface, (self.rect.width, self.rect.height)
                    )
                    self.animacoes[nome_anim].append(frame_escalado)
        except Exception:
            pass

    def atualizar(self, dt, jogador, mapa):
        if not self.ativo or self.morrendo:
            return

        self.timer_ataque += dt
        self.tempo_estado += dt
        self.timer_animacao += dt

        # Avançar quadros de animação
        frames_atuais = self.animacoes.get(self.estado, [])
        if frames_atuais and self.timer_animacao >= self.taxa_animacao:
            self.timer_animacao = 0.0
            self.frame_atual = (self.frame_atual + 1) % len(frames_atuais)

        # Direção de olhar
        if self.estado in ["idle", "walk"]:
            self.direcao_olhar = -1 if jogador.rect.centerx < self.rect.centerx else 1

        # Lógica de Estados
        if self.estado == "idle":
            self.velocidade_x = 0
            if self.timer_ataque >= self.cooldown_ataque:
                self._escolher_proximo_ataque(jogador)

        elif self.estado == "walk":
            self.velocidade_x = self.direcao_olhar * self.velocidade
            if self.tempo_estado >= 1.5:
                self.estado = "idle"

        elif self.estado == "lanca_fusos":
            self.velocidade_x = 0
            if self.frame_atual >= 2 and not self.ataque_executado:
                self._executar_lanca_fusos(jogador, mapa)
                self.ataque_executado = True
            if self.tempo_estado >= 1.2:
                self.estado = "idle"

        elif self.estado == "impacto_tectonico":
            self.velocidade_x = 0
            if self.frame_atual == 2 and not self.ataque_executado:
                self._executar_impacto_tectonico(mapa)
                self.ataque_executado = True
            if self.tempo_estado >= 1.4:
                self.estado = "idle"

        elif self.estado == "ciclone":
            self.velocidade_x = self.direcao_olhar * (self.velocidade * 2.4)
            if self.tempo_estado >= 1.5:
                self.velocidade_x = 0
                self.estado = "idle"

        super().atualizar(dt, jogador, mapa)

    def _escolher_proximo_ataque(self, jogador):
        self.timer_ataque = 0.0
        self.tempo_estado = 0.0
        self.frame_atual = 0
        self.ataque_executado = False

        distancia = abs(jogador.rect.centerx - self.rect.centerx)
        if distancia > 200:
            opcoes = ["lanca_fusos", "ciclone", "walk"]
            pesos = [0.5, 0.3, 0.2]
        else:
            opcoes = ["impacto_tectonico", "lanca_fusos", "ciclone"]
            pesos = [0.4, 0.3, 0.3]

        self.estado = random.choices(opcoes, weights=pesos)[0]

    def _executar_lanca_fusos(self, jogador, mapa):
        dx = jogador.rect.centerx - self.rect.centerx
        dy = jogador.rect.centery - self.rect.centery
        ang = math.atan2(dy, dx)

        for offset in [-0.2, 0.0, 0.2]:
            vx = math.cos(ang + offset) * 6.5
            vy = math.sin(ang + offset) * 6.5
            mapa.adicionar_projetil(
                ProjetilFusoHorario(self.rect.centerx, self.rect.centery, vx, vy)
            )

    def _executar_impacto_tectonico(self, mapa):
        chao_y = self.rect.bottom - 48
        mapa.adicionar_projetil(RochaTectonica(self.rect.centerx - 70, chao_y))
        mapa.adicionar_projetil(RochaTectonica(self.rect.centerx + 40, chao_y))

    def desenhar(self, superficie, camera_x, camera_y):
        if not self.ativo:
            return

        pos_x = self.rect.x - camera_x
        pos_y = self.rect.y - camera_y

        frames = self.animacoes.get(self.estado, [])
        if frames:
            idx = self.frame_atual % len(frames)
            img = frames[idx]
            if self.direcao_olhar > 0:
                img = pygame.transform.flip(img, True, False)
            superficie.blit(img, (pos_x, pos_y))
        else:
            pygame.draw.rect(
                superficie,
                self.cor,
                (pos_x, pos_y, self.rect.width, self.rect.height),
            )