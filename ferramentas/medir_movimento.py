"""Mede controles pela física real em piso plano, sem inimigos."""
import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')
os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')
import json
from collections import defaultdict
import pygame
from entidades.jogador import Jogador
pygame.init()
pygame.display.set_mode((960,540))
resultados = {}
for personagem in ('boy', 'menina'):
    jogador = Jogador(200, 408, personagem=personagem)
    solidos = [pygame.Rect(0,448,3000,100)]
    jogador.no_chao = True
    velocidades = []
    for _ in range(8):
        jogador.handle_input(defaultdict(bool,{pygame.K_d:True}), [])
        jogador.update(solidos, [])
        velocidades.append(round(jogador.velocidade.x,2))
    inicio = jogador.rect.x
    frenagem = 0
    while jogador.velocidade.x:
        jogador.handle_input(defaultdict(bool), [])
        jogador.update(solidos, [])
        frenagem += 1
    distancia_frenagem = jogador.rect.x-inicio
    inicio_x = jogador.rect.x
    menor_y = jogador.rect.y
    for quadro in range(90):
        eventos = [pygame.event.Event(pygame.KEYDOWN,key=pygame.K_SPACE)] if quadro == 0 else []
        jogador.handle_input(defaultdict(bool,{pygame.K_d:True}), eventos)
        jogador.update(solidos, [])
        menor_y = min(menor_y,jogador.rect.y)
        if quadro > 0 and jogador.no_chao: break
    resultados[personagem] = dict(velocidades_iniciais=velocidades, frenagem_quadros=frenagem,
        frenagem_pixels=distancia_frenagem, altura_salto_pixels=408-menor_y,
        duracao_salto_quadros=quadro+1, alcance_salto_pixels=jogador.rect.x-inicio_x)
print(json.dumps(resultados,ensure_ascii=False,indent=2))
pygame.quit()
