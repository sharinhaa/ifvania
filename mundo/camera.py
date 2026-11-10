"""Câmera 2D simples que segue o jogador e trava nos limites do nível."""
import pygame
from sistema import configuracoes
class Camera:
    def __init__(self, largura_fase, altura_fase):
        self.deslocamento = pygame.Vector2(0, 0)
        self.largura_fase = largura_fase
        self.altura_fase = altura_fase
        self.inicializada = False

    def update(self, retangulo_alvo):
        x = retangulo_alvo.centerx - configuracoes.LARGURA_TELA // 2
        # Uma zona vertical estável evita arrastar o cenário a cada salto.
        # Ao subir além dela a câmera continua acompanhando plataformas altas.
        y = self.deslocamento.y
        if not self.inicializada:
            y = retangulo_alvo.centery - configuracoes.ALTURA_TELA // 2
        elif retangulo_alvo.centery-y < 180:
            y = retangulo_alvo.centery-180
        elif retangulo_alvo.centery-y > 370:
            y = retangulo_alvo.centery-370
        x = max(0, min(x, max(0, self.largura_fase - configuracoes.LARGURA_TELA)))
        y = max(0, min(y, max(0, self.altura_fase - configuracoes.ALTURA_TELA)))
        self.deslocamento.x, self.deslocamento.y = x, y
        self.inicializada = True

    def apply(self, retangulo):
        return pygame.Rect(retangulo.x - self.deslocamento.x, retangulo.y - self.deslocamento.y, retangulo.width, retangulo.height)
