# Carga e retratos — 10/11/2026

Capturas reais de Pygame, SDL dummy. A prévia animada registra 72 atualizações:
movimento com carga, carga completa e parada mantendo o efeito. Os chefes e
inimigos ficam fora da atualização nesta captura para isolar a apresentação;
não é teste de sobrevivência. Capturas de diálogo usam falas preparadas para
inspeção dos retratos de cada identidade.

- [Prévia animada](previa_carga.gif)
- [Menino carregando](carga_menino.png) / [Menina carregando](carga_menina.png)
- [Protagonista](retrato_protagonista.png), [Max](retrato_max.png), [Romerito](retrato_romerito.png), [IFVania](retrato_ifvania.png)

Reproduzir: `python -m ferramentas.capturar_carga_dialogos /tmp/ifvania_carga --quadros`.
A flag opcional exporta a sequência para compor GIF/vídeo com ffmpeg, que não
é dependência do jogo. Os sprites vieram de `image_gen` integrada; prompt em
`recursos/fontes_arte/instrucoes_caminhada_carregando.json`. Os retratos usam
figuras já existentes. Não foram alterados danos, colisões ou comandos.
