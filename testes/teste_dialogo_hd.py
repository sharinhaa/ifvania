"""Bustos em alta resolução, escuta escurecida e troca do falante."""
import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')
os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')
from pathlib import Path
import unittest
from unittest.mock import patch
import pygame
from interface.dialogo import CaixaDialogo
from interface.quadro_dialogo import QuadroDialogo
from interface.retratos import RetratosDialogo


class TestesDialogoHd(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((960, 540))

    def tearDown(self):
        pygame.quit()

    def test_bustos_da_campanha_tem_resolucao_e_transparencia_reais(self):
        retratos = RetratosDialogo()
        for personagem in ('boy', 'menina'):
            for nome in ('Alex', 'Professor Max', 'Professor Romerito', 'IFVania', 'Entidade', 'Sistema', 'Indexador'):
                with self.subTest(nome=nome, personagem=personagem):
                    figura = retratos.obter(nome, 'Alex', personagem)
                    self.assertGreaterEqual(figura.get_width(), 768)
                    self.assertGreaterEqual(figura.get_height(), 1152)
                    self.assertEqual(figura.get_at((0, 0)).a, 0)
                    self.assertGreater(figura.get_bounding_rect().height, 200)
        pasta = Path(__file__).resolve().parents[1]/'recursos/fontes_arte/retratos_dialogo'
        for arquivo in pasta.glob('*.png'):
            figura = pygame.image.load(str(arquivo))
            self.assertGreaterEqual(figura.get_width(), 1024)
            self.assertGreaterEqual(figura.get_height(), 1536)

    def test_ouvinte_escurece_sem_alterar_a_imagem_original(self):
        retrato = RetratosDialogo().obter('Alex', 'Alex', 'menina')
        original = pygame.image.tostring(retrato, 'RGBA')
        quadro = QuadroDialogo()
        claro, escuro = pygame.Surface((960, 540)), pygame.Surface((960, 540))
        claro.fill((0, 0, 0)); escuro.fill((0, 0, 0))
        destino = quadro.desenhar_busto(claro, retrato, 'esquerda', 400, True)
        quadro.desenhar_busto(escuro, retrato, 'esquerda', 400, False)
        self.assertTrue(claro.get_rect().contains(destino))
        self.assertGreater(pygame.transform.average_color(claro)[0], pygame.transform.average_color(escuro)[0])
        self.assertEqual(pygame.image.tostring(retrato, 'RGBA'), original)

    def test_par_de_interlocutores_permanece_e_destaque_troca_com_a_fala(self):
        caixa = CaixaDialogo()
        caixa.nome_jogador = 'Alex'
        caixa.start([('Aluno(a)', 'Professor?'), ('Professor Max', 'Oi, Alex.')])
        tela = pygame.Surface((960, 540))
        with patch.object(caixa.quadro, 'desenhar_busto', wraps=caixa.quadro.desenhar_busto) as desenhar:
            caixa.draw(tela)
            self.assertEqual(desenhar.call_count, 2)
            self.assertEqual(desenhar.call_args.args[2], 'esquerda')
            self.assertTrue(desenhar.call_args.args[4])
            caixa.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_e))
            self.assertEqual(caixa.indice, 0)
            caixa.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_e))
            desenhar.reset_mock()
            caixa.draw(tela)
            self.assertEqual(desenhar.call_count, 2)
            self.assertEqual(desenhar.call_args.args[2], 'direita')
            self.assertTrue(desenhar.call_args.args[4])
