"""Regressões dos sprites de carga, energia contínua e retratos do diálogo."""
import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')
os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')
from collections import defaultdict
import unittest
from unittest.mock import patch
import pygame
from entidades.jogador import Jogador
from entidades.efeito_carga import desenhar_energia
from interface.dialogo import CaixaDialogo
from interface.retratos import RetratosDialogo
from interface import tema
from mundo.camera import Camera
from sistema import configuracoes


class TestesCargaRetratos(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((960, 540))
        self.piso = [pygame.Rect(0, 352, 3000, 100)]
        self.teclas = defaultdict(bool)

    def tearDown(self):
        pygame.quit()

    def carregar(self, jogador):
        jogador.handle_input(self.teclas, [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_k)])

    def test_sprite_de_carga_caminha_sem_mudar_corpo_ou_pes(self):
        for personagem in ('boy', 'menina'):
            jogador = Jogador(200, 312, personagem)
            jogador.no_chao = True
            self.carregar(jogador)
            figuras = set()
            for _ in range(40):
                jogador.handle_input(defaultdict(bool, {pygame.K_d: True}), [])
                jogador.update(self.piso, [])
                self.assertEqual(jogador.rect.size, (40, 40))
                self.assertEqual(jogador.rect.bottom, 352)
                self.assertIs(jogador.image, jogador.figuras['walk_charge_r'][jogador.quadro_animacao])
                figuras.add(pygame.image.tostring(jogador.image, 'RGBA'))
            self.assertGreater(len(figuras), 3)
            self.assertNotEqual(pygame.image.tostring(jogador.image, 'RGBA'),
                                pygame.image.tostring(jogador.figuras['walk_r'][jogador.quadro_animacao], 'RGBA'))
            jogador.handle_input(defaultdict(bool, {pygame.K_a: True}), [])
            jogador.update(self.piso, [])
            self.assertIs(jogador.image, jogador.figuras['walk_charge_l'][jogador.quadro_animacao])

    def test_energia_continua_depois_da_carga_completa_e_desenho_nao_muda_estado(self):
        jogador = Jogador(200, 312)
        jogador.no_chao = True
        self.carregar(jogador)
        imagens = []
        for _ in range(3):
            for _ in range(15): jogador.update(self.piso, [])
            if jogador.carga < configuracoes.TEMPO_CARGA: continue
            antes = (jogador.rect.copy(), jogador.carga, jogador.instante_carga, jogador.vida)
            tela = pygame.Surface((960, 540))
            desenhar_energia(tela, Camera(960, 540), jogador)
            imagens.append(pygame.image.tostring(tela, 'RGBA'))
            self.assertEqual((jogador.rect, jogador.carga, jogador.instante_carga, jogador.vida), antes)
        for _ in range(15): jogador.update(self.piso, [])
        tela = pygame.Surface((960, 540))
        desenhar_energia(tela, Camera(960, 540), jogador)
        imagens.append(pygame.image.tostring(tela, 'RGBA'))
        self.assertGreater(len(set(imagens)), 1)
        jogador.cancelar_entrada()
        self.assertEqual(jogador.instante_carga, 0)

    def test_retrato_respeita_falante_e_aparencia_do_protagonista(self):
        retratos = RetratosDialogo()
        menino = retratos.obter('Alex', 'Alex', 'boy')
        menina = retratos.obter('Alex', 'Alex', 'menina')
        self.assertNotEqual(pygame.image.tostring(menino, 'RGBA'), pygame.image.tostring(menina, 'RGBA'))
        self.assertIs(menina, retratos.obter('Alex', 'Alex', 'menina'))
        for falante in ('Professor Max', 'Professor Romerito', 'Entidade', 'IFVania', 'Sistema', 'Indexador'):
            self.assertGreater(retratos.obter(falante, 'Alex', 'menina').get_bounding_rect().width, 0)

    def test_retrato_troca_ao_avancar_fala_sem_consumir_duas_linhas(self):
        caixa = CaixaDialogo()
        caixa.nome_jogador = 'Alex'
        caixa.personagem_jogador = 'menina'
        caixa.start([('Aluno(a)', 'Oi, professor.'), ('Professor Max', 'Oi, Alex.')])
        tela = pygame.Surface((960, 540))
        with patch.object(caixa.retratos, 'obter', wraps=caixa.retratos.obter) as obter:
            caixa.draw(tela)
            self.assertEqual(obter.call_args.args, ('Alex', 'Alex', 'menina'))
            caixa.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_e))
            self.assertEqual(caixa.indice, 0)
            caixa.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_e))
            caixa.draw(tela)
            self.assertEqual(caixa.indice, 1)
            self.assertEqual(obter.call_args.args[0], 'Professor Max')

    def test_texto_longo_com_retrato_nao_e_truncado_em_tres_linhas(self):
        caixa = CaixaDialogo()
        texto = 'Precisamos encontrar os colegas e desligar a energia da escola. '*8
        caixa.start([('Professor Max', texto)])
        caixa._caracteres_exibidos = len(texto)
        with patch('interface.dialogo.tema.text', wraps=tema.text) as desenhar:
            caixa.draw(pygame.Surface((960, 540)))
        chamadas = desenhar.call_args_list
        falas = [chamada.args[2] for chamada in chamadas[1:]]
        self.assertEqual(' '.join(' '.join(falas).split()), ' '.join(texto.split()))
        for chamada in chamadas:
            self.assertGreaterEqual(chamada.args[3][1], 0)
            self.assertLess(chamada.args[3][1], 510)
