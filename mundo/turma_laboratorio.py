"""Colegas de costas, sentados diante dos monitores em planos de profundidade."""
import pygame


class TurmaLaboratorio:
    def __init__(self, postos):
        self.postos = postos

    def draw(self, superficie, camera, instante, hipnose=0):
        for indice, posto in enumerate(self.postos):
            figura = pygame.Surface((64, 76), pygame.SRCALPHA)
            hipnotizado = hipnose > indice*0.12
            inclinacao = 3 if hipnotizado else 0
            # Pés e base da cadeira recuam sob o assento.
            pygame.draw.line(figura, (86, 102, 108), (32, 48), (32, 69), 3)
            pygame.draw.lines(figura, (67, 85, 94), False, [(10, 72), (32, 66), (54, 72)], 3)
            for x in (9, 51):
                pygame.draw.rect(figura, (15, 24, 30), (x, 70, 5, 4))
            for x in (20, 37):
                pygame.draw.rect(figura, (29, 38, 51), (x, 44, 8, 20))
                pygame.draw.rect(figura, (16, 26, 32), (x-2, 60, 11, 5))
            # Ombros, braços apoiados na mesa e mãos apontam para a tela.
            pygame.draw.polygon(figura, (28, 93, 67), [(18, 23), (45, 23), (49, 47), (15, 47)])
            pygame.draw.lines(figura, (37, 118, 78), False, [(20, 25), (13, 18), (18, 9)], 7)
            pygame.draw.lines(figura, (37, 118, 78), False, [(44, 25), (51, 18), (46, 9)], 7)
            for x in (16, 44):
                pygame.draw.rect(figura, (183, 139, 103), (x, 7, 5, 5))
            pygame.draw.rect(figura, (168, 121, 88), (27, 17+inclinacao, 10, 10))
            pygame.draw.rect(figura, (50, 37, 33), (21, 0+inclinacao, 22, 22), border_radius=5)
            pygame.draw.rect(figura, (28, 27, 29), (20, 0+inclinacao, 24, 14), border_radius=4)
            pygame.draw.line(figura, (77, 56, 42), (25, 3+inclinacao), (36, 3+inclinacao), 2)
            if indice % 2:
                pygame.draw.ellipse(figura, (29, 27, 30), (39, 9+inclinacao, 9, 22))
            # Reflexo de tela e postura, sem olhos frontais ou raios de hipnose.
            if hipnotizado:
                pygame.draw.line(figura, (91, 151, 143), (20, 23), (44, 23), 2)
            pygame.draw.rect(figura, (18, 35, 49), (14, 36, 36, 21), border_radius=4)
            pygame.draw.rect(figura, (44, 67, 82), (16, 37, 32, 16), border_radius=3)
            pygame.draw.line(figura, (74, 94, 102), (19, 39), (43, 39))
            escala = posto.width/70
            figura = pygame.transform.scale(figura, (round(64*escala), round(76*escala)))
            destino = figura.get_rect(midtop=(posto.centerx, posto.bottom+round(9*escala)))
            superficie.blit(figura, camera.apply(destino))
