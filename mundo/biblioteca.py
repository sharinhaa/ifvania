"""Cenário em Pygame e objetivos locais da biblioteca virtual.

Materiais inspirados nas capturas 17-24-38 e 17-24-56 de referencia/ifrn.
O desenho não define colisões; apoios sólidos continuam no mapa de blocos.
"""
import pygame
import recursos
from habilidades import Habilidade
from mundo.dados_biblioteca import DIALOGO_MODULO
from mundo.escola_sombria import EscolaSombria
from mundo.camera import Camera


class Biblioteca(EscolaSombria):
    def __init__(self, largura, altura, y_piso):
        super().__init__(largura, altura, y_piso)
        self.fundo_ifrn = recursos.load_image('cenarios/biblioteca_ifrn.png')
        self.largura = largura
        self.paineis = [pygame.Rect(15*32, y_piso-40, 30, 40),
                        pygame.Rect(27*32, 9*32-40, 30, 40),
                        pygame.Rect(45*32, 9*32-40, 30, 40)]
        self.consultados = set()
        self.modulo_obtido = False
        self.modulo = pygame.Rect(18*32, y_piso-34, 30, 34)
        self.portao = pygame.Rect(59*32, 32, 32, y_piso-32)
        self.ajuda = ''
        self.camada = pygame.Surface((960, altura))
        self.camera_cenario = Camera(largura, altura)

    def draw_background(self, superficie, camera):
        self.camera_cenario.deslocamento.update(camera.deslocamento.x, 0)
        self._desenhar_ambiente(self.camada, self.camera_cenario)
        superficie.blit(self.camada, (0, -round(camera.deslocamento.y)))
        rotulo = f'ARQUIVO: {len(self.consultados)}/3  |  E consultar'
        superficie.blit(self.fonte.render(rotulo, True, (230, 221, 193)), (240, 66))
        if self.ajuda:
            superficie.blit(self.fonte.render(self.ajuda, True, (163, 235, 225)), (240, 86))

    def _desenhar_ambiente(self, superficie, camera):
        superficie.fill((35, 45, 53))
        piso = self.y_piso
        for coluna in range(0, self.largura, self.fundo_ifrn.get_width()):
            x = round(coluna-camera.deslocamento.x)
            superficie.blit(self.fundo_ifrn, (x, self.y_piso-352))
        for indice, painel in enumerate(self.paineis):
            destino = camera.apply(painel)
            pygame.draw.rect(superficie, (19, 30, 37), destino)
            cor = (119, 213, 176) if indice in self.consultados else (232, 194, 123)
            pygame.draw.rect(superficie, cor, destino.inflate(-8, -12), 2)
            superficie.blit(self.fonte.render(str(indice+1), True, cor), (destino.x+11, destino.y+12))
        if not self.modulo_obtido:
            destino = camera.apply(self.modulo)
            pygame.draw.rect(superficie, (85, 206, 211), destino, 2)
            pygame.draw.line(superficie, (226, 236, 220), destino.midbottom, destino.midtop, 3)
        if len(self.consultados) < 3:
            destino = camera.apply(self.portao)
            pygame.draw.rect(superficie, (102, 83, 70), destino)
            for y in range(40, piso, 24):
                pygame.draw.line(superficie, (228, 191, 122), (destino.x, y), (destino.right, y+15), 3)

    def interagir(self, jogador, eventos, solidos):
        self.ajuda = ''
        alvos = [(self.modulo, 'Módulo: E para examinar')] if not self.modulo_obtido else []
        alvos += [(painel, 'E para consultar o arquivo') for painel in self.paineis]
        perto = [alvo for alvo, _ in alvos
                 if jogador.rect.colliderect(alvo.inflate(55, 30))
                 and jogador.rect.bottom <= alvo.bottom+16]
        for alvo, dica in alvos:
            if alvo in perto:
                self.ajuda = dica
        if not any(evento.type == pygame.KEYDOWN and evento.key == pygame.K_e for evento in eventos):
            return None
        if not self.modulo_obtido and self.modulo in perto:
            self.modulo_obtido = True
            jogador.grant_ability(Habilidade.SALTO_DUPLO, aumentar_vida=False)
            return DIALOGO_MODULO
        for indice, painel in enumerate(self.paineis):
            if painel in perto and indice not in self.consultados:
                self.consultados.add(indice)
                textos = ('Registro: a mesma assinatura aparece em várias máquinas. Vencer Romerito não desligou a IA.',
                          'Mapa recuperado: existe uma passagem pelo pátio. Os colegas precisam dessa rota.',
                          'Inventário: o servidor usa nobreak. Cortar só a tomada não basta.')
                if len(self.consultados) == 3:
                    solidos.remove(self.portao)
                return [('Aluno(a)', textos[indice])]
        return None
