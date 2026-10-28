Guia de Execução do Simulador de Escalonamento

    Antes de executar, verifique no arquivo a quantidade de processos desejada, encontrado na variável: 'n_processos', 
que possui o valor padrão de '3' e o 'quantum' desejado, que possui o valor padrão de '2'.

    Ao executar o arquivo 'base.py', será feita a seguinte pergunta: "Será aleatório? S/N", espera-se um retorno de 'S' ou 'N', 
respectivamente 'sim' ou 'não' (também pode ser usados os valores de '1' e '0').
    A seguir serão criados os 'n' processos que serão utilizados no sistema, que serão retornados pelo terminal para a visualização dos valores.
Com os processos criados o usuário será direcionado para o menu, onde poderá escolher novamente qual critério de escalonamento utilizar com os processos.

    Ao selecionar o critério a ser utilizado, ele será executado imediatamente e irá retornar pelo terminal:
Uma linha do tempo da execução (Unidade de tempo atual, mostrando qual processo foi executado e quanto tempo resta para terminar), 
junto com o tempo de espera de cada processo, e a média do tempo de espera total.
    Terminando a execução do critério o usuário é retornado ao menu de seleção de critérios onde pode executar outro critério ou sair do sistema.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Funcionalidades disponíveis:

1: FCFS - First-Come-First-Served
    Executa os processos pela ordem de chegada, o primeiro processo a chegar será o primeiro a ser executado.

2: SJF preemptivo - Shortest-Job-First preemptivo
    Executa os processos que já chegaram e sempre o que tiver o menor tempo restante para terminar a execução, 
sendo preemptivo o escalonador pode encerrar a execução de um processo se um processo com menor tempo restante chegar.

3: SJF não-preemptivo - Shortest-Job-First não-preemptivo
    Executa os processos que já chegaram e sempre o que tiver o menor tempo restante para terminar a execução,
diferente do preemptivo este não encerra a execução de um processo, ele espera o término para poder selecionar o próximo 'menor' processo.

4: Prioridade preemptivo
    Executa os processos que já chegaram e sempre o que tiver a maior prioridade, em caso de empate executa o que chegou primeiro.
Em termos de funcionamento, age igual o SJF preemptivo isso é, se chegar um processo com maior prioridade ele pode tomar o lugar do processo que está em execução.

5: Prioridade não-preemptivo
    Executa os processos que já chegaram e sempre o que tiver a maior prioridade, em caso de empate executa o que chegou primeiro.
Em termos de funcionamento, age igual o SJF não-preemptivo isso é, um processo não pode ser interrompido quando está em execução.

6: Round-Robin
    Executa os processos que já chegaram enquanto respeita o 'quantum', isto é, por quantos ciclos um processo será executado por vez.
Os processos se 'rotacionam' em uma fila, o primeiro da fila é executado e ao final do quantum, retorna para o final da fila, isso é repetido até todos terminarem de executar.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Uso de IA

Inteligências Artificiais foram usadas para revisão de código escrito, sem interferir no código de forma direta, 
apenas com feedback sobre o funcionamento e possíveis erros que foram revisados e implementados pelo desenvolvedor com a sua própria visão.