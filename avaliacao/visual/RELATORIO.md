# Avaliação visual e funcional — IFVania

Data: 09/11/2026. Escopo: conteúdo disponível, prólogo e fases 1 e 2.

## Método e limites

Capturas reais de `Jogo._draw()`, com superfícies, sprites, fontes e composição do Pygame 2.6.1, Python 3.12.10 e SDL dummy. Há **34 PNGs antes e 34 depois**, em 960 × 540. Não são imagens simuladas. [Contato inicial](contato_antes.png) e [contato final](contato_depois.png).

`capturar_cenas.py` prepara posições e estados para inspeção e injeta comandos de caminhada, salto e ataque. Combates são amostras com chefe ativado diretamente; derrota, cartão e fim de conteúdo são estados preparados. Isso não demonstra uma partida contínua, sobrevivência ou vitória por habilidade humana. A captura `ataque` registra o estado após entrada X, mas não comprova isoladamente dano; os testes de combate verificam os acertos. A imagem inicial da aula foi capturada antes de revelar texto; a final revela a fala para facilitar a leitura, sem mudança no sistema de diálogo.

O ponto de entrada `principal.py` ficou ativo por dois segundos sem erro e foi encerrado pelo avaliador. Não houve janela visível, avaliação de áudio nem partida manual. As fases 3–6 não foram avaliadas porque não estão implementadas. Não foi usada a arte não rastreada `referencia/img.png`.

## Diagnóstico inicial por ambiente

- **Menu e seleção:** fachada reconhecível, tipografia hierarquizada, contraste e indicação da seleção bons. Não justifica redesenho. Evidências: [menu](antes/01_menu.png), [seleção](antes/02_selecao.png), [nome](antes/03_nome.png).
- **Aula e memória:** iluminação fria/quente coesa, mobiliário detalhado, alunos presentes e memória doméstica distinta. A abertura concentra muita informação em texto e monitor ampliado; ritmo de leitura ainda exige observação humana. [Aula](depois/04_aula.png), [memória](antes/05_memoria.png), [hipnose](antes/06_hipnose.png).
- **Pátio:** vegetação, pilares, piso e luminárias transmitem campus escolar com boa profundidade pictórica. Bancos parecem apoios, mas são decorativos; isso pode criar expectativa incorreta de colisão. O percurso permanece essencialmente uma caminhada até a porta. [Início](antes/07_corridor_inicio.png), [A28](antes/08_corridor_destino.png).
- **A28 e transporte:** continuidade de materiais com a aula e destino da sucção reconhecível. A captura de um instante não homologa duração ou compreensão da cena. [A28](antes/08_lab_destino.png), [sucção](antes/09_succao.png).
- **Mundo virtual:** tampos claros e faixas distinguem plataformas do mobiliário; bugs contrastam bem. Repetição do laboratório, figuras dos colegas e grande faixa inferior em grade reduzem variedade. O corpo visual de 80 px excede o corpo físico de 40 px por contrato: sobreposição visual não prova falha física. [Início](antes/fase1_inicio.png), [região central](antes/fase1_regiao_900.png), [combate](antes/fase1_combate.png).
- **Biblioteca:** fundo rico e coerente com o campus, mas objetos funcionais muito discretos. O portão era desenhado como uma coluna sem suas faixas; salto fazia a composição toda deslizar verticalmente. Estantes se repetem em módulos de 960 px. Indexador é mais esquemático que os ambientes. [Percurso](antes/fase2_regiao_900.png), [portão/arena](antes/fase2_regiao_2050.png), [salto](antes/fase2_salto.png).
- **Pausa, derrota e encerramento:** mensagens legíveis e funcionais, apresentação austera. Encerramento informa corretamente que a jornada continua; não há vitória final da campanha. [Pausa](antes/fase2_pausa.png), [derrota](antes/derrota.png), [fim](antes/fim_conteudo.png).

## Problemas priorizados

| Local | Problema e evidência | Impacto e causa provável | Proposta / prioridade / estado |
|---|---|---|---|
| Biblioteca, portão | Faixas apagadas: [antes](antes/fase2_regiao_2050.png) | Barreira parece coluna decorativa; sólidos desenhados depois do fundo cobriam a sinalização. Coordenadas Y das faixas também ignoravam a câmera. Comprovado por renderização e código. | Desenhar interativos após sólidos e usar coordenadas da câmera. **Alta, corrigido.** |
| Biblioteca, módulo e arquivos | Pequenos retângulos numerados sem identificação: [antes](antes/fase2_regiao_900.png) | Descoberta e objetivo pouco claros; peso visual menor que estantes e mesas. Observação visual; efeito no tempo de descoberta ainda inferido. | Rótulos locais, estado LIDO, fundo discretamente escurecido. **Alta, implementado.** |
| Biblioteca, HUD | Contador sem painel: [antes](antes/fase2_regiao_2050.png) | Cenário/portão atravessam o texto; desenhado dentro do fundo. Comprovado visualmente. | Painel de objetivo após mundo e HUD, entre colunas laterais. **Média, corrigido.** |
| Fases virtuais, saltos | Cenário acompanha toda variação de Y: [antes](antes/fase2_salto.png) | Referências visuais mudam a cada salto. Câmera centralizava ambos os eixos continuamente. Movimento comprovado; desconforto humano não medido. | Zona vertical 180–370 px, acompanhamento fora dela e limites do mapa. **Média, implementado.** |
| Fase 1, trecho inferior | Grande área de grade pouco variada: [início](antes/fase1_inicio.png) | Composição desperdiça parte da tela; piso físico alto e preenchimento simples. Comprovado visualmente. | Revisar enquadramento e fundações com novas composições antes de mudar geometria. **Média, pendente.** |
| Pátio e biblioteca | Mesas/bancos parecem possíveis apoios: [pátio](antes/07_corridor_inicio.png) | Possível tentativa de pouso frustrada. Decoração pictórica sem colisão; expectativa é inferência. | Observar iniciantes e reduzir contraste nas bordas ambíguas se confirmado. **Média, pendente.** |
| Fases 1 e 2 | Módulos de fundo repetidos: [fase 1](antes/fase1_regiao_1400.png) | Menor sensação de descoberta; repetição da mesma imagem. | Variações de salas e marcos por região preservando colisões. **Média, pendente.** |
| Biblioteca, Indexador | Corpo geométrico simples: [combate](antes/fase2_combate.png) | Menor acabamento que os cenários. Observação visual. | Sprites com poses de aviso, execução e recuperação; preservar classe e hitboxes. **Baixa, pendente.** |
| Campanha disponível | Balanceamento de sobrevivência não homologado | Testes usam proteção artificial para isolar arma/estados; não provam diversão. Limitação comprovada dos testes, não defeito de dificuldade confirmado. | Partidas humanas com ambos os protagonistas. **Alta, pendente.** |

Nenhum bloqueio crítico foi demonstrado nesta execução. Os testes de subida não demonstram alcançabilidade de todo ponto do mapa; não se afirma ausência de áreas inacessíveis.

## Jogabilidade e testes

Base inicial: **108 testes passaram**. Final: **110 testes passaram em 5,338 s**, suíte completa sem janela/áudio. Dois novos testes verificam estabilidade vertical/limites da câmera e pixel visível da faixa do portão com deslocamento de câmera, preservação dos sólidos e remoção do aviso após abertura.

A suíte existente exercita percurso básico até a saída com ambos os protagonistas, subida obrigatória com salto duplo, aceleração/combate, bloqueio do chicote por paredes, contato único por golpe, transformação, pausa, perda de foco, consultas, retomada e limpeza de ameaças. As lutas automatizadas com invulnerabilidade comprovam funcionamento da arma e estados, não dificuldade equilibrada. A caminhada parada contra parede já tem regressão.

Medição independente com física real em piso plano, sem inimigos: **ambos os protagonistas tiveram resultados iguais**. Velocidade máxima 3,2 px/quadro atingida no quinto quadro; frenagem em 4 quadros e 4 px. Salto básico com ápice 114 px, duração 38 quadros e alcance 113 px iniciando do repouso e mantendo direita. A 60 atualizações/s: aceleração em ~83 ms, frenagem ~67 ms e voo ~633 ms. Esses tempos dependem da cadência fixa do jogo. Não foram alterados gravidade, força de salto ou velocidade porque não houve evidência suficiente de defeito.

Dados: [medidas_movimento.json](medidas_movimento.json). Reprodução:

```bash
.venv/bin/python avaliacao/visual/capturar_cenas.py avaliacao/visual/nova_captura
.venv/bin/python avaliacao/visual/medir_movimento.py
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy PYGAME_HIDE_SUPPORT_PROMPT=1 .venv/bin/python -m unittest discover -s testes -q
```

## Implementação e comparação

| Arquivo | Alteração | Efeito verificado |
|---|---|---|
| `mundo/camera.py` | Zona vertical estável após enquadramento inicial | Salto comum movimenta menos o fundo, subida alta continua acompanhada. |
| `mundo/biblioteca.py` | Separação fundo/interativos/objetivos, camada escura apenas no fundo, rótulos e faixas | Objetos mais legíveis e aviso do portão visível. Nenhuma arte aprovada sobrescrita. |
| `mundo/fase.py` | Interativos da biblioteca após sólidos | A barreira deixa de apagar suas próprias faixas. |
| `jogo.py` | Objetivos após composição do HUD | Contador com painel legível e dicas próximas preservadas. |
| `testes/teste_avaliacao_visual.py` | Duas regressões | Câmera, limites, sinal do portão e geometria verificados. |
| `avaliacao/visual/` | Scripts, dados, relatório e capturas | Avaliação reproduzível com limitações explícitas. |

Comparações: [salto antes](antes/fase2_salto.png) / [depois](depois/fase2_salto.png); [arquivos antes](antes/fase2_regiao_900.png) / [depois](depois/fase2_regiao_900.png); [portão antes](antes/fase2_regiao_2050.png) / [depois](depois/fase2_regiao_2050.png). As duas séries usam os mesmos comandos e posições; a mudança de enquadramento no salto é resultado da câmera. O novo enquadramento deve ser homologado manualmente também ao descer de plataformas altas.

## Notas ponderadas

Notas são julgamento técnico provisório sobre o conteúdo disponível; não certificam experiência humana. Nenhuma dimensão foi excluída.

| Dimensão | Peso | Inicial | Final | Evidência / fundamento |
|---|---:|---:|---:|---|
| Arte dos cenários | 20% | 7,5 | 7,5 | Campus reconhecível e iluminação consistente; módulos repetidos e contraste entre chefe e fundo permanecem. |
| Composição e legibilidade | 15% | 6,0 | 7,0 | Rótulos e barreira corrigidos; grade inferior e decoração ambígua permanecem. |
| Movimentação | 15% | 7,0 | 7,5 | Aceleração/frenagem curtas medidas e controles cobertos; câmera menos móvel demonstrada, conforto manual pendente. |
| Plataformas/colisões/física | 15% | 7,0 | 7,0 | Percurso básico e subida obrigatória automatizados para ambos; cobertura espacial incompleta. |
| Combate/interatividade | 10% | 6,5 | 6,5 | Avisos, chicote e estados testados; sobrevivência não validada. |
| Diversidade/criatividade | 10% | 6,5 | 6,5 | Escola corrompida, corrida e arquivo têm identidade; percurso e fundos repetitivos. |
| Imersão/ambientação | 10% | 7,0 | 7,0 | Memória, hipnose e sucção renderizadas; áudio e ritmo não avaliados. |
| Polimento técnico/visual | 5% | 6,0 | 7,0 | Portão e objetivo corrigidos, 110 testes; telas finais simples e homologação pendente. |
| **Geral: soma(nota × peso)/100** | **100%** | **6,80** | **7,08** | Ganho limitado às melhorias demonstradas. |

A etapa 11 do plano continua aberta. Próximo ciclo: partida humana de sobrevivência e leitura do salto/câmera; depois, marcos regionais e redução de áreas visualmente vazias, com novas capturas comparáveis.
