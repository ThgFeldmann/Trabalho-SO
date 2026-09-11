Guia de Execução do Simulador de Escalonamento

    Antes de executar, verifique no arquivo a quantidade de processos desejada, encontrado na variável: 'n_processos', 
que possui o valor padrão de '3'.

    Ao executar o arquivo 'base.py', será feita a seguinte pergunta: "Será aleatório? ", espera-se um retorno em número, 
'1' para que todos os processos sejam aleatórios ou qualquer outro número para especificar os parâmetros de cada processo.
    A seguir serão criados os 'n' processos que serão utilizados no sistema, que serão retornados pelo terminal para a visualização dos valores.
    Com os processos criados o usuário será direcionado para o menu, onde poderá escolher qual critério de escalonamento utilizar com os processos.

    Ao selecionar o critério a ser utilizado, ele será executado imediatamente e irá retornar pelo terminal:
Uma linha do tempo da execução (Unidade de tempo atual, qual processo foi executado e quanto tempo resta para terminar), 
junto com o tempo de espera de cada processo, e a média do tempo de espera total.
    Terminando a execução do critério o usuário é retornado ao menu de seleção de critérios onde pode executar outro critério ou sair do sistema.