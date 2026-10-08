"""
Sistemas Operacionais - IFRS Campus Restinga - ADS 3N - 2026/2
Trabalho de Desenvolvimento: simulador de algoritmos de escalonamento de processos.

TODO: Funcionalidades: Prioridade (preemptivo e não-preemptivo) e ROUND ROBIN
"""

# Importando a biblioteca do Python 'random' para a 
# geração aleatória de números
import random

# Cópia profunda da lista de processos, sem alterar os valores dos objetos
import copy

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
n_processos = 4

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
    aleatorio = input("Será aleatorio? S/N:  ").upper()

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

    print(f"Tempo médio de espera: {tempo_espera_total / n_processos:.2f}")

# Função do critério FCFS (First-Come-First-Served)
def FCFS(processos):
    lista_processos = copy.deepcopy(processos)
    
    # processo inicial no FIFO e o zero
    processo_em_execucao = 0 # Define qual processo vai ser executado | é utilizado como o id do processo

    for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
        print("tempo[" + str(ut) + "]: processo[" + str(lista_processos[processo_em_execucao].id) + "] restante=" +
                str(lista_processos[processo_em_execucao].t_restante))

        if lista_processos[processo_em_execucao].t_execucao == lista_processos[processo_em_execucao].t_restante:
            lista_processos[processo_em_execucao].t_espera = ut - 1

        if lista_processos[processo_em_execucao].t_restante == 1:
            if processo_em_execucao == (n_processos - 1):
                break
            else:
                processo_em_execucao += 1
        else:
            lista_processos[processo_em_execucao].t_restante = lista_processos[processo_em_execucao].t_restante - 1
    #

    imprime_stats(lista_processos)

# Função do critério SJF (Shortest-Job-First)
def SJF(preemptivo: bool, processos):
    lista_processos = copy.deepcopy(processos)
    
    # processo inicial no FIFO e o zero
    processo_em_execucao = 0 # Define qual processo vai ser executado | é utilizado como o id do processo
    
    novo_processo = None # Criando a variavel, sem uso neste momento
    
    if not preemptivo: # SJF não-preemptivo
        lista_chegada = []
        lista_ordenada = []
        processo_em_execucao = 0
        todos_terminaram = False
        tempo_execucao_maximo = 0
        processo_atual = None
        
        for processo in lista_processos:
            tempo_execucao_maximo += processo.t_execucao
        
        for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
            for processo in lista_processos: # Simulando a chegada dos processos ao longo do tempo
                if processo.t_chegada == ut and processo not in lista_chegada:
                    lista_chegada.append(processo)
            
            # Lista ordenada pelo menor tempo restante
            lista_ordenada = sorted(lista_chegada, key=lambda processo: processo.t_restante)
            
            if len(lista_ordenada) > 0 and processo_em_execucao < len(lista_ordenada): # Se tiver processos para executar
                if processo_atual == None and len(lista_ordenada) > 0: 
                    processo_atual = lista_ordenada[processo_em_execucao]
                    inicio = ut

                if processo_atual.t_restante > 0:
                    print("tempo[" + str(ut) + "]: processo[" + str(processo_atual.id) + "] restante=" +
                            str(processo_atual.t_restante))
                
                if processo_atual.t_restante == 1: # Última execução do processo
                    processo_atual.t_restante = 0

                    processo_atual.t_espera = inicio - processo_atual.t_chegada # Calculo do tempo de espera
                    if processo_atual.t_espera < 0: # Caso o tempo de espera seja negativo depois do calculo
                        processo_atual.t_espera = 0
                    
                    if todos_terminaram == True:
                        break
                    else:
                        terminados = 0
                        for processo in lista_processos:
                            if processo.t_restante == 0:
                                terminados +=1
                        
                        if terminados == len(lista_processos):
                            todos_terminaram = True
                        
                        processo_em_execucao += 1
                        
                        if processo_em_execucao < len(lista_ordenada):
                            processo_atual = lista_ordenada[processo_em_execucao]
                            inicio = ut+1
                        else:
                            break
                else: # Executando o processo
                    processo_atual.t_restante = processo_atual.t_restante - 1
            else:
                print(f"Tempo[{ut}]: CPU ociosa")

    else: # SJF preemptivo
        lista_chegada = []
        processo_em_execucao = 0
        todos_terminaram = False
        tempo_execucao_maximo = 0
        
        for processo in lista_processos:
            tempo_execucao_maximo += processo.t_execucao
        
        for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
            for processo in lista_processos:
                if processo.t_chegada == ut and processo not in lista_chegada:
                    lista_chegada.append(processo)
            
            if len(lista_chegada) > 0: # Se tiver processos para executar
                # Lista ordenada pelo menor tempo restante
                lista_ordenada = sorted(lista_chegada, key=lambda processo: processo.t_restante)
                
                if processo_em_execucao < len(lista_ordenada):
                    if lista_ordenada[processo_em_execucao].t_restante > 0:
                        print("tempo[" + str(ut) + "]: processo[" + str(lista_ordenada[processo_em_execucao].id) + "] restante=" +
                                str(lista_ordenada[processo_em_execucao].t_restante))
                    
                    if lista_ordenada[processo_em_execucao].t_restante == 1:
                        lista_ordenada[processo_em_execucao].t_restante = 0

                        if ut-1 != tempo_execucao_maximo:
                            lista_ordenada[processo_em_execucao].t_espera = ut+1 - lista_ordenada[processo_em_execucao].t_chegada - lista_ordenada[processo_em_execucao].t_execucao
                        else:
                            lista_ordenada[processo_em_execucao].t_espera = ut+1 - lista_ordenada[processo_em_execucao].t_chegada - lista_ordenada[processo_em_execucao].t_execucao
                        
                        
                        if lista_ordenada[processo_em_execucao].t_espera < 0:
                            lista_ordenada[processo_em_execucao].t_espera = 0
                        
                        if todos_terminaram == True:
                            break
                        else:
                            terminados = 0
                            for processo in lista_processos:
                                if processo.t_restante == 0:
                                    terminados +=1
                            
                            if terminados == len(lista_processos):
                                todos_terminaram = True
                            
                            processo_em_execucao += 1
                    else:
                        lista_ordenada[processo_em_execucao].t_restante = lista_ordenada[processo_em_execucao].t_restante - 1
            else:
                print(f"Tempo[{ut}]: CPU ociosa")

    imprime_stats(lista_processos)

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
