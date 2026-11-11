"""Exporta oito passos em postura de carga para cada protagonista."""
import pygame
from sistema import configuracoes
from ferramentas.preparar_figuras_personagens import extract_figures, export_frames


def principal():
    pygame.init()
    pygame.display.set_mode((1, 1))
    try:
        figuras = extract_figures('caminhada_carregando.png', 2, 8)
        for fileira, pasta in enumerate(('jogador/caminhada_carregando',
                                        'jogador/menina/caminhada_carregando')):
            export_frames(figuras[fileira*8:fileira*8+8], pasta,
                          [f'caminhada_{i}.png' for i in range(8)], configuracoes.TAMANHO_PERSONAGEM)
    finally:
        pygame.quit()


if __name__ == '__main__':
    principal()
