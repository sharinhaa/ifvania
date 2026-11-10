"""Integração do ponto de entrada e dos recursos após reorganização."""
import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')
os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import pygame
from sistema import recursos
from sistema.jogo import Jogo

RAIZ = Path(__file__).resolve().parents[1]


class TestesOrganizacao(unittest.TestCase):
    def test_principal_inicializa_pela_raiz_e_por_diretorio_externo(self):
        ambiente = {**os.environ, 'SDL_VIDEODRIVER': 'dummy',
                    'SDL_AUDIODRIVER': 'dummy', 'PYGAME_HIDE_SUPPORT_PROMPT': '1'}
        with tempfile.TemporaryDirectory(prefix='ifvania_inicio_') as externo:
            for diretorio, entrada in ((RAIZ, 'principal.py'), (externo, str(RAIZ/'principal.py'))):
                with self.subTest(diretorio=str(diretorio)):
                    processo = subprocess.Popen([sys.executable, '-u', entrada], cwd=diretorio,
                                                env=ambiente, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                text=True)
                    try:
                        try:
                            saida, erros = processo.communicate(timeout=1.5)
                        except subprocess.TimeoutExpired:
                            processo.terminate()
                            saida, erros = processo.communicate(timeout=5)
                        else:
                            self.fail(f'Jogo encerrou antes da interação: {processo.returncode}\n{saida}\n{erros}')
                        self.assertNotIn('Traceback', erros)
                        self.assertNotIn('[recursos] aviso', saida)
                    finally:
                        if processo.poll() is None:
                            processo.kill()
                            processo.communicate()

    def test_campanha_e_imagens_carregam_fora_da_raiz_sem_substitutos(self):
        anterior = Path.cwd()
        with tempfile.TemporaryDirectory(prefix='ifvania_recursos_') as externo:
            try:
                os.chdir(externo)
                recursos.clear_cache()
                recursos._avisos_ausentes.clear()
                jogo = Jogo()
                jogo._draw()
                for ambiente in ('classroom', 'corridor', 'lab'):
                    jogo._load_school(ambiente, novo_jogador=True)
                    jogo.fase.draw(jogo.tela)
                for indice in range(len(jogo.definicoes_fases)):
                    jogo._load_level(indice, novo_jogador=True)
                    jogo.fase.draw(jogo.tela)
                for arquivo in (RAIZ/'recursos/imagens').rglob('*.png'):
                    recursos.load_image(arquivo.relative_to(RAIZ/'recursos/imagens').as_posix())
                self.assertFalse(recursos._avisos_ausentes)
                self.assertEqual(Path.cwd(), Path(externo).resolve())
            finally:
                os.chdir(anterior)
                pygame.quit()
