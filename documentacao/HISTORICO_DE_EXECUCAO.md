# Histórico de execução anterior à revisão do início

Registro preservado em 02/11/2026. Números de etapas, estados e resultados abaixo são históricos. O plano ativo está em [documentacao/PLANO_DE_EXECUCAO.md](PLANO_DE_EXECUCAO.md).

# Plano de execução — IFVania

**Atualizado em:** 02/11/2026

Referências: `AGENTS.md`, `documentacao/DOCUMENTO_DE_REQUISITOS.md` versão 3.3, `documentacao/ROTEIRO_HISTORIA.md` e as seis capturas em `referencia/ifrn/`.

## Estratégia

Implementar por etapas verificáveis, preservando as alterações existentes no roteiro e nas referências visuais. As etapas 1 a 4 registram a base implementada. A expansão segue as etapas 5 a 10, e a etapa 11 reúne a validação final. Cada incremento recebe verificações técnicas e inspeção antes da próxima fase. A campanha antiga permanece isolada para manutenção e regressão; ela não define os chefes ou poderes das seis fases do roteiro atual.

## Etapa 1 — Dimensões e arquitetura dos bosses

- [x] Definir dimensões corporais comuns em `sistema/configuracoes.py`, 40 × 40 pixels, mantendo a altura corporal e aproximando a escala visual de humanos e bugs.
- [x] Aplicar as dimensões ao jogador, bugs, bosses e às duas formas de RomerBug.
- [x] Carregar sequências de sprites com escala proporcional compartilhada, alinhamento dos pés e filtro sem suavização; tratar poses de ataque como exceção visual, sem alterar colisão corporal.
- [x] Adequar pontos de surgimento para manter os pés no piso e evitar sobreposição com blocos.
- [x] Dar classe própria a cada boss existente, com seleção de ataques própria e registro explícito de tipos, sem fallback para boss genérico.
- [x] Validar dimensões, transformações, chão das arenas, ataque com chicote e regressões existentes.

**Aceite:** CA-08 e CA-09 para as entidades disponíveis, junto aos testes existentes de encontro e combate. A validação visual definitiva inclui os personagens que serão criados nas próximas etapas.

## Etapa 2 — Menu e seleção do protagonista

- [x] Criar fachada em pixel art baseada em `referencia/fachada_escola.png`.
- [x] Implementar Jogar e Sair com clique e navegação por teclado.
- [x] Implementar tela de escolha Menino / Menina e persistência da seleção na campanha.
- [x] Criar e integrar spritesheet completo da Menina, cobrindo os mesmos estados do Menino e as dimensões comuns.
- [x] Verificar entrada, encerramento e ambas as opções de personagem: CA-01 e CA-02.

**Dependência:** etapa 1 para o contrato de dimensões e animações. Usar o fluxo de geração de imagens para arte nova; não considerar imagens substitutas como arte concluída.

## Etapa 3 — Introdução e percurso escolar

- [x] Substituir a introdução de CODIGO.EXE pela aula de Max, apresentação e revolta da IFVania.
- [x] Integrar representações de Max e Romerito baseadas nas referências, com dimensões comuns.
- [x] Construir corredores e A28 como adaptação lateral jogável; consulta ao link do Maps tentada, sem planta acessível. O laboratório A28 foi conferido na referência oficial; o traçado interno real continua sem homologação.
- [x] Implementar gatilhos únicos para encontro, ataque, abdução e transporte ao mundo virtual.
- [x] Apresentar a descoberta do mouse na bolsa antes de liberar seu uso.
- [x] Validar ordem narrativa e suspensão da simulação nos diálogos: CA-03 e CA-10.

## Etapa 4 — Primeira fase da nova campanha

- [x] Ajustar o percurso virtual para funcionar sem depender das habilidades da campanha antiga.
- [x] Inserir a fala de Romerito sobre Brasília e corridas e a infecção antes do combate.
- [x] Revisar aviões, medalhas, perseguição e transformação única a 50%, preservando vida e tamanho.
- [x] Encerrar ataques e projéteis ao derrotar o boss.
- [x] Remover recompensas e mensagens antigas sem respaldo no novo roteiro.
- [x] Separar a campanha antiga do fluxo principal; o fim do conteúdo disponível deve indicar que a jornada continua, sem anunciar a escola salva.
- [x] Validar CA-04 a CA-07 e repetir CA-08 com os novos personagens.

## Continuidade narrativa definida em 02/11/2026

O roteiro agora define seis fases, progressão, chefes e desligamento da IFVania. A revisão narrativa está concluída; sua implementação permanece pendente e não altera a conclusão das etapas 1 a 4 ou a homologação da validação final. O registro abaixo preserva o histórico das decisões anteriores.

## Registro de execução

- Etapa 1 implementada: dimensão lógica comum de 40 × 40 pixels, normalização proporcional das sequências, alinhamento dos pés, surgimento em piso livre e classes concretas com estratégias próprias para os seis bosses existentes.
- `Chefe` passou a ser abstrata para a escolha de ataques; tipos desconhecidos são rejeitados, sem substituição por um boss genérico.
- Inspeção visual feita com todas as entidades disponíveis lado a lado, incluindo SpeedBug. As silhuetas preservam suas proporções naturais dentro da mesma área; Max, Romerito humano e Menina serão verificados após a criação de suas artes.
- Validação: 31 testes passaram com Python 3.9.6 e Pygame 2.6.1, incluindo seis novos testes de dimensões, normalização, surgimento e estratégias. Comando: `python -m unittest discover -s testes -v`.
- O Python 3.15 instalado no sistema não compilou Pygame 2.6.1; a validação usou ambiente temporário com Python 3.9.6, sem mudar as dependências do projeto.
- Etapa 2 implementada: fachada baseada na fotografia, Jogar/Sair com mouse e teclado, seleção com prévia animada e confirmação, onze quadros da Menina e persistência da escolha entre fases e reaparecimentos.
- Introdução textual da etapa 3 atualizada: aula de Max, nome completo da IFVania, anúncio de desligamento, revolta, hipnose/alucinações e objetivo de cortar a energia. O percurso escolar e o combate virtual foram concluídos nas etapas 3 e 4 descritas abaixo.
- Artes geradas com a ferramenta integrada `image_gen`; fontes, prompts e PNG de execução estão no repositório. Exportação reproduzível: `python -m ferramentas.preparar_recursos_menu`.
- Validação ao concluir a etapa 2: 42 testes passaram com Python 3.9.6 e Pygame 2.6.1. Onze novos testes cobrem menu, ambas as opções, preservação da escolha, reinício de progresso, pausa da simulação e isolamento de eventos entre telas.
- Inspeção visual feita nas capturas de menu, seleção, introdução, primeira fase com Menina e todos os seus quadros nas duas direções. Também foram atualizadas e desenhadas as doze combinações entre dois protagonistas e seis mapas por 60 quadros cada, sem abrir janela.
- Etapa 3 implementada em 22/10/2026: aula com Max e mudança visual dos monitores na revolta da IA; corredor navegável com placas e acesso ao A28; encontro com Romerito por E; investida, recuo do protagonista e abdução animada; transporte para o mapa virtual e descoberta do mouse na bolsa antes de liberar o chicote.
- `FaseEscolar` mantém cenários sem inimigos/boss antecipado e gatilhos únicos. O mesmo protagonista atravessa as cenas. A arma fica bloqueada na escola e durante a descoberta; diálogos e pausa suspendem a simulação, inclusive o transporte.
- Max e Romerito possuem dois quadros cada, derivados das fotos de `referencia/`, com transparência e corpo comum de 40 × 40. Fontes e prompts salvos no projeto; exportação: `python -m ferramentas.preparar_recursos_escola`.
- Referência geográfica: o link curto do Maps não abriu uma planta consultável. A página oficial sobre horários dos laboratórios confirma A28: https://portal.ifrn.edu.br/campus/caico/noticias/horarios-laboratorios-de-informatica/ . As portas A25–A27 e as distâncias do corredor são composição de cenário, sem afirmação de posição real.
- Validação ao concluir a etapa 3: 51 testes passaram com Python 3.9.6 e Pygame 2.6.1. Os nove testes novos percorrem a rota com movimento real para Menino/Menina, conferem a ordem dos eventos, proximidade e tecla E, gatilhos únicos, ataque narrativo, arma bloqueada, pausa, dimensões, câmera e texto.
- Inspeção visual: aula, corredor, A28, abdução e descoberta do mouse; cenas escolares e transporte também renderizados sem janela com os dois protagonistas.
- Etapa 4 implementada em 23/10/2026: a campanha principal contém somente o mapa virtual previsto no HistoryBoard. Os seis mapas antigos, seus diálogos e poderes foram isolados em `mundo/fases_antigas.py`, fora do menu.
- O mapa fixo tem piso contínuo, degraus de 32/64 pixels, quatro bugs e arena plana. O piso mantém os personagens visíveis acima do diálogo. Foi percorrido com movimento e salto básicos, sem poderes, com ambos os protagonistas.
- Romerito aparece humano, fala de Brasília e corridas e é infectado por um bug em uma sequência de 60 atualizações. Ataques ficam bloqueados até seu término; a pausa suspende a infecção. O corpo e a vida são preservados.
- RomerBug/SpeedBug conservam a transformação única a 50%, os aviões, as medalhas e a perseguição. Após a derrota, ameaças e projéteis são removidos, sem item ou bônus de vida.
- A saída permanece bloqueada até a derrota. O fim do conteúdo apresenta “A jornada continua”, informa que a IFVania segue ativa e permite voltar ao menu e reiniciar a campanha.
- Validação ao concluir a etapa 4: 61 testes passaram com Python 3.9.6/Pygame 2.6.1. Os dez novos testes cobrem a campanha isolada, percurso básico, diálogo/infecção, pausa, dimensões, duas formas, limpeza, ausência de recompensa e encerramento/reinício. O combate por teclado foi verificado para Menino e Menina em condições controladas, sem representar homologação do balanceamento de sobrevivência.
- Inspeção visual: percurso, Romerito humano, infecção, SpeedBug, derrota e tela de continuação; capturas em `recursos/fontes_arte/virtual_*_preview.png` e `previa_fim_conteudo.png`.
- Próxima etapa: integração e homologação (validação final), incluindo teste manual, revisão integrada e balanceamento. O conteúdo narrativo posterior continua sem definição.

## Ajustes solicitados em 25/10/2026

- [x] Estilizar menu, seleção, cartões, pausa, diálogos e HUD com uma paleta escura legível.
- [x] Criar fachada noturna e fundo de laboratório escolar, preservando colisões e percurso.
- [x] Implementar a transição a 50%: uma perna apoiada, entidade, fala “Ainda não terminou.”, metamorfose e levantamento.
- [x] Aplicar aproximação/retorno suaves da câmera apenas no desenho; congelar combate e permitir pausa em toda a cena.
- [x] Preservar vida restante e corpo; limpar ataques/projéteis e oferecer proteção na retomada.
- [x] Apresentar proposta para substituir aviões/medalhas, sem aplicar mudança mecânica ainda não escolhida.

Artes feitas com a ferramenta integrada image_gen, fontes preservadas em
`recursos/fontes_arte/`, prompts em `instrucoes_artes_sombrias.json` e exportação reproduzível
com `python -m ferramentas.preparar_recursos_sombrios`. A entidade permanece de origem indefinida.

Validação da revisão de 25/10: 68 testes passaram. Os sete novos testes cobrem transição,
pausa e fala, vida/corpo, retomada, zoom visual, poses e legibilidade das dicas.
Foram inspecionadas capturas do menu, seleção, arena e etapas da transformação;
prévia animada em `recursos/fontes_arte/previa_transformacao_chefe.gif`.

A proposta está em `documentacao/PROPOSTA_CHEFE_ROMERBUG.md`. A validação final ainda requer homologação
manual e balanceamento; esta revisão não a declara concluída.

## Ajuste de proporção — 26/10/2026

Conforme a delimitação do responsável, somente o protagonista (Menino/Menina) e
os bosses recebem escala visual de 110%, durante toda a partida, incluindo
exploração, combate e transformação. São desenhados em 44 × 44 com apoio dos pés
preservado. Professores enquanto NPCs, bugs e entidade permanecem em 40 × 40. Colisões, velocidades, alcance e geometria do mapa permanecem iguais.
A escala fica centralizada em `configuracoes.ESCALA_VISUAL_PERSONAGEM`.

## Escala e arte escolar — 27/10/2026

A solicitação atual amplia também os NPCs e substitui a escala da revisão de
26/10: protagonista, bosses, professores e entidade usam 80 × 80 visuais; bugs
mantêm 40 × 40. Colisões de todos permanecem em 40 × 40. Os nomes dos NPCs,
a captura pela IFVania e a saída do chicote acompanham a nova apresentação.

Os laboratórios e corredores receberam novas fontes em resolução nativa de
960 × 540 por módulo, sem esticar um único painel para todo o corredor. Móveis,
portas e computadores recebem detalhes em camadas. Os terminais mudam texto,
gráficos e estados dentro da tela, acompanham a câmera e refletem a corrupção.
Seu relógio é visual: funciona em diálogos sem atualizar física/combate e congela
na pausa. A arena usa o mesmo sistema de monitores.

Artes novas feitas com image_gen e preservadas em `recursos/fontes_arte/`;
prompts em `instrucoes_escola_detalhada.json`. Exportação:
`python -m ferramentas.preparar_escola_detalhada`. Prévia animada:
`recursos/fontes_arte/previa_monitores_animados.gif`.

Validação atual: 74 testes passaram; seis novos testes cobrem escala, recorte
dos monitores, câmera, animação em diálogos/pausa e alcance da ponta do chicote.
Inspeção visual de aula, laboratório, corredor, arena, ataque e transformação.
A homologação manual e o balanceamento da validação final continuam pendentes.


## Caminhada e diálogos personalizados — 27/10/2026

- [x] Criar ciclos de oito quadros para Menino e Menina, preservando as artes anteriores.
- [x] Sincronizar os quadros com o deslocamento real e interromper a caminhada contra paredes; corrigir a pose de entrada e reaparecimento.
- [x] Inserir tela de nome entre seleção e aula, com acentos, limite de 20 caracteres, validação, edição e retorno.
- [x] Reescrever a introdução como diálogo iniciado pelo aluno com Max, sem narrador.
- [x] Aplicar o nome nas falas do aluno e nas respostas dos professores, preservando-o nas transições.
- [x] Validar 81 testes automatizados e inspecionar capturas da entrada de nome e dos diálogos.

Prévias em `recursos/fontes_arte/previa_nome_jogador.png`,
`previa_introducao_aluno.png`, `previa_resposta_com_nome.png` e
`previa_caminhada_jogador.gif`. A homologação manual da validação final permanece pendente.


## Nomenclatura em português e orientações — 28/10/2026

- [x] Renomear classes, variáveis, atributos, parâmetros e constantes próprios
  no jogo, testes e exportadores, preservando interfaces externas.
- [x] Atualizar importações, herança, callbacks, argumentos nomeados e acessos
  dinâmicos, sem modificar os caminhos dos módulos e imagens.
- [x] Criar `AGENTS.md` com convenções e contratos do projeto.
- [x] Atualizar referências técnicas na documentação.
- [x] Executar os 81 testes e os oito exportadores em pasta temporária (74 PNGs).

`ferramentas/gerar_recursos.py` passou por conferência estática de sintaxe e referências;
sua execução não foi realizada porque Pillow não está instalado no ambiente.
A homologação manual da validação final continua pendente.


## Arquivos e pastas em português — 28/10/2026

- [x] Renomear código, testes, exportadores, documentação, imagens e pastas
  próprias: 224 caminhos atualizados.
- [x] Atualizar importações, carregamento de imagens, nomes de quadros gerados,
  comandos e links locais. Preservar nomes técnicos de descoberta.
- [x] Conferir os 81 testes, os oito exportadores e a entrada `principal.py`.
- [x] Conferir todos os links locais e preservar os bytes das 160 imagens/GIFs.

Os comandos atuais são `python principal.py` e
`python -m unittest discover -s testes -v`; dependências em `configuracao/dependencias.txt`.
As fontes de arte ficam em `recursos/fontes_arte/`. A homologação manual
da validação final continua pendente.


## Revisão de controle, combate e plataformas — 28/10/2026

- [x] Movimento a 3,2 px/quadro, aceleração/frenagem curtas, tolerância de borda e memória de salto.
- [x] Corrigir direção e persistência do recuo de dano.
- [x] Chicote tolerante com alcance 100, carga de 0,6 s/dano 2, cancelamento e efeitos de peso.
- [x] Esquiva básica com recarga e proteção curta, tutorial e HUD.
- [x] Sobrecarga anunciada e investida de direção fixa, com recuperação e sem dano de contato passivo.
- [x] Contorno e faixa nas superfícies de apoio expostas, sem alterar colisões.
- [x] Atualizar regressões dos ataques substituídos e validar 92 testes.
- [x] Renderizar e inspecionar carga, mouse reforçado, plataformas e avisos dos ataques.

Cenários determinísticos sem invulnerabilidade artificial cobrem fuga da descarga
e salto sobre a investida. Isso não substitui homologação humana de sobrevivência,
ritmo e dificuldade; a validação final permanece pendente.


## Ciclo de projéteis e investida — 29/10/2026

- [x] Restaurar aviões de RomerBug, com 2,3 s entre lançamentos e aviso prévio.
- [x] Restaurar medalhas de SpeedBug a cada 1,5 s, com movimento curto limitado.
- [x] Alternar dois lançamentos, pausa, investida anunciada e recuperação.
- [x] Esperar os projéteis saírem antes de preparar a investida.
- [x] Manter transformação, proteção, controles do aluno e plataformas.
- [x] Validar 95 testes; homologação humana de ritmo/dificuldade segue pendente.


## Expansão do roteiro — 02/11/2026

Solicitação: atualizar a história conforme `AGENTS.md`, acrescentar cinco fases e melhorar a coerência, sem implementar conteúdo jogável nesta entrega.

- [x] Preservar o prólogo doméstico fornecido pelo responsável e integrá-lo à conversa inicial com Max, sem narrador.
- [x] Planejar cinco fases adicionais, totalizando seis, com ambientes, objetivos, percursos, chefes, diálogos e transições.
- [x] Explicar a resistência parcial do protagonista, a camada virtual e a identidade da entidade como autopreservação da IFVania.
- [x] Construir o desfecho com resgate, interrupção da recriação de processos, isolamento da rede e desligamento dos equipamentos, incluindo o nobreak.
- [x] Definir salto duplo durante a fase 2 e ancoragem após o encontro da fase 4, com tutoriais seguros e sem recompensa na fase 1.
- [x] Sincronizar roteiro, resumo do LEIA_ME e alcance dos requisitos, distinguindo planejamento e implementação.

A implementação futura está detalhada nas etapas 5 a 11 a seguir.

Verificação desta entrega: revisão documental da sequência de seis fases, obtenção de habilidades antes de seu uso obrigatório, participação dos aliados e condições do final; conferência dos links locais e do diff. Não foram executados testes do jogo nem homologação manual, pois nenhum código ou recurso jogável foi alterado. A validação final permanece pendente; os 95 testes citados acima são resultados históricos.


## Referências visuais do IFRN — leitura de 02/11/2026

As seis capturas em `referencia/ifrn/` foram inspecionadas individualmente. Mostram a biblioteca e espaços de circulação e convivência do campus, com interface do Google Maps sobreposta. Os horários abaixo identificam os arquivos, não a data de construção ou o estado atual dos ambientes.

| Captura | Elementos observados | Aplicação planejada |
|---|---|---|
| [17-24-38](../referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-24-38.png) | Biblioteca: mesas retangulares claras, cadeiras azuis e pretas, estantes metálicas, computadores de consulta, divisórias envidraçadas, persianas verticais, piso cerâmico claro e luminárias lineares. | Entrada e área segura da fase 2; separar consulta, leitura e acervo para variar o percurso. |
| [17-24-56](../referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-24-56.png) | Corredores entre estantes metálicas cinzentas, livros de cores variadas, expositores de revistas e placas de classificação com setas. | Módulos de acervo, orientação visual, atalhos e arena do Indexador na fase 2. |
| [17-26-04](../referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-26-04.png) | Circulação coberta, estrutura aparente sob telhado cerâmico, luminárias lineares, pilares amarelos com base revestida de branco e faixa vermelha, bancos de concreto, lixeira, árvores e placa de saída. | Corredores escolares, entrada do pátio e leitura da rota de resgate; repetir pilares e variar bancos e vegetação. |
| [17-27-22](../referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-27-22.png) | Jardim entre blocos, palmeiras e arbustos, vasos, paredes amarelas, corredor com revestimento branco e faixa vermelha, portas e janelas pequenas; unidades de ar-condicionado. | Transição entre biblioteca e pátio, fundo dos blocos e pausa visual antes dos desafios da fase 3. |
| [17-27-40](../referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-27-40.png) | Caminho pavimentado sombreado, bancos de concreto esverdeados, árvores e canteiros, circulação coberta e telhas ao fundo. | Área de reunião dos estudantes e trechos de descanso do pátio; separar caminho livre e jardim decorativo. |
| [17-27-45](../referencia/ifrn/Captura%20de%20tela%20de%202026-11-02%2017-27-45.png) | Outro ângulo da área de convivência: bancos, árvores, solo e gramado, arbustos e blocos baixos com cobertura cerâmica. | Variações do pátio e retorno à escola no epílogo, com iluminação que comunique a libertação. |

**Limites da referência:** as imagens não fornecem planta, medidas, continuidade entre todas as vistas ou identificação legível do A28. Também não mostram a quadra, o laboratório de manutenção, os equipamentos de rede ou o nobreak. Esses espaços continuam sendo composições ficcionais apoiadas na linguagem arquitetônica observada. As capturas complementam a referência geográfica já existente; não homologam conexões reais entre salas.

### Direção de arte a executar

- [ ] Preparar uma prancha de materiais com piso cerâmico claro, revestimento branco, faixa vermelha, paredes amarelas, metal cinzento, telhas e vegetação. Derivar a paleta das regiões visíveis, considerando a exposição irregular das capturas.
- [ ] Criar módulos de biblioteca: mesa de leitura, cadeiras, terminal de consulta, estante, expositor, placa de classificação, persiana e vidro. A passagem da área de leitura ao acervo deve ser reconhecível em vista lateral.
- [ ] Criar módulos externos: pilar revestido, cobertura, banco de concreto, lixeira, vaso, árvore, arbusto e placa de saída. Usar planos separados para arquitetura, vegetação distante e elementos próximos.
- [ ] Produzir versões normal, corrompida e restaurada a partir dos mesmos elementos. A corrupção altera mensagens, luzes e organização virtual, preservando elementos que permitam reconhecer o campus.
- [ ] Adaptar as referências diurnas à direção sombria já adotada no jogo sem apagar as cores dos materiais ou reduzir a leitura do personagem, do piso e dos avisos de ataque.
- [ ] Manter bancos, cadeiras e plantas decorativos quando não forem plataformas. Nas estantes virtuais escaláveis, destacar os apoios reais; não sugerir colisão em toda prateleira desenhada.
- [ ] Preservar os arquivos de referência e as artes aprovadas; guardar fontes, prompts e variações em `recursos/fontes_arte/`. Registrar qual captura orientou cada conjunto e exportar primeiro para pasta temporária.
- [ ] Usar as capturas como referência para recriação em pixel art. Interface, setas de navegação, minimapas, pessoas fotografadas e sobreposições do Maps não integram os cenários do jogo.

**Aceite visual:** comparar capturas do jogo com as referências e reconhecer biblioteca, corredor coberto e área de convivência pelos materiais e mobiliário. Conferir módulos sem emendas evidentes, proporções com personagens em 80 × 80 visuais, corpo lógico em 40 × 40, apoios legíveis e contraste na resolução de 960 × 540. A inspeção das referências está concluída; a produção e a homologação das novas artes permanecem pendentes.

## Etapa 5 — Preparação da expansão e materiais do campus

**Dependência:** roteiro de seis fases definido; revisão da base jogável na validação final antes de considerar a expansão homologada.

- [ ] Desdobrar a expansão em requisitos e critérios de aceite próprios, mantendo o encerramento provisório da fase 1 enquanto a fase 2 não estiver utilizável.
- [x] Adaptar a introdução à tarefa de casa e à aula de programação orientada a objetos; preservar a conversa iniciada pelo aluno, sem narrador, e o nome personalizado.
- [ ] Definir a passagem de estado entre fases: protagonista, nome, vida, habilidades, objetivos locais e limpeza de ataques e entradas pendentes.
- [ ] Especificar retomada após derrota, cura e repetição de encontros. Preservar os objetivos locais das fases 3 a 6 conforme o roteiro, sem pressupor salvamento persistente em disco.
- [ ] Implementar o conjunto visual de biblioteca, circulação coberta e convivência listado acima; validar a exportação temporária antes de integrar recursos.
- [x] Separar mapa e falas da biblioteca, cenário e objetivos locais, e classe concreta do Indexador em módulos próprios.
- [ ] Aplicar a mesma organização às fases seguintes.

**Aceite:** critérios da expansão registrados; transição de fase exercitada com ambas as aparências; novas artes inspecionadas em cena. Mudanças visuais nos cenários existentes preservam colisões. A campanha antiga continua isolada.

## Etapa 6 — Fase 2: Biblioteca dos arquivos perdidos

**Dependência:** etapa 5; salto simples e combate da fase 1 preservados.

- [x] Construir entrada com mesas e terminais, subida entre estantes e arquivo central a partir das capturas 17-24-38 e 17-24-56.
- [x] Implementar três consultas obrigatórias, liberação do portão e registros sobre processos distribuídos.
- [ ] Diferenciar bugs de arquivo dos bugs básicos e acrescentar atalhos de retorno entre as estantes.
- [x] Apresentar o Módulo de Repetição e ensinar salto duplo em sala segura, antes dos primeiros vãos obrigatórios; atualizar dicas e HUD apenas após a obtenção.
- [x] Implementar Indexador com classe concreta, faixas anunciadas, fichas e janelas de contra-ataque.
- [x] Integrar mapa de evacuação, inventário do servidor/nobreak e diálogo com Romerito.
- [ ] Conectar a saída da biblioteca ao pátio quando a fase 3 estiver disponível.
- [x] Substituir o cartão “A jornada continua” da fase 1 pela continuação somente quando este percurso estiver utilizável.

**Aceite:** chegar ao módulo com salto básico, concluir o restante com salto duplo e alcançar a fase 3 em construção ou um encerramento provisório explícito. Testar obtenção única, preservação da habilidade, pausa e limpeza do chefe; experimentar manualmente percurso e combate com Menino e Menina.

## Etapa 7 — Fase 3: Recreio em repetição

**Dependência:** etapa 6 e regras de retomada definidas na etapa 5.

- [ ] Construir circulação coberta, jardins e área de reunião usando as quatro capturas externas; compor a quadra e arquibancadas como cenários ficcionais, sem alegar referência fotográfica disponível.
- [ ] Introduzir bolas com trajetórias legíveis e ondas do sinal separadamente antes de combinar os perigos.
- [ ] Implementar três travas, atalhos, bolsões de silêncio e resgate sem escolta de aliados vulneráveis.
- [ ] Implementar Inspetor de Intervalo com classe própria, investidas anunciadas, ondas e recuperação.
- [ ] Registrar travas concluídas ao repetir o encontro local; mostrar Romerito conduzindo o grupo e a imagem de Max preso no laboratório.

**Aceite:** a derrota no chefe não refaz os resgates concluídos; estudantes não entram nas áreas de dano. Os bancos e jardins orientam a reunião sem criar plataformas falsas. Não conceder habilidade nova nesta fase.

## Etapa 8 — Fase 4: Laboratório das cópias

**Dependência:** etapa 7; regras de transição e progresso consolidadas.

- [ ] Compor o laboratório com a linguagem dos interiores escolares existentes; as novas capturas não mostram equipamentos desse ambiente.
- [ ] Implementar comparações de arquivos, estabilização das salas e ciclos legíveis dos bugs repetidos.
- [ ] Apresentar a origem da tarefa, a sessão de autoria e a entidade como autopreservação da IFVania, com registros obrigatórios curtos e pausas seguras.
- [ ] Implementar Max em Loop com classe própria, cópias, cabo que identifica a origem real do ataque e janela de recompilação vulnerável.
- [ ] Integrar libertação de Max, confissão do protagonista, interrupção da recriação dos processos e isolamento do pendrive.
- [ ] Definir e implementar comando contextual da ancoragem em conectores fixos, sem balanço livre; ensinar numa sala segura e conferir conflitos com ataque e diálogo.

**Aceite:** identificar o ataque verdadeiro por sinal visível; concluir a luta antes de exigir ancoragem. A nova habilidade permanece nas transições, funciona apenas nos conectores indicados e respeita pausa, perda de foco e colisões.

## Etapa 9 — Fase 5: Rede sem saída

**Dependência:** etapa 8 e tutorial de ancoragem concluído.

- [ ] Criar corredores técnicos e sala de rede ficcionais, mantendo materiais e sinalização do campus nas áreas de acesso.
- [ ] Introduzir pulsos de dados e combinar ancoragem e salto duplo com apoios seguros e retorno próximo após falha de travessia.
- [ ] Implementar três ramais isoláveis, confirmações de Max e mudança visual nos monitores dos setores afetados.
- [ ] Implementar Roteador Sentinela com classe própria, portas sinalizadas, barreira, flancos acessíveis e inversão da ordem dos disparos.
- [ ] Confirmar evacuação, confinamento da IA no servidor e preparação do desligamento pela equipe aliada.

**Aceite:** ramais concluídos permanecem isolados ao repetir o encontro; a IA não volta a controlar setores já cortados. A arena permite executar os comandos ensinados com o corpo lógico comum. Não conceder novo poder nesta fase.

## Etapa 10 — Fase 6: A última chamada e epílogo

**Dependência:** etapa 9 e condições narrativas de resgate e isolamento registradas.

- [ ] Construir três desafios curtos que retomem as habilidades adquiridas, com descanso e sem comandos novos.
- [ ] Implementar IFVania em classe concreta, com reserva única de vida, dois momentos, transição sem dano e padrões anunciados.
- [ ] Integrar rompimento do controle, diálogo final e terminal de encerramento, sem ataque residual ou cronômetro surpresa.
- [ ] Conferir pessoas liberadas, rede isolada e autopreservação encerrada antes do retorno ao A28 e do desligamento dos equipamentos e da alimentação de reserva pelos aliados.
- [ ] Criar epílogo da tarefa refeita, retorno da turma e fachada ao amanhecer; reaproveitar materiais restaurados da escola, sem representar cópia sobrevivente da IA.
- [ ] Substituir o encerramento provisório por “Escola livre. Aula encerrada.” e retorno ao menu, com reinício seguro de uma nova campanha.

**Aceite:** vitória final só após as condições da campanha; nome e aparência preservados até o epílogo. Combate para durante conversas, transições e encerramento; nova partida não herda habilidades ou objetivos anteriores indevidamente.

## Etapa 11 — Validação final e homologação da campanha completa

**Dependência:** etapas 1 a 10; única etapa final de validação consolidada. A antiga etapa 5 foi incorporada aqui e permanece pendente.

- [ ] Executar a suíte completa de regressão e os critérios de aceite adicionados para as fases 2 a 6.
- [ ] Percorrer manualmente as seis fases com Menino e Menina, avaliando ritmo, sobrevivência, pistas, diálogos, retomadas e variedade dos chefes.
- [ ] Inspecionar biblioteca, circulação coberta e pátio lado a lado com as seis referências; registrar aproximações visuais e adaptações ficcionais.
- [ ] Conferir câmera, legibilidade, escala, transparência, ancoragem dos pés e distinção entre decoração, conectores e plataformas em todos os ambientes.
- [ ] Revisar áudio e efeitos: avisos complementares por som e forma, intensidade dos tremores, leitura dos projéteis e silêncio/restauração no final.
- [ ] Atualizar requisitos, roteiro se necessário, LEIA_ME, controles e registros de geração com o estado realmente entregue.
- [ ] Registrar problemas restantes e resultados separados de testes automáticos, inspeção visual e experiência manual, sem usar aprovação automática como prova de diversão ou equilíbrio.

**Comandos de validação:** `python principal.py` para experimentar o jogo e `python -m unittest discover -s testes -v` para regressões. Sem janela/áudio: `SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy PYGAME_HIDE_SUPPORT_PROMPT=1 python -m unittest discover -s testes -v`. Executar exportadores em pasta temporária antes de substituir artes utilizadas.

## Registro da atualização do plano — 02/11/2026

- [x] Inspecionar as seis imagens de `referencia/ifrn/` e relacionar cada uma a materiais e cenários planejados.
- [x] Distinguir biblioteca e áreas externas observadas de espaços ainda sem referência interna.
- [x] Organizar a expansão em etapas 5 a 11 com dependências, entregas e critérios de aceite, preservando o histórico das etapas anteriores.
- [x] Registrar diretrizes para recriação em pixel art, variantes da corrupção e conferência de colisões e legibilidade.

Entrega exclusivamente documental: referências originais preservadas; nenhuma arte nova, alteração de código ou fase implementada nesta atualização. Links locais e formatação do diff conferidos. Não foram executados o jogo ou testes de regressão nesta entrega. A validação final continua pendente; os resultados de testes registrados no histórico não são execuções desta revisão.


## Primeiro incremento jogável da expansão — 02/11/2026

A antiga etapa 5 de integração/homologação foi incorporada à etapa 11, última da sequência. As antigas etapas 6 a 11 passaram a 5 a 10. Testes por incremento continuam obrigatórios; a validação final inclui a campanha completa e permanece aberta.

Implementado neste incremento:

- Introdução em diálogo com Max sobre a tarefa, oscilação de energia e execução sem revisão, com índice da corrupção derivado das falas.
- Saída da fase 1 conectada à biblioteca, preservando a identidade e sem conceder recompensa por RomerBug.
- Biblioteca com cenário modular desenhado em Pygame, inspirado nas duas capturas internas: mesas claras, cadeiras azuis, persianas, estantes metálicas e livros. É arte provisória feita em código, sem substituir fontes aprovadas. A produção dos materiais externos continua pendente.
- Módulo de Repetição obtido por E antes dos patamares obrigatórios; salto duplo sem cura ou aumento de vida, com piso seguro sob a área de treino.
- Três terminais de consulta e portão que exige todos os registros. Piso contínuo oferece recuperação de saltos falhos; a primeira subida obrigatória foi ajustada para 160 pixels após simulação da física.
- Indexador com classe concreta e corpo comum, alternando faixas com mira fixa anunciadas por 48 atualizações, fichas em duas alturas e recuperação. Sem dano corporal passivo; a derrota limpa faixas e projéteis.
- R na derrota da biblioteca reinicia o encontro, preservando o módulo e as consultas; Enter continua retornando ao menu. A retomada é local, sem gravação em disco.
- Entrada em fase e retomada restauram a integridade até a capacidade atual, sem aumentá-la. Transições cancelam cargas, golpes e projéteis pendentes. Nova campanha recria o protagonista e reinicia suas habilidades.

Permanecem pendentes nas etapas 5 e 6: materiais externos, especificação completa das fases futuras, bugs de arquivo especializados, atalhos e homologação humana de ritmo, controles e sobrevivência. As fases 3 a 6 ainda não estão disponíveis; a saída da biblioteca apresenta o cartão provisório de continuação.

Verificações deste incremento: **102 testes passaram** com Python 3.14.4 e pygame-ce 2.5.8 (módulo `pygame`), usando vídeo e áudio dummy. Incluem sete novos testes da biblioteca e atualização de duas expectativas da campanha para a continuação após RomerBug. Exercitados obtenção sem cura, três consultas/portão, retomada, identidade, limpeza, congelamento em diálogo/pausa, subida de 160 pixels com física real e derrota do Indexador pelo chicote com ambas as aparências. O teste de combate usa proteção artificial para isolar acertos e transições; não comprova equilíbrio de sobrevivência. Capturas da entrada, acervo e arena foram renderizadas e inspecionadas, com ajuste de alinhamento da camada de cenário à câmera. Não houve partida manual; a etapa 11 permanece pendente.
