"""Exporta fundos do IFRN preservando as fontes e as artes anteriores."""
from pathlib import Path
import argparse
import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')
os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')
import pygame

RAIZ = Path(__file__).resolve().parents[1]


def exportar(destino):
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=True)
    pygame.init()
    try:
        for nome in ('biblioteca_ifrn', 'patio_ifrn', 'memoria_tarefa'):
            origem = RAIZ/'recursos'/'fontes_arte'/(nome+'.png')
            imagem = pygame.image.load(str(origem))
            pygame.image.save(pygame.transform.scale(imagem, (960, 540)), str(destino/(nome+'.png')))
    finally:
        pygame.quit()


if __name__ == '__main__':
    analisador = argparse.ArgumentParser(description=__doc__)
    analisador.add_argument('--destino', type=Path, default=RAIZ/'recursos'/'imagens'/'cenarios')
    exportar(analisador.parse_args().destino)
