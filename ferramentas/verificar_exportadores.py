"""Executa exportadores Pygame em cópia temporária, protegendo as artes do jogo.

Na raiz: python -m ferramentas.verificar_exportadores
Pillow não é necessário; gerar_recursos é o gerador original opcional.
"""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile


def principal():
    raiz = Path(__file__).resolve().parents[1]
    ambiente = {**os.environ, 'SDL_VIDEODRIVER': 'dummy', 'SDL_AUDIODRIVER': 'dummy',
                'PYGAME_HIDE_SUPPORT_PROMPT': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
    resultados = []
    with tempfile.TemporaryDirectory(prefix='ifvania_exportadores_') as temporario:
        copia = Path(temporario)
        for pasta in ('ferramentas', 'sistema'):
            shutil.copytree(raiz/pasta, copia/pasta, ignore=shutil.ignore_patterns('__pycache__'))
        (copia/'recursos').mkdir()
        # Fontes são apenas lidas; destinos de exportação ficam dentro da cópia.
        shutil.copytree(raiz/'recursos/fontes_arte', copia/'recursos/fontes_arte')
        for arquivo in sorted((copia/'ferramentas').glob('preparar_*.py')):
            resultado = subprocess.run([sys.executable, '-m', 'ferramentas.'+arquivo.stem],
                                       cwd=copia, env=ambiente, capture_output=True, text=True)
            registro = {'ferramenta': arquivo.stem, 'codigo_saida': resultado.returncode}
            if resultado.returncode:
                registro['erro'] = resultado.stderr
            resultados.append(registro)
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
        print('PNGs distintos exportados:', len(list((copia/'recursos/imagens').rglob('*.png'))))
    return 0 if all(registro['codigo_saida'] == 0 for registro in resultados) else 1


if __name__ == '__main__':
    raise SystemExit(principal())
