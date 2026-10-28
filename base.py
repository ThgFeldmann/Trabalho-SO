"""
Sistemas Operacionais - IFRS Campus Restinga - ADS 3N - 2026/2
Trabalho de Desenvolvimento: simulador de algoritmos de escalonamento de processos.
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
n_processos = 3

# Quantum usado no Round-Robin, padrão é '2', alterar o valor irá afetar o resultado da função
quantum = 2

# Função principal, bloco principal de código
def main():
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
            PRIORIDADE(True, processos)

        elif alg == 5:  # PRIORIDADE NAO PREEMPTIVO
            PRIORIDADE(False, processos)

        elif alg == 6:  # Round_Robin
            Round_Robin(processos, quantum)

        elif alg == 7:  # IMPRIME CONTEUDO INICIAL DOS PROCESSOS
            imprime_processos(processos)

        elif alg == 8:  # REATRIBUI VALORES INICIAIS
            popular_processos(processos)
            imprime_processos(processos)

        elif alg == 9:  # Sair do programa (Parar a execução)
            break

# def executar_processos(processos):

# Função para verificar se todos os processos da lista foram concluídos
# Recebe uma lista de processos e retorna um booleano
def TodosProcessosForamConcluidos(lista_processos):
    concluidos = 0

    for processo in lista_processos:
        if processo.t_restante == 0:
            concluidos += 1
    
    if concluidos == len(lista_processos):
        return True
    else:
        return False

# Função que recebe uma lista de processos, retira processos já concluídos e retorna uma lista apenas com processos não concluídos
# Recebe: lista de processos e retorna uma lista de processos pendentes
def RemoverProcessosConcluidos(processos):
    lista_processos_pendentes = []
    
    for processo in processos:
        if processo.t_restante > 0:
            lista_processos_pendentes.append(processo)
    
    return lista_processos_pendentes

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
    
    if not preemptivo: # SJF não-preemptivo
        lista_chegada = []
        lista_ordenada = []
        processo_atual = None
        
        for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
            for processo in lista_processos: # Simulando a chegada dos processos ao longo do tempo
                if processo.t_chegada == ut and processo not in lista_chegada:
                    lista_chegada.append(processo)

            # Lista ordenada pelo tempo restante
            lista_ordenada = sorted(
                [processo for processo in lista_chegada if processo.t_restante > 0], # Ordenando apenas processos pendentes
                key=lambda processo: processo.t_restante
            )
            
            if processo_atual is None and len(lista_ordenada) > 0: # Se não tiver um processo executando
                processo_atual = lista_ordenada[0] # Seleciona o próximo processo da fila
                inicio = ut # Marca o tempo de inicio do processo
            
            if processo_atual is not None: # Se tiver um processo para executar
                print("tempo[" + str(ut) + "]: processo[" + str(processo_atual.id) + "] restante=" +
                    str(processo_atual.t_restante))
                
                processo_atual.t_restante -= 1 # Executa o processo
                
                if processo_atual.t_restante <= 0: # Se o processo terminou neste ciclo
                    processo_atual.t_restante = 0
                    processo_atual.t_espera = inicio - processo_atual.t_chegada # Calculo do tempo de espera
                    
                    if processo_atual.t_espera < 0: # Caso o tempo de espera seja negativo depois do calculo
                        processo_atual.t_espera = 0
                    
                    processo_atual = None # Remove o processo do estado de 'Executando'
                    
                    # Verificando se todos os processos já terminaram
                    todos_terminaram = all(processo.t_restante == 0 for processo in lista_processos)
                    
                    if todos_terminaram: # Se todos terminaram, cancela a execução da função
                        break
            else: # Se não há um processo para executar no ciclo atual
                print(f"Tempo[{ut}]: CPU ociosa")

    else: # SJF preemptivo
        lista_chegada = []
        lista_ordenada = []
        processo_atual = None
        
        for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
            for processo in lista_processos: # Simulando a chegada dos processos ao longo do tempo
                if processo.t_chegada == ut and processo not in lista_chegada:
                    lista_chegada.append(processo)
        
            # Lista ordenada pelo menor tempo restante
            lista_ordenada = sorted(
                [processo for processo in lista_chegada if processo.t_restante > 0], # Ordenando apenas processos pendentes
                key=lambda processo: processo.t_restante
            )
            
            if len(lista_ordenada) > 0: # Se tiver processos ordenados para execução
                proximo_processo = lista_ordenada[0] # Selecionando o próximo processo na lista
                
                if processo_atual is None: # Se não há um processo executando
                    processo_atual = proximo_processo # O processo em execução será o próximo processo na lista
                    inicio = ut # Salvando o tempo de inicio do processo
                elif proximo_processo.t_restante < processo_atual.t_restante: # Se o próximo processo na lista for 'menor' que o atual em execução
                    processo_atual = proximo_processo # O processo em execução será o próximo processo na lista
                    inicio = ut # Salvando o tempo de inicio do processo
                
                if processo_atual is not None: # Se tiver um processo selecionado para execução
                    print("tempo[" + str(ut) + "]: processo[" + str(processo_atual.id) + "] restante=" +
                        str(processo_atual.t_restante))
                    
                    processo_atual.t_restante -= 1 # Executa o processo
                    
                    if processo_atual.t_restante <= 0: # Se o processo terminou neste ciclo
                        processo_atual.t_restante = 0
                        processo_atual.t_espera = ut - (processo_atual.t_chegada+1) - processo_atual.t_execucao # Calculo do tempo de espera
                        
                        if processo_atual.t_espera < 0: # Caso o tempo de espera seja negativo depois do calculo
                            processo_atual.t_espera = 0
                        
                        processo_atual = None # Remove o processo do estado de 'Executando'
                        
                        # Verificando se todos os processos já terminaram
                        todos_terminaram = all(processo.t_restante == 0 for processo in lista_processos)
                        
                        if todos_terminaram: # Se todos terminaram, cancela a execução da função
                            break
            else: # Se não há um processo para executar no ciclo atual
                processo_atual = None
                print(f"Tempo[{ut}]: CPU ociosa")

    imprime_stats(lista_processos)

# Função do critério de Prioridade
def PRIORIDADE(preemptivo, processos):
    lista_processos = copy.deepcopy(processos)
    
    if not preemptivo: # Prioridade não-preemptivo
        lista_chegada = []
        lista_ordenada = []
        processo_atual = None
        
        for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
            for processo in lista_processos: # Simulando a chegada dos processos ao longo do tempo
                if processo.t_chegada == ut and processo not in lista_chegada:
                    lista_chegada.append(processo)

            # Lista ordenada pela prioridade
            lista_ordenada = sorted(
                [processo for processo in lista_chegada if processo.t_restante > 0], # Ordenando apenas processos pendentes
                key=lambda processo: processo.prioridade
            )
            
            if processo_atual is None and len(lista_ordenada) > 0: # Se não tiver um processo executando
                processo_atual = lista_ordenada[0] # Seleciona o próximo processo da fila
                inicio = ut # Marca o tempo de inicio do processo
            
            if processo_atual is not None: # Se tiver um processo para executar
                print("tempo[" + str(ut) + "]: processo[" + str(processo_atual.id) + "] restante=" +
                    str(processo_atual.t_restante))
                
                processo_atual.t_restante -= 1 # Executa o processo
                
                if processo_atual.t_restante <= 0: # Se o processo terminou neste ciclo
                    processo_atual.t_restante = 0
                    processo_atual.t_espera = inicio - processo_atual.t_chegada # Calculo do tempo de espera
                    
                    if processo_atual.t_espera < 0: # Caso o tempo de espera seja negativo depois do calculo
                        processo_atual.t_espera = 0
                    
                    processo_atual = None # Remove o processo do estado de 'Executando'
                    
                    # Verificando se todos os processos já terminaram
                    todos_terminaram = all(processo.t_restante == 0 for processo in lista_processos)
                    
                    if todos_terminaram: # Se todos terminaram, cancela a execução da função
                        break
            else: # Se não há um processo para executar no ciclo atual
                print(f"Tempo[{ut}]: CPU ociosa")

    else: # Prioridade preemptivo
        lista_chegada = []
        lista_ordenada = []
        processo_atual = None
        
        for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
            for processo in lista_processos: # Simulando a chegada dos processos ao longo do tempo
                if processo.t_chegada == ut and processo not in lista_chegada:
                    lista_chegada.append(processo)
        
            # Lista ordenada pela prioridade
            lista_ordenada = sorted(
                [processo for processo in lista_chegada if processo.t_restante > 0], # Ordenando apenas processos pendentes
                key=lambda processo: -processo.prioridade # Ordenando pela maior prioridade
            )
            
            if len(lista_ordenada) > 0: # Se tiver processos ordenados para execução
                processo_atual = lista_ordenada[0] # Selecionando o processo com a maior prioridade na lista
                
                print("tempo[" + str(ut) + "]: processo[" + str(processo_atual.id) + "] restante=" +
                    str(processo_atual.t_restante))
                
                processo_atual.t_restante -= 1 # Executa o processo
                
                if processo_atual.t_restante <= 0: # Se o processo terminou neste ciclo
                    processo_atual.t_restante = 0
                    processo_atual.t_espera = ut - (processo_atual.t_chegada+1) - processo_atual.t_execucao # Calculo do tempo de espera
                    
                    if processo_atual.t_espera < 0: # Caso o tempo de espera seja negativo depois do calculo
                        processo_atual.t_espera = 0
                    
                    processo_atual = None # Remove o processo do estado de 'Executando'
                    
                    # Verificando se todos os processos já terminaram
                    todos_terminaram = all(processo.t_restante == 0 for processo in lista_processos)
                    
                    if todos_terminaram: # Se todos terminaram, cancela a execução da função
                        break
            else: # Se não há um processo para executar no ciclo atual
                processo_atual = None
                print(f"Tempo[{ut}]: CPU ociosa")

    imprime_stats(lista_processos)


def Round_Robin(processos, quantum):
    lista_processos = copy.deepcopy(processos) # Copiando a lista de processos sem prejudicá-la
    fila_processos = [] # Fila de processos que 'rotaciona' ao longo do Round-Robin | Não é usado a 'lista_chegada' pois a execução não é linear
    processo_atual = None # Processo que está em execução, começa em 'None'
    quantum_restante = 0 # O quatum será verificado durante a execução do processo

    for ut in range(1, MAXIMO_TEMPO_EXECUCAO):
        #* Simulando a chegada dos processos ao longo do tempo
        for processo in lista_processos:
            if processo.t_chegada == ut and processo not in fila_processos:
                fila_processos.append(processo)
        
        #* Contando o tempo de espera dos processos, exceto do atual processo em execução
        if len(fila_processos) > 0: # Se tiver processos na fila para executar
            for processo in fila_processos: # Atualizando o tempo de espera dos processos da fila que não estão em execução
                if processo is not processo_atual:
                    processo.t_espera += 1
        
        #* Se não tiver um processo para executar | Seleciona um novo e reinicia o quantum
        if processo_atual is None and len(fila_processos) > 0: # Se não tiver um processo em execução E há processos para executar na fila
            processo_atual = fila_processos.pop(0) # 'Remove' um processo da fila para executá-lo
            quantum_restante = quantum # Marca o quantum para a execução do processo atual
        
        #* Se tiver um processo para executar, execute-o
        if processo_atual is not None: # Se tiver um processo para executar neste ciclo
            print("tempo[" + str(ut) + "]: processo[" + str(processo_atual.id) + "] restante=" +
                str(processo_atual.t_restante))
            
            processo_atual.t_restante -= 1 # Executa o processo
            quantum_restante -= 1 # Reduz o quantum

            if processo_atual.t_restante <= 0: # Se o processo terminou de executar
                processo_atual.t_restante = 0
                processo_atual = None # Removendo o processo da execução
                quantum_restante = 0 # O quatum acabou
                
                # Verificando se todos os processos já terminaram
                todos_terminaram = all(processo.t_restante == 0 for processo in lista_processos)
                
                if todos_terminaram: # Se todos terminaram, cancela a execução da função
                    break
        
        #* Se o quatum terminou porém o processo atual não terminou
        if quantum_restante == 0 and processo_atual is not None: # Se o quantum terminou
            fila_processos.append(processo_atual) # O processo atual volta para a fila de processos com as informações atuais
            processo_atual = None # Removendo o processo da execução
        
        else: # Se não há um processo para executar no ciclo atual
            print(f"Tempo[{ut}]: CPU ociosa")


    imprime_stats(lista_processos)


main()
