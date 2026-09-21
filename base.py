"""
Sistemas Operacionais - IFRS Campus Restinga - ADS 3N - 2026/2
Trabalho de Desenvolvimento: simulador de algoritmos de escalonamento de processos.

TODO: Funcionalidades: SJF (preemptivo e não-preemptivo), Prioridade (preemptivo e não-preemptivo) e ROUND ROBIN
"""

# Importando a biblioteca do Python 'random' para a 
# geração aleatória de números
import random

class Processo:
    def __init__(self, t_execucao, t_chegada, t_espera=0, t_restante=0, prioridade=0):
        self.t_execucao = t_execucao
        self.t_chegada = t_chegada
        self.t_espera = t_espera
        self.t_restante = t_restante
        self.prioridade = prioridade

# Tempo máximo que o progama pode ficar em execução
MAXIMO_TEMPO_EXECUCAO = 65535

# Quantidade de processos que vão ser criados e utilizados
n_processos = 3

# Função principal, bloco principal de código
def main():
    # Variáveis dos processos
    tempo_execucao = [0] * n_processos # Tempo de execução
    tempo_chegada = [0] * n_processos # Tempo de chegada
    prioridade = [0] * n_processos # Prioridade do processo (Não implementado)
    tempo_espera = [0] * n_processos # Tempo de espera
    tempo_restante = [0] * n_processos # Tempo restante de execução
    
    # Lista de processos
    processos = []

    # Executando a função que cria os processos, 
    # o usuário escolhe se gera processos aleatórios ou se cria manualmente cada um
    popular_processos(processos)
    # popular_processos(tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

    # Executa a função que retorna os processos diretamente no terminal
    imprime_processos(processos)
    # imprime_processos(tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

    # Escolher algoritmo
    while True:
        # Variável que pergunta ao usuário qual critério utilizar (ou sair do programa)
        # e armazena a escolha
        alg = int(input(
            "Escolha o algoritmo?: [1=FCFS 2=SJF Preemptivo 3=SJF Nao Preemptivo  "
            "4=Prioridade Preemptivo 5=Prioridade Nao Preemptivo  6=Round_Robin  "
            "7=Imprime lista de processos 8=Popular processos novamente 9=Sair]: "))

        # Verificações condicionais abaixo para determinar o critério a ser usado
        # baseado na escolha do usuário
        if alg == 1:  # FCFS
            FCFS(tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)

        elif alg == 2:  # SJF PREEMPTIVO
            SJF(True, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)

        elif alg == 3:  # SJF NAO PREEMPTIVO
            SJF(False, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)

        elif alg == 4:  # PRIORIDADE PREEMPTIVO
            PRIORIDADE(True, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

        elif alg == 5:  # PRIORIDADE NAO PREEMPTIVO
            PRIORIDADE(False, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

        elif alg == 6:  # Round_Robin
            Round_Robin(tempo_execucao, tempo_espera, tempo_restante)

        elif alg == 7:  # IMPRIME CONTEUDO INICIAL DOS PROCESSOS
            imprime_processos(tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

        elif alg == 8:  # REATRIBUI VALORES INICIAIS
            popular_processos(tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)
            imprime_processos(tempo_execucao, tempo_espera, tempo_restante, tempo_chegada, prioridade)

        elif alg == 9:  # Sair do programa (Parar a execução)
            break

# Função de criação de processos
# Escolha do usuário: gerar aleatórios ou manualmente
def popular_processos(processos):
    aleatorio = input("Sera aleatorio? S/N:  ").upper()

    for i in range(n_processos): # Repetindo até o número total de processos ser criado
        if aleatorio == "S" or aleatorio == "SIM" or aleatorio == "1": # Popular Processos Aleatorio
            processo = Processo( # Criando um processo aleatório | ordem: execução, chegada, prioridade
                t_execucao=random.randint(1, 10),
                t_chegada=random.randint(1, 10),
                prioridade=random.randint(1, 15),
            )
        else: # Popular Processos Manual
            tempo_execucao = int(input("Digite o tempo de execucao do processo[" + str(i) + "]:  "))
            tempo_chegada = int(input("Digite o tempo de chegada do processo[" + str(i) + "]:  "))
            prioridade = int(input("Digite a prioridade do processo[" + str(i) + "]:  "))
            processo = Processo(t_execucao=tempo_execucao, t_chegada=tempo_chegada, prioridade=prioridade)

        processo.t_restante = processo.t_execucao
        processo.t_espera = 0
        
        processos.append(processo)

# Retorna os processos existentes no terminal
def imprime_processos(processos):
    incremento = 0
    # Imprime lista de processos
    for processo in processos:
        print("Processo[" + str(incremento) + "]: tempo_execucao=" + str(processo.t_execucao) +
                " tempo_restante= " + str(processo.t_restante) +
                " tempo_chegada= " + str(processo.t_chegada) +
                " prioridade= " + str(processo.prioridade))
        incremento+=1

# Função que retorna no terminal os atributos do processo ao longo da execução
def imprime_stats(espera):
    tempo_espera = list(espera)
    # Implementar o calculo e impressao de estatisticas

    tempo_espera_total = 0.0

    for i in range(n_processos):
        print("Processo[" + str(i) + "]: tempo_espera=" + str(tempo_espera[i]))
        tempo_espera_total = tempo_espera_total + tempo_espera[i]

    print("Tempo medio de espera: " + str(tempo_espera_total / n_processos))

# Função do critério FCFS (First-Come-First-Served)
def FCFS(execucao, espera, restante, chegada):
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    # tempo_chegada = list(chegada)

    processo_em_execucao = 0  # processo inicial no FIFO e o zero

    for i in range(1, MAXIMO_TEMPO_EXECUCAO):
        print("tempo[" + str(i) + "]: processo[" + str(processo_em_execucao) + "] restante=" +
                str(tempo_restante[processo_em_execucao]))

        if tempo_execucao[processo_em_execucao] == tempo_restante[processo_em_execucao]:
            tempo_espera[processo_em_execucao] = i - 1

        if tempo_restante[processo_em_execucao] == 1:
            if processo_em_execucao == (n_processos - 1):
                break
            else:
                processo_em_execucao = processo_em_execucao + 1
        else:
            tempo_restante[processo_em_execucao] = tempo_restante[processo_em_execucao] - 1
    #

    imprime_stats(tempo_espera)


def SJF(preemptivo, execucao, espera, restante, chegada):
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    tempo_chegada = list(chegada)

    # implementar codigo do SJF preemptivo e nao preemptivo
    # ...
    #

    imprime_stats(tempo_espera)


def PRIORIDADE(preemptivo, execucao, espera, restante, chegada, prioridade):
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    tempo_chegada = list(chegada)
    prioridade_temp = list(prioridade)

    # implementar codigo do Prioridade preemptivo e nao preemptivo
    # ...
    #

    imprime_stats(tempo_espera)


def Round_Robin(execucao, espera, restante):
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)

    # implementar codigo do Round-Robin
    # ...
    #

    imprime_stats(tempo_espera)


main()
