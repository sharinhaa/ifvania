"""Exporta bustos HD independentes dos sprites de combate."""
import pygame
from ferramentas.preparar_figuras_personagens import ORIGENS, DESTINO

NOMES = ('menino', 'menina', 'max', 'romerito', 'entidade', 'indexador')


def principal():
    pygame.init()
    try:
        destino = DESTINO/'dialogos'
        destino.mkdir(parents=True, exist_ok=True)
        for nome in NOMES:
            imagem = pygame.image.load(str(ORIGENS/'retratos_dialogo'/f'{nome}.png'))
            if imagem.get_width() < 1024 or imagem.get_height() < 1536:
                raise ValueError(f'Fonte de {nome} deve ter pelo menos 1024 × 1536')
            if nome == 'entidade':
                imagem = pygame.transform.flip(imagem, True, False)
            pygame.image.save(pygame.transform.smoothscale(imagem, (768, 1152)), str(destino/f'{nome}.png'))
        # Sistema é uma interface, representada por símbolo vetorial em alta resolução.
        sistema = pygame.Surface((768, 1152), pygame.SRCALPHA)
        pygame.draw.rect(sistema, (17, 33, 54), (80, 285, 608, 420), border_radius=38)
        pygame.draw.rect(sistema, (118, 205, 226), (80, 285, 608, 420), 12, border_radius=38)
        pygame.draw.lines(sistema, (167, 237, 227), False, [(172, 410), (245, 480), (172, 550)], 22)
        pygame.draw.line(sistema, (236, 216, 166), (315, 560), (544, 560), 22)
        pygame.draw.rect(sistema, (85, 130, 154), (352, 705, 64, 125))
        pygame.draw.rect(sistema, (133, 187, 203), (244, 830, 280, 22), border_radius=8)
        pygame.image.save(sistema, str(destino/'sistema.png'))
    finally:
        pygame.quit()


if __name__ == '__main__':
    principal()
