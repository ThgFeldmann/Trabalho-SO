"""
Sistemas Operacionais - IFRS Campus Restinga - ADS 3N - 2026/2
Trabalho de Desenvolvimento: simulador de algoritmos de escalonamento de processos.

TODO: Funcionalidades: SJF (preemptivo e não-preemptivo), Prioridade (preemptivo e não-preemptivo) e ROUND ROBIN
"""

# Importando a biblioteca do Python 'random' para a 
# geração aleatória de números
import random

class Processo:
    def __init__(self, id, t_execucao, t_chegada, t_espera=0, t_restante=0, prioridade=0):
        self.id = id
        self.t_execucao = t_execucao
        self.t_chegada = t_chegada
        self.t_espera = t_espera
        self.t_restante = t_restante
        self.prioridade = prioridade
    
    def Info(self):
        print(f"Processo[{self.id}]: tempo_execucao= {self.t_execucao} tempo_restante= {self.t_restante} tempo_chegada= {self.t_chegada} prioridade= {self.prioridade}")

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
            FCFS(processos)
            # FCFS(tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)

        elif alg == 2:  # SJF PREEMPTIVO
            # SJF(True, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)
            SJF(True, processos)

        elif alg == 3:  # SJF NAO PREEMPTIVO
            # SJF(False, tempo_execucao, tempo_espera, tempo_restante, tempo_chegada)
            SJF(False, processos)

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

# def executar_processos(processos):

# Função de criação de processos
# Escolha do usuário: gerar aleatórios ou manualmente
def popular_processos(processos):
    aleatorio = input("Sera aleatorio? S/N:  ").upper()

    for i in range(n_processos): # Repetindo até o número total de processos ser criado
        if aleatorio == "S" or aleatorio == "SIM" or aleatorio == "1": # Popular Processos Aleatorio
            processo = Processo( # Criando um processo aleatório | ordem: execução, chegada, prioridade
                id = i,
                t_execucao=random.randint(1, 10),
                t_chegada=random.randint(1, 10),
                prioridade=random.randint(1, 15),
            )
        else: # Popular Processos Manual
            tempo_execucao = int(input("Digite o tempo de execucao do processo[" + str(i) + "]:  "))
            tempo_chegada = int(input("Digite o tempo de chegada do processo[" + str(i) + "]:  "))
            prioridade = int(input("Digite a prioridade do processo[" + str(i) + "]:  "))
            processo = Processo(id=i, t_execucao=tempo_execucao, t_chegada=tempo_chegada, prioridade=prioridade)

        processo.t_restante = processo.t_execucao
        processo.t_espera = 0
        
        processos.append(processo)

# Retorna os processos existentes no terminal
def imprime_processos(processos):
    # Imprime lista de processos
    for processo in processos:
        processo.Info()

# Função que retorna no terminal os atributos do processo ao longo da execução
def imprime_stats(processos):
    tempo_espera_total = 0.0

    for processo in processos:
        print("Processo[" + str(processo.id) + "]: tempo_espera=" + str(processo.t_espera))
        tempo_espera_total += processo.t_espera

    print("Tempo medio de espera: " + str(tempo_espera_total / n_processos))

# Função do critério FCFS (First-Come-First-Served)
def FCFS(processos):
    # processo inicial no FIFO e o zero
    processo_em_execucao = 0 # Define qual processo vai ser executado | é utilizado como o id do processo

    for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
        print("tempo[" + str(ut) + "]: processo[" + str(processos[processo_em_execucao].id) + "] restante=" +
                str(processos[processo_em_execucao].t_restante))

        if processos[processo_em_execucao].t_execucao == processos[processo_em_execucao].t_restante:
            processos[processo_em_execucao].t_espera = ut - 1

        if processos[processo_em_execucao].t_restante == 1:
            if processo_em_execucao == (n_processos - 1):
                break
            else:
                processo_em_execucao += 1
        else:
            processos[processo_em_execucao].t_restante = processos[processo_em_execucao].t_restante - 1
    #

    imprime_stats(processos)

# def SJF(preemptivo, execucao, espera, restante, chegada):
#     tempo_execucao = list(execucao)
#     tempo_espera = list(espera)
#     tempo_restante = list(restante)
#     tempo_chegada = list(chegada)

#     # implementar codigo do SJF preemptivo e nao preemptivo
#     # ...
#     #

#     imprime_stats(tempo_espera)

# Função do critério SJF (Shortest-Job-First)
def SJF(preemptivo: bool, processos):
    # processo inicial no FIFO e o zero
    processo_em_execucao = 0 # Define qual processo vai ser executado | é utilizado como o id do processo

    # implementar codigo do SJF preemptivo e nao preemptivo
    for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
        if not preemptivo: # SJF não-preemptivo
            processos_ordenados = sorted(processos, key=lambda processo: (processo.t_restante)) # Ordenando os processos por tempo restante de execução
            # Executando o processo | Mesma lógica do FCFS
            if processos_ordenados[processo_em_execucao].t_execucao == processos_ordenados[processo_em_execucao].t_restante:
                processos_ordenados[processo_em_execucao].t_espera = ut - 1
    
            if processos_ordenados[processo_em_execucao].t_restante == 1:
                if processo_em_execucao == (n_processos - 1):
                    break
                else:
                    processo_em_execucao += 1
            else:
                processos_ordenados[processo_em_execucao].t_restante = processos_ordenados[processo_em_execucao].t_restante - 1

        # else: # SJF preemptivo

    imprime_stats(processos)


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
