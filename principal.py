"""Ponto de entrada do IFVania.

Execute com:  python principal.py
Requer:       pip install -r configuracao/dependencias.txt
"""
from sistema.jogo import Jogo


def principal():
    Jogo().run()


if __name__ == "__main__":
    principal()
