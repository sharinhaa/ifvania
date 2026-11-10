"""Cenário em Pygame e objetivos locais da biblioteca virtual.

Materiais inspirados nas capturas 17-24-38 e 17-24-56 de referencia/ifrn.
O desenho não define colisões; apoios sólidos continuam no mapa de blocos.
"""
import pygame
from sistema import recursos
from interface import tema
from sistema.habilidades import Habilidade
from mundo.dados_biblioteca import DIALOGO_MODULO
from mundo.escola_sombria import EscolaSombria
from mundo.camera import Camera


class Biblioteca(EscolaSombria):
    def __init__(self, largura, altura, y_piso):
        super().__init__(largura, altura, y_piso)
        self.fundo_ifrn = recursos.load_image('cenarios/biblioteca_ifrn.png')
        self.largura = largura
        self.paineis = [pygame.Rect(15*32, y_piso-40, 30, 40),
                        pygame.Rect(27*32, 9*32-40, 30, 40),
                        pygame.Rect(45*32, 9*32-40, 30, 40)]
        self.consultados = set()
        self.modulo_obtido = False
        self.modulo = pygame.Rect(18*32, y_piso-34, 30, 34)
        self.portao = pygame.Rect(59*32, 32, 32, y_piso-32)
        self.ajuda = ''
        self.camada = pygame.Surface((960, altura))
        self.camera_cenario = Camera(largura, altura)
        self.sombra_fundo = pygame.Surface((960, altura), pygame.SRCALPHA)
        self.sombra_fundo.fill((8, 17, 25, 45))

    def draw_background(self, superficie, camera):
        self.camera_cenario.deslocamento.update(camera.deslocamento.x, 0)
        self._desenhar_ambiente(self.camada, self.camera_cenario)
        superficie.blit(self.camada, (0, -round(camera.deslocamento.y)))

    def desenhar_objetivos(self, superficie):
        # Coluna central livre dos painéis de vida, habilidades e chefe.
        tema.panel(superficie, (240, 61, 330, 27), tema.AMBAR)
        rotulo = self.ajuda or f'ARQUIVOS {len(self.consultados)}/3  |  E consultar  |  siga os terminais'
        superficie.blit(self.fonte.render(rotulo, True, (230, 221, 193)), (250, 69))

    def _desenhar_ambiente(self, superficie, camera):
        superficie.fill((35, 45, 53))
        for coluna in range(0, self.largura, self.fundo_ifrn.get_width()):
            x = round(coluna-camera.deslocamento.x)
            superficie.blit(self.fundo_ifrn, (x, self.y_piso-352))
        superficie.blit(self.sombra_fundo, (0, 0))

    def desenhar_interativos(self, superficie, camera):
        """Sinais no mesmo plano dos sólidos, após desenhar as plataformas."""
        for indice, painel in enumerate(self.paineis):
            destino = camera.apply(painel)
            pygame.draw.rect(superficie, (19, 30, 37), destino)
            cor = (119, 213, 176) if indice in self.consultados else (232, 194, 123)
            pygame.draw.rect(superficie, cor, destino.inflate(-8, -12), 2)
            superficie.blit(self.fonte.render(str(indice+1), True, cor), (destino.x+11, destino.y+12))
            rotulo = 'LIDO' if indice in self.consultados else f'ARQUIVO {indice+1}'
            self._rotular(superficie, destino, rotulo, cor)
        if not self.modulo_obtido:
            destino = camera.apply(self.modulo)
            pygame.draw.rect(superficie, (85, 206, 211), destino, 2)
            pygame.draw.line(superficie, (226, 236, 220), destino.midbottom, destino.midtop, 3)
            self._rotular(superficie, destino, 'SALTO DUPLO', tema.CIANO)
        if len(self.consultados) < 3:
            destino = camera.apply(self.portao)
            pygame.draw.rect(superficie, (102, 83, 70), destino)
            for y in range(destino.top+8, destino.bottom-15, 24):
                pygame.draw.line(superficie, (228, 191, 122), (destino.x, y), (destino.right-1, y+15), 3)
            self._rotular(superficie, destino, f'ARQUIVOS {len(self.consultados)}/3', tema.AMBAR)

    def _rotular(self, superficie, destino, texto, cor):
        imagem = self.fonte.render(texto, True, cor)
        rotulo = imagem.get_rect(midbottom=(destino.centerx, destino.top-6))
        pygame.draw.rect(superficie, (14, 24, 30), rotulo.inflate(10, 6))
        superficie.blit(imagem, rotulo)

    def interagir(self, jogador, eventos, solidos):
        self.ajuda = ''
        alvos = [(self.modulo, 'Módulo: E para examinar')] if not self.modulo_obtido else []
        alvos += [(painel, 'E para consultar o arquivo') for painel in self.paineis]
        perto = [alvo for alvo, _ in alvos
                 if jogador.rect.colliderect(alvo.inflate(55, 30))
                 and jogador.rect.bottom <= alvo.bottom+16]
        for alvo, dica in alvos:
            if alvo in perto:
                self.ajuda = dica
        if not any(evento.type == pygame.KEYDOWN and evento.key == pygame.K_e for evento in eventos):
            return None
        if not self.modulo_obtido and self.modulo in perto:
            self.modulo_obtido = True
            jogador.grant_ability(Habilidade.SALTO_DUPLO, aumentar_vida=False)
            return DIALOGO_MODULO
        for indice, painel in enumerate(self.paineis):
            if painel in perto and indice not in self.consultados:
                self.consultados.add(indice)
                textos = ('Registro: a mesma assinatura aparece em várias máquinas. Vencer Romerito não desligou a IA.',
                          'Mapa recuperado: existe uma passagem pelo pátio. Os colegas precisam dessa rota.',
                          'Inventário: o servidor usa nobreak. Cortar só a tomada não basta.')
                if len(self.consultados) == 3:
                    solidos.remove(self.portao)
                return [('Aluno(a)', textos[indice])]
        return None
