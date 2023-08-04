# Tamanho da memoria em MB = x
# Memória Fixa
# Frist-fis, Wort-fit
import utilitarios
import menu
import memoria
import Algoritimos_CPU.FIFO as fifo
from random import choice
from os import system

mem = menu.menu_interativo()

def First_fit(mem):
    memoria_principal = memoria.Memoria(mem[0], mem[1])
    processador = fifo.FIFO()
    while True:
        
        resulti = utilitarios.menu("Esta em First_fit, oque deseja fazer?", ["Executar","Adicionar Item", "Verificar", "Voltar"])

        if resulti == 1:
            while True:
                
                fim = processador.cosumidor()
                if fim != 1 and fim != None:
                    if fim != 2 and fim != None:
                        memoria_principal.remove_processo(fim)
                        
                if fim == 2:
                    if processador.em_execucao.local_memoria == "Memoria_s":
                        memoria_principal.aloca_processo(processador.em_execucao, "First-fit")
                        memoria_principal.remove_secundaria(processador.em_execucao.ID)
                        processador.em_execucao.local_memoria = "Memoria_p"

                system("cls")
                processador.to_string()
                memoria_principal.to_string()
                result = input("Dijite 'p' para parar:").upper()
                if result == "P":
                    break
        elif resulti == 2:
            add_proc(processador, memoria_principal, "First-fit")
            
        elif resulti == 3:
            system("cls")
            processador.to_string()
            memoria_principal.to_string()
            input("Aperte Enter para para continuar! ")
            continue
        else:
            break
        
def Next_fit(mem):
    memoria_principal = memoria.Memoria(mem[0], mem[1])
    processador = fifo.FIFO()
    while True:
        
        resulti = utilitarios.menu("Esta em Next_fit, oque deseja fazer?", ["Executar","Adicionar Item", "Verificar", "Voltar"])

        if resulti == 1:
            while True:
                
                fim = processador.cosumidor()
                if fim != 1 and fim != None:
                    if fim != 2 and fim != None:
                        memoria_principal.remove_processo(fim)
                if fim == 2:
                    if processador.em_execucao.local_memoria == "Memoria_s":
                        memoria_principal.aloca_processo(processador.em_execucao, "Next-fit")
                        memoria_principal.remove_secundaria(processador.em_execucao.ID)
                        processador.em_execucao.local_memoria = "Memoria_p"

                system("cls")
                processador.to_string()
                memoria_principal.to_string()
                result = input("Digite 'p' para parar:").upper()
                if result == "P":
                    break
        elif resulti == 2:
            add_proc(processador, memoria_principal, "Next-fit")
            
            
        elif resulti == 3:
            system("cls")
            processador.to_string()
            memoria_principal.to_string()
            input("Aperte Enter para para continuar! ")
            continue
        else:
            break 

def add_proc(fifo, mem, tipo):
    nome = input("O nome do processo: ")
    cust = utilitarios.verifica_int("Custo de CPU do processo: ")
    tam = utilitarios.verifica_int("Tamanho da memoria do processo: ")
    fifo.add_proc(nome, cust, tam)
    while True:
        if mem.tamanho_livre() < tam:
            mem.swapping(choice(fifo.processos))
        else:
            break
            
    mem.aloca_processo(fifo.processos[-1], tipo)

while True:
    algoritimo = utilitarios.menu("Qual o algoritimo sera executado", ["First_fit", "Next_fit", "Sair"])

    if algoritimo == 1:
        First_fit(mem)
    
    elif algoritimo == 2:
        Next_fit(mem)
    
    else:
        break
    

utilitarios.titulo_modelo("Fim da apresentação")
