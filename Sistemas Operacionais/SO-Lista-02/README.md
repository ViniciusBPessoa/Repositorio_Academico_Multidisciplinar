# Lista 02 de Sistemas operacionais

- Questão 01 - Cinco threads concorrendo simultaneamente a dois recursos compartilhados (ex.: variáveis globais, buffers, etc.), as quais somente uma thread por vez pode acessar cada recurso compartilhado (pode utilizar qualquer técnica de exclusão mútua). Nesse caso, deve ser demonstrado (com logs, prints, graficamente, etc.) que as condições de corrida existem e que a exclusão mútua de fato ocorre. Como sugestão, considerar a permuta de uma thread para outra a cada 3 segundos (nesse intervalo, uma thread pode estar "consumindo" o recurso enquanto as demais aguardam, seja de forma bloqueada ou como espera ocupada), como no exemplo do produtor/consumidor (porém aqui com dois buffers).
 
- Questão 02 Um "mini" simulador (pode se basear nessa ferramenta: https://sourceforge.net/projects/oscsimulator/) de escalonamento preemptivo de processos, onde seja possível um usuário (não precisa de interface gráfica, pode ser linha de comando):

    Criar processos indicando: ID, Nome, prioridade, processo I/O bound ou CPU/bound, tempo de CPU total (ex.: em unidades inteiras de tempo, por exemplo, 1 a 10 ms). A cada criação, o processo deve ser inserido na fila de "pronto" para ser escalonado conforme algoritmo de escalonamento;
    Escolher uma de duas opções de algoritmo de escalonamento implementadas (se em dupla escolher uma por integrante);
    Selecionar o tempo de quantum da preempção (ex.: em unidades inteiras de tempo, por exemplo, 1 a 10 ms)
    Mostrar a lista de processos na fila de "prontos" dinamicamente (atualizar conforme escalonamento);
    Iniciar a execução e escalonamento de processos, mostrando (com logs, prints, graficamente, etc.) ao usuário qual processo está ativo na CPU (por quanto tempo), a preempção do processo e quais estão aguardando, indicando sempre a ordem de execução dos algoritmos.
    Ao final da execução, indicar o tempo de turnaround de cada processo e o tempo médio de espera de todos os processos.


# Questão 01:

- Todo o codigo esta disponivel em Questao_01
- Apenas nescessario executar o main.py para verificar a execução do processo.

## Como o codigo dunciona:

    O algoritimo simula a recepção e o atendimento de pessoas em algum estabelicimento, onde temos uma thread que adiciona o nome de pessoas em uma lista (espera_lista) de espera.
    Essas pessoas serão atendidas por uma das threads consumidoras (4 no total) que vão remover o nome que esta na posição 0 da lista, ficar um tempo piseldo aleatorio entre 1 e 5 segundos e depois inseri-lo na lista de atendidos (atendimento_lista), ou seja essa lista esta sendo acessada por 4 diferentes threads.

São ao todo 5 threads competindo por 2 recursos - sendo esses recursos 2 listas.
- lista espera_lista
- lista atendimento_lista 

# Questão 02:

 - todo o codigo esta disponivel em quesao_2

 ## Modelos celecionados:

 1. Prioridade
 2. SJF

 ## Prioridade:
 
    Levando em consideração 50% de Custo de CPU e 100% da prioridade para ordenar a entrada de processos.

## SJF (Shortest job first):

    O menor Custo de CPU vai primeiro e caso um novo processo chegue e contenha um costo menor que o em execução o que esta em execução deve ser substituido por ele e o mesmo deve ser realocado na fila.