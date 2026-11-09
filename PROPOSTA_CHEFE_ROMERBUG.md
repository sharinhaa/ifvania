# Ataques do primeiro chefe — RomerBug / SpeedBug

**Revisão:** 29/10/2026 — implementada conforme novo pedido do responsável.
A sobrecarga no piso foi retirada do encontro; aviões e medalhas retornam,
com ciclos legíveis de lançamento, pausa, investida e recuperação.

## RomerBug

Patrulha curta seguida de dois aviões. Cada lançamento tem 30 quadros de preparação
(0,5 s), com mira fixada no começo da preparação. Os lançamentos ficam separados
por 138 quadros (2,3 s): intervalo de 108 mais preparação de 30. Cada avião
avança a 4,5 pixels por quadro e não persegue mudanças de posição após lançado.

Depois do segundo avião, o professor faz uma pausa mínima de 48 quadros
(0,8 s), estendida até os projéteis anteriores saírem de cena. Prepara a
investida por 48 quadros, avança até 160 pixels a 6 pixels por quadro em direção
fixa e fica exposto por 60 quadros (1 s). Respeita paredes e limites da arena.

## SpeedBug

Usa o mesmo ciclo, com duas medalhas e deslocamento discreto: no máximo
0,55 pixel por quadro, limitado a 24 pixels para cada lado da posição inicial
do ciclo. Não há perseguição contínua ou salto reativo.

Cada lançamento tem preparação de 24 quadros (0,4 s). As medalhas são separadas
por 90 quadros (1,5 s): intervalo de 66 mais preparação de 24. A velocidade é
5 pixels por quadro, menor que os 6,5 da versão antiga. A mira também fica
fixada antes do disparo.

Depois das medalhas, pausa por pelo menos 48 quadros e espera a arena ficar
livre de projéteis. Prepara uma investida por 36 quadros (0,6 s), avança até
160 pixels sem corrigir a direção e recupera por 78 quadros (1,3 s).

## Leitura e justiça do encontro

Não há indicativos auxiliares dos ataques: sem textos, miras, setas ou sons
de aviso. A preparação e a recuperação continuam nos quadros do próprio
personagem, com os mesmos tempos e direção fixa. Projéteis causam
dano enquanto existem, mas nenhum permanece ao começar o período de preparação da investida.

O ciclo privilegia aprendizado do padrão, como solicitado na referência a
Mega Man X. Os parâmetros são iniciais; avaliação humana do ritmo continua pendente.

## Transição e validação

Mantidos a transformação única a 50%, joelho apoiado, entidade e fala, vida
compartilhada, pausa e proteção na retomada. Transformação e derrota limpam
projéteis e reiniciam o ciclo. Os controles do aluno e as plataformas destacadas
permanecem como na revisão anterior.

95 testes automatizados cobrem ciclos completos em ambas as formas, cadência,
mira fixa, movimento curto, pausa até expirar os projéteis, colisões, investida,
recuperação, transição e controles do aluno.
