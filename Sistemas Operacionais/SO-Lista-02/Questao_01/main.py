# 5 threads simultaneas x 2 recursos compartilhados
# duas listas (trate como recursos)
# lista 1 realizando algum processo com as informações da lista 2
# lista 2 recebendo dados

import threading
from random import choice, randint
import time

# Começa recurso 1 --------------------------------------------------------------------------------------------
def produtora(ID):  
    inicio = time.time()
    while True:                           
        global espera_lista
        global nomes
        global soninho
        global max_espera
        
        nome_atender = choice(nomes)
        
        semaforo.acquire()
        if len(espera_lista) < max_espera:
            espera_lista.append(nome_atender)
            print("")
            print(f"A \033[0;32mthread {ID}\033[m colocou \033[0;36m{nome_atender}\033[m na lista de espera")
            print(f"A lista de espera é {espera_lista}")
            
        semaforo.release()
        
        fim = time.time()
        
        if fim - inicio >= limite_tempo: break
# Termina recurso 1 -------------------------------------------------------------------------------------------

# Começa recurso 2 --------------------------------------------------------------------------------------------
def consumidora(ID): 
    while True:
        global max_exec
        global espera_lista
        global atendimento_lista
        
        nome_atendimento = ""
        
        semaforo.acquire()
        if len(espera_lista) > 0:
            nome_atendimento = espera_lista[0]
            espera_lista.pop(0)
            print(f"A \033[0;33mthread {ID}\033[m vai atender \033[0;36m{nome_atendimento}\033[m")
            semaforo.release()
        else: 
            time.sleep(randint(1, soninho))
            if len(espera_lista) == 0: 
                semaforo.release()
                break
        
        time.sleep(randint(1, soninho))
        
        if nome_atendimento != "":
            semaforo.acquire()
            atendimento_lista.append(nome_atendimento)
            print("")
            print(f"A \033[0;35mthread {ID}\033[m atendeu \033[0;36m{nome_atendimento}\033[m")
            print(f"A lista de espera é {espera_lista}")
            print(f"A lista de atendimento é {atendimento_lista}")
            
            semaforo.release()
# Termina recurso 2 -------------------------------------------------------------------------------------------

limite_tempo        = 15                                                        # Variável guardando tempo total de execução do código                                                       
semaforo            = threading.Semaphore()                                     # Instancia semáforo
soninho             = 3                                                         # Variável guardando tempo máximo de espera para a thread
max_espera          = 5                 
atendimento_lista   = []                                                        # Lista de pessoas atendidas
espera_lista        = []                                                        # Lista de pessoas em espera
threads             = []                                                        # Lista das threads          
nomes               = ["João", "Maria", "Pedro", "Ana",                         # Lista contendo o nome das pessoas
         "Lucas", "Mariana", "Gabriel", "Laura", "Rafael", "Carolina"]      

for c in range(1, 6):
    if c == 1: threads.append(threading.Thread(target=produtora, args=(c,)))
    else:      threads.append(threading.Thread(target=consumidora, args=(c,)))

for c in range(0, 5): threads[c].start()
for c in range(0, 5): threads[c].join()
    
print()
print("\033[0;32mO codigo encerrou\033[m")
