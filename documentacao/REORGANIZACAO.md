# Reorganização do repositório — 10/11/2026

`principal.py` é o único arquivo Python da aplicação na raiz. A execução continua com `python principal.py`, sem alterar o diretório de trabalho do processo ou introduzir aliases dos módulos antigos.

## Estrutura

```text
ifvania/
├── principal.py
├── AGENTS.md
├── .gitignore
├── sistema/         # jogo, configurações, habilidades, recursos e sons
├── entidades/       # personagens, chefes, armas e projéteis
├── mundo/           # campanha, mapas, cenários, câmera e transições
├── interface/       # menus, diálogos, HUD e tema
├── recursos/
│   ├── imagens/     # 87 PNGs de execução, preservados integralmente
│   └── fontes_arte/ # atlas, prompts, originais e registros de arte
├── referencia/      # fotos e referências; imagem local preservada
├── testes/          # suíte e duas regressões da reorganização
├── ferramentas/     # exportadores e avaliação visual
├── configuracao/
│   └── dependencias.txt
├── documentacao/    # apresentação, roteiro, requisitos, plano e inventários
└── avaliacao/visual/ # relatório, métricas e capturas distintas
```

Exceções na raiz: `AGENTS.md` permanece para descoberta automática das instruções; `.gitignore` define exclusões para todo o repositório. Os diretórios locais `.git/`, `.venv/` e `.idea/` são metadados do Git, ambiente Python e configuração pessoal da IDE. Foram preservados e não são arquivos da aplicação; os dois últimos já estavam ignorados. Não foi criado outro arquivo de apresentação na raiz.

## Mapeamento anterior às exclusões

[Inventário original](inventario_antes.json): 421 arquivos rastreados, tamanho, SHA-256 e, para Python, importações e referências literais a recursos. [Movimentos](arquivos_movidos.json): origem/destino dos 25 arquivos movidos. A inspeção também cobriu documentação, registro dinâmico de chefes, nomes de imagens montados com f-strings, ferramentas, fontes e sons. Não havia CI, Makefile, pyproject.toml, setup.cfg ou tox.ini rastreados.

| Grupo | Uso identificado | Decisão |
|---|---|---|
| `principal.py` → `sistema.jogo` | Entrada da aplicação e máquina de estados | Entrada mantida; estado e serviços em `sistema/`. |
| Configurações, habilidades, recursos, sons | Importados por entidades, mundo, interface e testes, inclusive importação local de sons durante carga/impacto | Mover e atualizar todos os consumidores. |
| `entidades/`, `mundo/`, `interface/` | Componentes ativos da campanha | Estrutura existente preservada; imports atualizados. |
| `mundo/fases_antigas.py`, professores e sprites antigos | Chamados por cinco módulos de testes; `CLASSES_CHEFES` resolve tipos dos dados em execução | Preservados: não são arquivos sem uso, embora fora do menu atual. |
| Nove `preparar_*.py` | Regeneram personagens, caminhada, professores, chefes, transição e ambientes a partir dos atlas/fontes | Movidos para `ferramentas/`; importações internas e raízes atualizadas. |
| `gerar_recursos.py` | Gerador original documentado, também usado no ensino; pode sobrescrever imagens | Preservado em `ferramentas/`, com caminho independente do diretório atual. Requer Pillow, ausente neste ambiente; não executado. |
| Fontes e prompts de arte | Consumidos pelos exportadores e utilizados como registro de geração | Preservados; nos JSON, apenas comandos de exportação foram atualizados. |
| Fontes tipográficas e áudio | `pygame.font.Font(None, ...)` e síntese por `pygame.mixer.Sound(buffer=...)` | Não há TTF, música ou WAV externo para mover/apagar. |
| Scripts de captura/medição | Produzem as evidências da avaliação | Movidos para `ferramentas/`; execução por `python -m`. Captura padrão agora usa `avaliacao/visual/atual`, para preservar a série inicial. |
| Documentos e dependências | Referências, comandos e continuidade do desenvolvimento | Movidos; links, caminhos, imports exemplificados e comandos atualizados, inclusive em `AGENTS.md`. |

[Uso observado de recursos](uso_recursos.json): 70 imagens carregadas na amostra da campanha (duas aparências, três ambientes escolares, duas fases, transformação e projéteis), mais cinco nas fases antigas. As outras 12 não foram excluídas: 11 são saídas ainda regeneradas por ferramentas (`corredor_detalhado`, `laboratorio_sombrio`, fachada e oito quadros de caminhada), e `item_habilidade` é carregado ao criar coletáveis nos testes antigos. A lista exata está no JSON. Não observar uma imagem numa amostra não prova desuso. As imagens continuam sendo carregadas dinamicamente pelo nome relativo em `sistema.recursos`.

## Remoções comprovadas e preservações

Foram removidas **68 cópias PNG byte a byte idênticas** das séries de avaliação: **23.550.148 bytes (~22,46 MiB)**. Cada uma tem cópia canônica preservada com o mesmo SHA-256; [mapa de consolidação](capturas_consolidadas.json). Links dos documentos apontam para as cópias restantes. Relatórios e contagens históricas foram mantidos e anotados para explicar a consolidação. Nenhum frame distinto foi removido. Os contatos gerais continuam disponíveis.

Caches Python ignorados da aplicação foram limpos durante a movimentação; podem ser recriados normalmente. Nenhuma arte aprovada, fonte de geração, foto, documento histórico ou arquivo de código foi excluído por simplesmente parecer antigo. `referencia/img.png`, não rastreado antes do trabalho, permanece no mesmo local e com o mesmo SHA-256. Não havia outras alterações locais rastreadas no início.

O uso futuro de materiais históricos de `recursos/fontes_arte/originais/` e prévias antigas não está completamente estabelecido. São registros protegidos pela orientação de arte e podem servir à comparação ou recuperação; para removê-los seria necessário decidir quais referências históricas deixarão de ser mantidas e conferir seus consumidores documentais. Não foram classificados como lixo.

## Comandos atualizados

Execute estes comandos pela raiz do repositório:

```bash
python -m pip install -r configuracao/dependencias.txt
python principal.py
python -m unittest discover -s testes -v
python -m ferramentas.capturar_cenas /tmp/ifvania_capturas
python -m ferramentas.medir_movimento
python -m ferramentas.verificar_exportadores
python -m ferramentas.preparar_ambientes_ifrn --destino /tmp/ifvania_ambientes
```

Os demais exportadores seguem `python -m ferramentas.preparar_figuras_personagens`, `python -m ferramentas.preparar_figuras_chefes`, etc. A execução como módulo substitui os comandos dos scripts antigos na raiz. O verificador executa todos os nove exportadores em uma cópia temporária, sem substituir recursos da aplicação. `python -m ferramentas.gerar_recursos` continua opcional e exige Pillow; ele sobrescreve as artes originais se executado no projeto.

De outro diretório, informe o caminho do ponto de entrada:

```bash
python /caminho/para/ifvania/principal.py
```

O carregador resolve `recursos/imagens` a partir de `sistema/recursos.py`, sem depender de `cwd`. Os exportadores também resolvem suas fontes e destinos padrão a partir de `__file__`. No ambiente utilizado, o executável está em `.venv/bin/python`; `python` fica disponível ao ativar esse ambiente.

## Validação

- Antes: 112 testes passaram. Depois: suíte completa com 114 testes, incluindo inicialização real do ponto de entrada na raiz e em diretório temporário e carregamento da campanha/imagens fora da raiz sem placeholders.
- Os subprocessos do ponto de entrada ficaram em seu loop por 1,5 s em cada diretório, sem traceback ou aviso de imagem ausente; foram encerrados pelo teste.
- 34 frames reais do Pygame regenerados e **idênticos byte a byte** aos da revisão de profundidade anterior à reorganização. Menu, seleção, aula, pátio, A28, sucção, mapas, movimento, combate, pausa e encerramento estão nessa série. Estados preparados, sem afirmar partida humana contínua.
- Medidas automatizadas de movimento idênticas ao JSON anterior.
- Todos os 87 PNGs de execução carregados sem substitutos. Hashes de **195 arquivos binários de arte/referência rastreados**, mais a imagem local, preservados. Apenas documentação e comandos de exportação nos registros JSON foram atualizados em `recursos/fontes_arte`.
- Nove exportadores Pygame executados com sucesso em cópia temporária; 77 PNGs distintos exportados. Gerador original verificado estaticamente; Pillow não está instalado, portanto não foi executado.
- Links Markdown locais, sintaxe Python e `git diff --check` conferidos.

A validação foi offscreen com SDL dummy, Python 3.12.10 e Pygame 2.6.1. Não houve inspeção humana de janela ou áudio. Não foram alterados narrativa, controles, física, colisões ou apresentação. Nenhum commit ou publicação realizado.
