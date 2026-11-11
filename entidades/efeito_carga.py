"""Partículas pixeladas de convergência e pulso local, sem alterar o combate."""
import math
import pygame
from sistema import configuracoes


def desenhar_energia(superficie, camera, jogador):
    centro = camera.apply(jogador.rect).midbottom
    centro = pygame.Vector2(centro[0], centro[1]-43)
    instante = jogador.instante_carga
    fracao = min(1, jogador.carga/configuracoes.TEMPO_CARGA)
    pronto = fracao >= 1
    cor = (115, 239, 223) if pronto else (255, 191, 79)
    camada = pygame.Surface((128, 128), pygame.SRCALPHA)
    # Partículas seguem chegando mesmo depois de o contador de dano saturar.
    for indice in range(10 if pronto else 6):
        fase = ((instante*0.035+indice*0.137) % 1)
        angulo = indice*2.399+instante*0.025
        raio = 55*(1-fase)+5
        x = 64+round(math.cos(angulo)*raio)
        y = 64+round(math.sin(angulo)*raio*0.83)
        tamanho = 4 if fase < 0.65 else 2
        pygame.draw.rect(camada, (*cor, round(100+155*fase)), (x-1, y-1, tamanho+2, tamanho+2))
        pygame.draw.rect(camada, (255, 255, 226, 235), (x, y, tamanho, tamanho))
    if pronto:
        pulso = (math.sin(instante*0.18)+1)/2
        # Aura estreita e translúcida: rosto, cenário e ameaças continuam visíveis.
        pygame.draw.ellipse(camada, (*cor, round(35+25*pulso)), (42, 27, 44, 77), 3)
        for lado in (-1, 1):
            x = 64+lado*(24+round(3*pulso))
            pygame.draw.lines(camada, (*cor, 155), False,
                              [(x, 82), (x+lado*4, 65), (x-lado*2, 52), (x+lado*2, 36)], 2)
    superficie.blit(camada, (round(centro.x)-64, round(centro.y)-64))
