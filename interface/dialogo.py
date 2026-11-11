"""Sistema simples de caixas de diálogo estilo RPG/metroidvania."""
import pygame
from sistema import configuracoes
from interface import tema
from interface.retratos import RetratosDialogo
from interface.quadro_dialogo import QuadroDialogo


class CaixaDialogo:
    def __init__(self):
        self.linhas = []          # lista de tuplas (falante, texto)
        self.indice = 0
        self.ativo = False
        self.ao_concluir = None
        self.fonte = pygame.font.Font(None, 22)
        self.fonte_nome = pygame.font.Font(None, 24)
        self._caracteres_exibidos = 0
        self._velocidade_digitacao = 2  # caracteres por frame
        self.nome_jogador = 'Aluno(a)'
        self.personagem_jogador = 'boy'
        self.retratos = RetratosDialogo()
        self.quadro = QuadroDialogo()

    def resolve_lines(self, linhas):
        return [(self.nome_jogador if falante in ('Aluno(a)', '{player}') else falante,
                 texto.replace('{player}', self.nome_jogador)) for falante, texto in linhas]

    def start(self, linhas, ao_concluir=None):
        if not linhas:
            if ao_concluir:
                ao_concluir()
            return
        self.linhas = self.resolve_lines(linhas)
        self.indice = 0
        self.ativo = True
        self.ao_concluir = ao_concluir
        self._caracteres_exibidos = 0

    def handle_event(self, evento):
        if not self.ativo:
            return
        if evento.type == pygame.KEYDOWN and evento.key in (
            pygame.K_e, pygame.K_RETURN, pygame.K_SPACE
        ):
            falante, texto = self.linhas[self.indice]
            if self._caracteres_exibidos < len(texto):
                self._caracteres_exibidos = len(texto)  # revela tudo de uma vez
                return
            self.indice += 1
            self._caracteres_exibidos = 0
            if self.indice >= len(self.linhas):
                self.ativo = False
                ao_finalizar = self.ao_concluir
                self.ao_concluir = None
                if ao_finalizar:
                    ao_finalizar()

    def update(self):
        if not self.ativo:
            return
        falante, texto = self.linhas[self.indice]
        if self._caracteres_exibidos < len(texto):
            self._caracteres_exibidos = min(len(texto), self._caracteres_exibidos + self._velocidade_digitacao)

    def _wrap(self, texto, largura_maxima):
        palavras = texto.split(' ')
        linhas, atual = [], ''
        for palavra in palavras:
            tentativa = (atual + ' ' + palavra).strip()
            if self.fonte.size(tentativa)[0] > largura_maxima:
                linhas.append(atual)
                atual = palavra
            else:
                atual = tentativa
        if atual:
            linhas.append(atual)
        return linhas

    def draw(self, superficie):
        if not self.ativo:
            return
        falante, texto = self.linhas[self.indice]
        texto_exibido = texto[: self._caracteres_exibidos]

        largura_texto = superficie.get_width()-104
        linhas_completas = self._wrap(texto, largura_texto)
        altura = max(136, 64+len(linhas_completas)*20)
        retangulo_caixa = pygame.Rect(24, superficie.get_height()-altura-14,
                                     superficie.get_width()-48, altura)
        destaque = tema.CIANO if falante in ('Entidade', 'IFVania', 'Sistema', 'Indexador') else tema.AMBAR
        interlocutor = falante if falante != self.nome_jogador else next(
            (nome for nome, _ in self.linhas if nome not in (self.nome_jogador, 'Sistema')), None)
        participantes = [(self.nome_jogador, 'esquerda')]
        if interlocutor:
            participantes.append((interlocutor, 'direita'))
        # Primeiro o ouvinte escurecido; por último o falante iluminado.
        for nome, lado in sorted(participantes, key=lambda item: item[0] == falante):
            imagem = self.retratos.obter(nome, self.nome_jogador, self.personagem_jogador)
            self.quadro.desenhar_busto(superficie, imagem, lado, retangulo_caixa.top+12, nome == falante)
        self.quadro.desenhar_painel(superficie, retangulo_caixa, destaque)
        largura_nome = min(retangulo_caixa.width-32, max(144, self.fonte_nome.size(falante.upper())[0]+38))
        x_nome = retangulo_caixa.x+16 if falante == self.nome_jogador else retangulo_caixa.right-largura_nome-16
        placa_nome = pygame.Rect(x_nome, retangulo_caixa.top-31, largura_nome, 34)
        pygame.draw.rect(superficie, (16, 35, 56), placa_nome, border_radius=6)
        pygame.draw.rect(superficie, destaque, placa_nome, 2, border_radius=6)
        tema.text(superficie, self.fonte_nome, falante.upper(), (placa_nome.x+19, placa_nome.y+7), destaque)
        linhas_quebradas = self._wrap(texto_exibido, largura_texto)
        for i, linha in enumerate(linhas_quebradas):
            tema.text(superficie, self.fonte, linha, (retangulo_caixa.x+28, retangulo_caixa.y+26+i*20))
        if self._caracteres_exibidos >= len(texto):
            fonte_dica = pygame.font.Font(None, 18)
            dica = fonte_dica.render('E / ENTER / ESPAÇO   continuar', True, (177, 203, 214))
            superficie.blit(dica, dica.get_rect(bottomright=(retangulo_caixa.right-38, retangulo_caixa.bottom-16)))
            x, y = retangulo_caixa.right-24, retangulo_caixa.bottom-22
            pygame.draw.polygon(superficie, (177, 203, 214), [(x-3, y-4), (x+3, y), (x-3, y+4)])
