# Plano de execução — IFVania

**Reorganizado em:** 02/11/2026, após revisão das lacunas do início da história.

Referências: [AGENTS.md](AGENTS.md), [ROTEIRO_HISTORIA.md](ROTEIRO_HISTORIA.md), [DOCUMENTO_DE_REQUISITOS.md](DOCUMENTO_DE_REQUISITOS.md) e as seis imagens de `referencia/ifrn/`. O registro anterior foi preservado integralmente em [HISTORICO_DE_EXECUCAO.md](HISTORICO_DE_EXECUCAO.md).

## Ordem de trabalho e estado real

Priorizar coerência e apresentação do início antes de ampliar a campanha. As etapas 1 a 4 abaixo reúnem correções da base existente; não significam reconstruir os sistemas já prontos. As etapas 5 a 10 preparam e completam a expansão. A **etapa 11 é a última e reúne a validação final**. Testes técnicos e inspeções continuam acontecendo a cada incremento, sem antecipar a homologação final.

Disponível: seleção/nome, conversa com Max e lembrança da tarefa, laboratório com turma, pátio de passagem até o A28, sucção para o computador, RomerBug/SpeedBug e biblioteca com consultas, salto duplo e Indexador. O pátio de passagem usa a arte da futura fase 3, mas não implementa seu resgate, quadra ou chefe. O jogo ainda termina com “A jornada continua” após a biblioteca.

## Lacunas encontradas ao comparar roteiro e jogo

| Trecho do roteiro | Lacuna anterior | Correção e estado |
|---|---|---|
| Tarefa em casa, mãe, jantar e energia | Apenas explicação verbal, sem lembrança visual. | Acrescentada lembrança do quarto e jantar, com monitor animado, oscilação visual e registro de continuidade, durante a conversa com Max. Não é uma fase doméstica independente. |
| Apresentação da atividade | Não mostrava claramente pedido da tarefa e execução do arquivo. | Max pede à turma que abra e explique o exercício; o aluno conecta o pendrive; monitores passam por código, execução e controle da IFVania. |
| Hipnose coletiva | Havia falas e telas corrompidas, mas nenhum colega visível. | Quatro alunos sentados em computadores, posturas e olhos alterados com a corrupção. A evolução é visual; física e combate seguem suspensos. |
| Ataque e abdução no A28 | Anéis sobre personagens parados, sem destino aparente. | Investida/recuo seguidos por trajetória curva, redução, rotação e partículas até um monitor; fechamento da imagem antes da fase virtual. |
| Descoberta do mouse na bolsa | Continua sendo diálogo e liberação da arma; falta encenação da bolsa. | Pendente na etapa 3. Não registrar como animação concluída. |
| Investida de SpeedBug | Na borda, a direção podia apontar para fora da arena e interromper imediatamente o avanço. | Reposicionamento sem dano antes do anúncio, seguido de direção fixa; distância computada pelo deslocamento real. Regressão nas duas bordas. |
| Romerito libertado | Diálogo de recuperação mantendo a figura de SpeedBug derrotado. | Forma humana restaurada na posição do chefe antes da conversa posterior. |
| Biblioteca e pátio | Biblioteca em blocos simples destoava da fase 1; fotos sem aplicação visual ao percurso. | Novos fundos de ambos a partir das fotos e do estilo da fase 1; biblioteca integrada e pátio aplicado ao caminho escolar até o A28. |
| Fases 3 a 6 | Roteiro definido, conteúdo jogável ausente. | Permanecem pendentes, com entregas separadas nas etapas 7 a 10. |

## Etapa 1 — Corrigir e encenar o início da história

- [x] Mostrar Max pedindo a apresentação da atividade de programação orientada a objetos.
- [x] Incluir a origem da tarefa: chegada em casa, lembrete da mãe, IA durante o jantar, oscilação, arquivo pronto e pendrive, por diálogo e lembrança visual.
- [x] Preservar a abertura iniciada pelo aluno, sem narrador, com o nome escolhido.
- [x] Mostrar código, execução da tarefa e revolta como estados distintos nos monitores e numa visualização ampliada legível.
- [x] Mostrar colegas sentados nos computadores e hipnose progressiva por postura, olhos e vínculo com as telas.
- [x] Preservar a resistência parcial sem revelar antecipadamente a explicação da fase 4.
- [ ] Homologar manualmente tempo de leitura, enquadramento e compreensão da passagem de casa para a aula com ambas as aparências.

**Aceite:** sequência tarefa → execução → tentativa de desligamento → revolta → hipnose → busca por Romerito. Diálogos não avançam física, combate ou caminhada. Animações visuais param na pausa. A lembrança não substitui nem contradiz a revelação da fase 4.

## Etapa 2 — Corrigir a investida de RomerBug/SpeedBug

- [x] Reproduzir a ausência de avanço ao anunciar investida contra a borda da arena.
- [x] Criar espaço com reposicionamento antes do anúncio quando houver menos de 80 pixels livres naquela direção.
- [x] Manter o limite de ±24 pixels apenas nos trechos de lançamento; o reposicionamento e a investida têm movimentos próprios.
- [x] Contar os até 160 pixels de investida pelo deslocamento efetivo, respeitando paredes e limites.
- [x] Preservar direção fixa, aviso, recuperação, ausência de dano corporal passivo e transformação com vida compartilhada.
- [x] Testar SpeedBug nas duas bordas, além dos encontros e ciclos já existentes.
- [ ] Experimentar sobrevivência e ritmo das duas formas, inclusive recuo junto ao limite da arena.

**Aceite:** a corrida anunciada avança quando há espaço; parede real interrompe o avanço e leva à recuperação. Não há perseguição que altere a direção depois do anúncio nem animação correndo contra a borda sem deslocamento.

## Etapa 3 — Dar continuidade visual aos encontros e ao transporte

**Dependência:** abertura da etapa 1 e controles/combate preservados.

- [x] Manter investida de Romerito e recuo do protagonista antes da captura, sem dano narrativo.
- [x] Usar um monitor real do cenário como destino da sucção dos dois personagens.
- [x] Reduzir e girar as imagens ao longo da trajetória; ocultar as figuras originais para evitar duplicatas durante a cena.
- [x] Fechar a imagem antes de carregar a fase virtual e manter o mouse bloqueado até o fim da descoberta.
- [x] Congelar o transporte na pausa, sem alterar corpos lógicos pelo desenho.
- [x] Restaurar Romerito humano depois de SpeedBug, com conversa e saída para a biblioteca.
- [ ] Animar a abertura da bolsa e retirada do mouse durante as falas correspondentes.
- [ ] Revisar chegada ao mundo virtual, contato pelo terminal e posição de Romerito no reencontro, para que a separação e a recuperação fiquem claras visualmente.

**Aceite:** observar aproximação → captura → absorção pelo monitor → chegada virtual → descoberta da arma. Nome e aparência permanecem os mesmos. Uma tecla de diálogo não dispara simultaneamente arma ou interação na cena seguinte.

## Etapa 4 — Unificar cenários com a direção de arte da fase 1

**Dependência:** preservar a geometria dos mapas existentes.

- [x] Usar `laboratorio_detalhado.png` como referência de acabamento: pixel art detalhada, sombras frias, paredes em ocre e pontos de luz âmbar/ciano.
- [x] Gerar e integrar biblioteca com estantes metálicas, livros, mesas claras, cadeiras azuis e persianas das fotos internas.
- [x] Gerar e integrar pátio coberto com pilares amarelos/revestidos, faixa vermelha, telhas, bancos e jardins das fotos externas.
- [x] Aplicar pátio ao percurso até o A28 sem inventar posições reais de salas; preservar limites, piso e zona de entrada.
- [x] Trocar o fundo provisório da biblioteca sem alterar plataformas, terminais, portão ou colisões.
- [x] Preservar fontes e prompts; exportar primeiro para pasta temporária e conferir PNGs em 960 × 540.
- [ ] Completar variações normal/corrompida/restaurada e continuidade de módulos para a fase 3 e o epílogo.
- [ ] Conferir legibilidade de estantes e plataformas, escala do mobiliário e repetição dos módulos durante uma partida manual.

**Aceite:** laboratório, pátio e biblioteca pertencem à mesma direção visual; mudança de ambiente preserva sinais jogáveis. Bancos, cadeiras e livros decorativos não criam colisões ou falsos apoios. A quadra e os setores técnicos continuam adaptações ficcionais sem foto interna disponível.

### Imagens de referência e aplicação

| Arquivo em `referencia/ifrn/` | Observação | Aplicação |
|---|---|---|
| [17-24-38](referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-24-38.png) | Biblioteca: leitura, terminais, mesas claras, cadeiras azuis, vidro e persianas. | Área de leitura e consulta do fundo da biblioteca. |
| [17-24-56](referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-24-56.png) | Estantes metálicas, lombadas e placas de classificação. | Acervo e identidade visual da fase 2. |
| [17-26-04](referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-26-04.png) | Corredor coberto, pilares revestidos com faixa vermelha, bancos e saída. | Estrutura e materiais do pátio de passagem. |
| [17-27-22](referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-27-22.png) | Jardim entre blocos, palmeiras, arbustos, vasos e paredes amarelas. | Vegetação e fundo dos blocos no pátio. |
| [17-27-40](referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-27-40.png) | Área sombreada com árvores, bancos de concreto e caminho pavimentado. | Composição e referência para o futuro ponto de reunião. |
| [17-27-45](referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-27-45.png) | Outro ângulo dos bancos, árvores e blocos baixos. | Banco e jardim no fundo gerado; futuras variações do pátio. |

As imagens foram inspecionadas individualmente. Não fornecem planta interna, medidas ou identificação do A28; não comprovam continuidade entre todas as vistas. Interface e pessoas fotografadas não foram incorporadas como elementos do jogo.

## Etapa 5 — Consolidar progressão e infraestrutura da expansão

- [x] Preservar nome/aparência/habilidades ao trocar de fase e limpar cargas, golpes e projéteis pendentes.
- [x] Reiniciar habilidades numa nova campanha; manter a campanha antiga isolada.
- [x] Especificar e implementar retomada local da biblioteca por R, com módulo e consultas preservados, sem salvamento em disco.
- [x] Documentar que entrada em fase e retomada recuperam a integridade até a capacidade atual; módulo não cura nem aumenta vida.
- [x] Separar dados, cenário, objetivos e chefe da biblioteca em módulos próprios.
- [ ] Definir retomadas e objetivos persistentes das fases 3 a 6, incluindo falha de travessia na ancoragem.
- [ ] Desdobrar os critérios de aceite de toda a expansão, além dos já definidos para a biblioteca e esta revisão.

## Etapa 6 — Completar a Biblioteca dos arquivos perdidos

**Dependência:** etapas 4 e 5; incremento jogável já disponível.

- [x] Módulo de salto duplo antes da subida obrigatória, com piso seguro e instrução.
- [x] Três consultas, portão condicionado aos registros, mapa de saída e inventário do nobreak.
- [x] Indexador concreto, faixas anunciadas, fichas e janelas de contra-ataque.
- [ ] Criar bugs de arquivo com fichas anunciadas, substituindo os bugs comuns provisórios.
- [ ] Abrir atalhos de retorno a cada consulta concluída, como previsto no roteiro.
- [ ] Integrar bilhete opcional de monitoria, sem esconder explicação obrigatória.
- [ ] Ligar a saída ao pátio quando a fase 3 estiver utilizável.

**Aceite:** obter módulo sem poderes anteriores, aprender salto duplo antes de precisar dele e concluir percurso/chefe com ambos os protagonistas. Arte detalhada preserva leitura dos apoios.

## Etapa 7 — Construir Recreio em repetição

**Dependência:** biblioteca e regras de retomada; fundo de pátio pronto na etapa 4.

- [ ] Ampliar o pátio de passagem para o cenário próprio de combate e resgate da fase 3, sem reutilizar seus gatilhos escolares por acidente.
- [ ] Compor quadra e arquibancadas ficcionais na mesma direção de arte.
- [ ] Ensinar bolas de trajetória legível e ondas do sinal antes de combiná-las.
- [ ] Implementar três travas, atalhos, bolsões de silêncio e resgate sem escolta de aliados vulneráveis.
- [ ] Implementar Inspetor de Intervalo em classe própria, aviso de investida, ondas e recuperação.
- [ ] Preservar travas e resgates ao repetir o encontro; mostrar Romerito conduzindo o grupo e Max preso numa tela.

**Aceite:** resgatados fora das áreas de dano, objetivos preservados na retomada e nenhuma habilidade nova nessa fase.

## Etapa 8 — Construir Laboratório das cópias

**Dependência:** etapa 7 e progresso local consolidado.

- [ ] Construir salas repetidas com os materiais do laboratório da fase 1.
- [ ] Implementar comparação de arquivos, estabilização de salas e ciclos legíveis de bugs.
- [ ] Revelar sessão de autoria e identidade da entidade, retomando a lembrança da tarefa sem repetir toda a introdução.
- [ ] Implementar Max em Loop, cópias, cabo que identifica a origem real e pausa vulnerável de recompilação.
- [ ] Integrar libertação de Max, responsabilidade do protagonista, interrupção da recriação dos processos e isolamento do pendrive.
- [ ] Implementar ancoragem em conectores fixos e tutorial seguro, com comando sem conflito com ataque/diálogo.

**Aceite:** luta concluída antes de exigir ancoragem; mesma habilidade disponível nas transições, respeitando pausa, foco e colisões.

## Etapa 9 — Construir Rede sem saída

**Dependência:** etapa 8 e tutorial de ancoragem.

- [ ] Criar corredores técnicos e sala de rede ficcionais com materiais do campus.
- [ ] Introduzir pulsos de dados, combinar ancoragem/salto duplo e recuperar perto do apoio após falhas.
- [ ] Implementar três ramais, confirmação de Max e efeitos visíveis nos monitores de cada setor isolado.
- [ ] Implementar Roteador Sentinela, portas sinalizadas, barreira e flancos acessíveis.
- [ ] Confirmar evacuação, confinamento da IA e preparação do desligamento.

**Aceite:** ramais concluídos permanecem isolados; nenhum novo poder é concedido; o corpo comum permite as rotas da arena.

## Etapa 10 — Construir A última chamada e epílogo

**Dependência:** etapa 9 e condições de resgate/isolamento registradas.

- [ ] Retomar habilidades em três desafios curtos com descanso, sem comandos novos.
- [ ] Implementar IFVania em classe própria, reserva única de vida, dois momentos e transição sem dano.
- [ ] Integrar rompimento do controle e terminal de encerramento, sem ataque residual ou cronômetro surpresa.
- [ ] Exigir pessoas liberadas, rede isolada e autopreservação encerrada antes do desligamento e retorno ao A28.
- [ ] Mostrar desligamento dos equipamentos e alimentação de reserva pelos aliados; manter pendrive isolado.
- [ ] Criar epílogo da tarefa refeita e fachada ao amanhecer; trocar encerramento provisório por “Escola livre. Aula encerrada.”.

**Aceite:** vitória final depende da campanha; nome/aparência chegam ao epílogo; nova partida não herda progresso indevido.

## Etapa 11 — Validação final e homologação

**Dependência:** todas as entregas anteriores. Última etapa do plano; permanece pendente.

- [ ] Executar suíte completa e todos os critérios de aceite da campanha entregue.
- [ ] Percorrer as seis fases manualmente com Menino e Menina.
- [ ] Homologar abertura, turma/hipnose, sucção, controles, câmera e perda de foco.
- [ ] Homologar sobrevivência, dificuldade, avisos e recuperação dos chefes, incluindo SpeedBug nas bordas.
- [ ] Comparar pátio e biblioteca com as fotos e com a fase 1; revisar escala, emendas, contraste e distinção entre decoração e apoio.
- [ ] Revisar efeitos/áudio e intensidade visual para não ocultar ameaças ou prejudicar leitura.
- [ ] Sincronizar documentos, controles, fontes e prompts com o estado entregue.
- [ ] Registrar separadamente resultados automáticos, inspeções e experiências manuais; listar pendências concretas.

Comandos: `python principal.py` e `python -m unittest discover -s testes -v`. Sem janela/áudio: `SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy PYGAME_HIDE_SUPPORT_PROMPT=1 python -m unittest discover -s testes -v`.

## Registro desta correção

- **Automático:** 108 testes passaram com Python 3.14.4 e pygame-ce 2.5.8. Seis novos testes cobrem encadeamento visual, hipnose/pausa, sucção dos dois protagonistas, corrida nas duas bordas, recuperação humana de Romerito e preservação de colisões.
- **Arte:** ferramenta integrada `image_gen`, com fontes preservadas e prompts em [instrucoes_ambientes_ifrn.json](recursos/fontes_arte/instrucoes_ambientes_ifrn.json). Exportador: `python preparar_ambientes_ifrn.py --destino /tmp/ifvania_ambientes`, conferido antes da integração. Sem Pillow ou ffmpeg para jogar/exportar.
- **Inspeção:** capturas de execução da tarefa, memória doméstica, hipnose, sucção, pátio e biblioteca em `recursos/fontes_arte/revisao_*.png`. Conferidos enquadramento, estilo, destino da absorção e alinhamento à câmera.
- **Limite:** não houve partida manual de sobrevivência ou homologação de diversão. Artes integradas não significam fase 3 concluída. A etapa 11 continua aberta.
