"""Alunos sentados: composição das artes existentes, sem corpos de combate."""
import math
import pygame
import recursos


class TurmaLaboratorio:
    def __init__(self, postos):
        self.postos = postos
        self.figuras = recursos.load_character_frames([
            'jogador/repouso_0.png', 'jogador/menina/repouso_0.png'])

    def draw(self, superficie, camera, instante, hipnose=0):
        for indice, posto in enumerate(self.postos):
            x, y = posto.x-24, posto.y+4
            destino = camera.apply(pygame.Rect(x, y, 64, 100))
            if not destino.colliderect(superficie.get_rect()):
                continue
            # Encosto, pernas dobradas e torso na mesma escala do protagonista.
            pygame.draw.rect(superficie, (28, 48, 67), (destino.x+12, destino.y+37, 27, 46), border_radius=3)
            pygame.draw.line(superficie, (83, 97, 104), (destino.x+16, destino.y+78), (destino.x+10, destino.y+101), 4)
            pygame.draw.line(superficie, (83, 97, 104), (destino.x+34, destino.y+78), (destino.x+44, destino.y+101), 4)
            figura = self.figuras[indice % 2]
            torso = pygame.transform.scale(figura.subsurface((0, 0, 40, 27)), (80, 54))
            oscilacao = 0 if hipnose else round(math.sin(instante*0.05+indice)*1.2)
            superficie.blit(torso, (destino.x-6, destino.y+oscilacao))
            pygame.draw.lines(superficie, (26, 36, 45), False,
                              [(destino.x+28, destino.y+52), (destino.x+48, destino.y+63),
                               (destino.x+46, destino.y+91), (destino.x+58, destino.y+91)], 8)
            mao = (destino.x+49, destino.y+42+oscilacao)
            pygame.draw.line(superficie, (163, 124, 96), (destino.x+32, destino.y+37), mao, 4)
            if hipnose > indice*0.12:
                # Olhos fixos e vínculo na direção da tela, não dano ou projétil.
                olhos = (destino.x+35, destino.y+13)
                pygame.draw.line(superficie, (138, 240, 217), (olhos[0]-3, olhos[1]), (olhos[0]+5, olhos[1]), 2)
                pygame.draw.line(superficie, (75, 148, 157), olhos, camera.apply(posto).center, 1)
                if hipnose < 1:
                    raio = 10+round(8*hipnose)
                    pygame.draw.circle(superficie, (100, 196, 189), (destino.x+32, destino.y+13), raio, 1)
