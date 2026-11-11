"""Moldura azul e composição dos bustos de conversa, em resolução nativa."""
import pygame


class QuadroDialogo:
    def __init__(self):
        self.paineis = {}
        self.bustos = {}

    def desenhar_busto(self, superficie, imagem, lado, base, ativo):
        chave = (id(imagem), ativo)
        if chave not in self.bustos:
            escala = min(238/imagem.get_width(), 300/imagem.get_height())
            busto = pygame.transform.smoothscale(imagem, (round(imagem.get_width()*escala),
                                                        round(imagem.get_height()*escala)))
            if not ativo:
                busto.fill((112, 125, 143, 255), special_flags=pygame.BLEND_RGBA_MULT)
            self.bustos[chave] = busto
        busto = self.bustos[chave]
        destino = busto.get_rect(bottomleft=(38, base)) if lado == 'esquerda' else busto.get_rect(bottomright=(superficie.get_width()-38, base))
        superficie.blit(busto, destino)
        return destino

    def desenhar_painel(self, superficie, retangulo, destaque):
        chave = (retangulo.size, destaque)
        if chave not in self.paineis:
            painel = pygame.Surface(retangulo.size, pygame.SRCALPHA)
            largura, altura = retangulo.size
            for y in range(altura):
                fracao = y/max(1, altura-1)
                cor = (round(24-12*fracao), round(48-22*fracao), round(77-30*fracao), 242)
                pygame.draw.line(painel, cor, (3, y), (largura-4, y))
            pygame.draw.rect(painel, (6, 13, 25, 255), painel.get_rect(), 4, border_radius=10)
            pygame.draw.rect(painel, (179, 211, 224, 255), painel.get_rect().inflate(-4, -4), 2, border_radius=9)
            pygame.draw.rect(painel, (62, 109, 144, 255), painel.get_rect().inflate(-12, -12), 1, border_radius=6)
            pygame.draw.line(painel, (*destaque, 220), (22, 10), (largura-23, 10), 2)
            for x in (13, largura-14):
                for y in (13, altura-14):
                    pygame.draw.polygon(painel, (*destaque, 255), [(x-3,y),(x,y-3),(x+3,y),(x,y+3)])
            self.paineis[chave] = painel
        sombra = pygame.Surface(retangulo.size, pygame.SRCALPHA)
        sombra.fill((0, 0, 0, 100))
        superficie.blit(sombra, retangulo.move(0, 5))
        superficie.blit(self.paineis[chave], retangulo)
