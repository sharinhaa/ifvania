"""Transporte visual ao monitor, independente de física e dano."""
import math
import pygame


class SuccaoComputador:
    DURACAO = 150

    def __init__(self, fase, jogador):
        self.fase = fase
        self.atores = [jogador, *fase.professores]
        # Monitor mais próximo de Romerito; coordenadas do mesmo cenário.
        self.monitor = min(fase.arte.telas_monitores, key=lambda tela: abs(tela.centerx-700)).copy()
        self.inicios = [ator.get_draw_image().get_rect(midbottom=fase.camera.apply(ator.rect).midbottom)
                        for ator in self.atores]
        self.recuos = [retangulo.copy() for retangulo in self.inicios]
        self.recuos[0].x -= 12
        self.recuos[1].centerx = jogador.rect.x+jogador.largura-8+20
        self.quadros = [ator.get_draw_image().copy() for ator in self.atores]

    def amostra(self, indice, progresso):
        fracao = max(0, min(1, (progresso-0.16-indice*0.045)/0.70))
        curva = fracao*fracao*(3-2*fracao)
        inicio = pygame.Vector2(self.inicios[indice].center).lerp(
            pygame.Vector2(self.recuos[indice].center), min(1, progresso/0.12))
        alvo = pygame.Vector2(self.fase.camera.apply(self.monitor).center)
        centro = inicio.lerp(alvo, curva)
        centro.y -= math.sin(fracao*math.pi)*48
        escala = max(0.02, (1-curva)**1.3)
        return centro, escala, fracao

    def draw(self, superficie, progresso):
        tela = self.fase.camera.apply(self.monitor)
        centro = pygame.Vector2(tela.center)
        sombra = pygame.Surface(superficie.get_size(), pygame.SRCALPHA)
        sombra.fill((3, 10, 23, round(130*min(1, progresso*2))))
        superficie.blit(sombra, (0, 0))
        brilho = pygame.Surface(superficie.get_size(), pygame.SRCALPHA)
        pygame.draw.ellipse(brilho, (97, 219, 216, 95), tela.inflate(36, 28))
        superficie.blit(brilho, (0, 0))
        # Partículas viajam da sala até o centro da tela; sem relógio externo.
        for indice in range(36):
            angulo = indice*2.399+progresso*2
            distancia = (1-((progresso*2+indice/36) % 1))*210
            origem = centro+pygame.Vector2(math.cos(angulo)*distancia, math.sin(angulo)*distancia*0.55)
            fim = origem.lerp(centro, 0.12)
            pygame.draw.line(superficie, (80, 171, 181), origem, fim, 1)
        for indice, quadro in enumerate(self.quadros):
            posicao, escala, fracao = self.amostra(indice, progresso)
            if fracao >= 1:
                continue
            tamanho = (max(1, round(quadro.get_width()*escala)), max(1, round(quadro.get_height()*escala)))
            imagem = pygame.transform.scale(quadro, tamanho)
            imagem = pygame.transform.rotate(imagem, (1 if indice == 0 else -1)*fracao*300)
            superficie.blit(imagem, imagem.get_rect(center=(round(posicao.x), round(posicao.y))))
            for faixa in range(3):
                cauda = posicao.lerp(centro, 0.25+faixa*0.15)
                pygame.draw.line(superficie, (92, 194, 201), posicao, cauda, 1)
        pygame.draw.rect(superficie, (164, 251, 228), tela, 2)
        if progresso > 0.90:
            # A imagem inteira fecha sobre o monitor antes de revelar a fase virtual.
            margem = round((progresso-0.90)*10*superficie.get_height()/2)
            pygame.draw.rect(superficie, (2, 9, 16), (0, 0, superficie.get_width(), margem))
            pygame.draw.rect(superficie, (2, 9, 16), (0, superficie.get_height()-margem, superficie.get_width(), margem))
