"""Guardião do catálogo: faixas anunciadas, fichas e pausa vulnerável."""
import pygame
from entidades.chefe import Chefe
from entidades.projetil import Projetil


class Indexador(Chefe):
    def __init__(self, *argumentos, **opcoes):
        super().__init__(*argumentos, **opcoes)
        self.faixas = []
        self.ciclo = 0
        # Arte vetorial simples própria, desenhada em resolução lógica de sprite.
        figura = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.rect(figura, (59, 77, 87), (4, 7, 32, 29), border_radius=3)
        for y in (10, 19, 28):
            pygame.draw.rect(figura, (180, 174, 142), (7, y, 26, 6))
            pygame.draw.line(figura, (65, 77, 81), (16, y+3), (23, y+3), 2)
        pygame.draw.rect(figura, (98, 187, 189), (12, 0, 16, 7))
        pygame.draw.rect(figura, (21, 36, 43), (15, 2, 3, 3))
        pygame.draw.rect(figura, (21, 36, 43), (23, 2, 3, 3))
        self.figura_direita = self.figura_esquerda = self.image = figura

    def take_damage(self, quantidade, recuo=(0, 0)):
        super().take_damage(quantidade, recuo)
        if self.derrotado:
            self.faixas = []
            self.estado_ataque = None

    def choose_attack(self, jogador):
        return 'carimbar' if self.ciclo % 2 == 0 else 'fichas'

    def update(self, jogador, solidos):
        if not self.ativo or not self.vivo:
            return
        self.brilho_dano = max(0, self.brilho_dano-1)
        self.projeteis.update(solidos)
        self.temporizador_ataque -= 1
        if self.estado_ataque is None:
            if self.temporizador_ataque > 0:
                return
            self.estado_ataque = self.choose_attack(jogador)
            self.relogio_ataque = 0
            # Mira fixa no início do aviso; sempre sobra espaço ao lado.
            centro = max(self.arena.left+32, min(self.arena.right-32, jogador.rect.centerx))
            self.faixas = [pygame.Rect(centro-28, self.arena.top, 56, self.arena.height)]
            if self.etapa >= 2:
                outro = self.arena.left+56 if centro > self.arena.centerx else self.arena.right-56
                self.faixas.append(pygame.Rect(outro-24, self.arena.top, 48, self.arena.height))
        self.relogio_ataque += 1
        if self.estado_ataque == 'fichas' and self.relogio_ataque in (48, 78):
            direcao = -1 if jogador.rect.centerx < self.rect.centerx else 1
            altura = self.rect.bottom-(18 if self.relogio_ataque == 48 else 65)
            self.projeteis.add(Projetil(self.rect.centerx, altura, (direcao, 0),
                                       dono='boss', velocidade=4, cor=(235, 211, 151)))
        if self.relogio_ataque >= 150:
            self.estado_ataque = None
            self.faixas = []
            self.ciclo += 1
            self.temporizador_ataque = 45

    def get_all_hit_rects(self):
        ataques = [(projetil.rect, projetil.dano) for projetil in self.projeteis]
        if self.estado_ataque == 'carimbar' and 48 <= self.relogio_ataque < 60:
            ataques += [(faixa, 1) for faixa in self.faixas]
        return ataques

    def draw(self, superficie, camera):
        if self.ativo and self.vivo and self.estado_ataque == 'carimbar' and self.relogio_ataque < 60:
            cor = (236, 88, 93) if self.relogio_ataque >= 48 else (231, 192, 119)
            for faixa in self.faixas:
                destino = camera.apply(faixa)
                pygame.draw.rect(superficie, cor, destino, 3)
                for y in range(destino.top, destino.bottom, 22):
                    pygame.draw.line(superficie, cor, (destino.left, y), (destino.right, y+14), 2)
        super().draw(superficie, camera)
