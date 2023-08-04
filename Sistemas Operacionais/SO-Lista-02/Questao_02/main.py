import utilitarios
from processo import Processo
from Prioridade import Prioridades
from Sjf import Sjf
from os import system

menu = ["Shortest Job First", "Prioridades", "Sair"]
menu_prioridade_lista = ["Executar processos atuais", "Adicionar processo", "Visualizar processos", "Voltar"]

def menu_prioridade():
    global processos_base
    global menu_prioridade_lista
    escalonador = Prioridades(processos_base)
    while True:
        system("cls")
        resultado = utilitarios.menu("Você está em Escalonador por Prioridade, selecione sua ação", menu_prioridade_lista)
        
        if resultado == 1:
            var = escalonador.mostrador_sequencial()
            if var == 1:
                continue
            elif var == -1:
                break
        
        if resultado == 2:
            utilitarios.titulo_modlo("Adicione seu novo processo: ")
            nome = input("\nNome do processo: ")
            prioridade = utilitarios.verifica_int("\nDigite a prioridade de 0 a 20: ")
            CPUtotal = utilitarios.verifica_int("\nDigite a CPU total: ")
            ID = 0
            novo_processo = Processo(ID, nome, prioridade, CPUtotal)
            escalonador.add_processo(novo_processo)
            print("\033[0;32mProcesso adicionado\033[m")
            continue
        
        if resultado == 3:
            escalonador.mostrador()
            continue
        
        if resultado == 4:
            break
    return -1

def menu_sjf():
    global processos_base
    global menu_prioridade_lista
    escalonador = Sjf(processos_base)
    while True:
        system("cls")
        resultado = utilitarios.menu("Você está em Escalonador por Prioridade, selecione sua ação", menu_prioridade_lista)
        
        if resultado == 1: 
            var = escalonador.mostrador_sequencial()
            if var == 1:
                continue
            elif var == -1:
                break
        
        if resultado == 2:
            utilitarios.titulo_modlo("Adicione seu novo processo: ")
            nome = input("\nNome do processo: ")
            prioridade = utilitarios.verifica_int("\nDigite a prioridade de 0 a 20: ")
            CPUtotal = utilitarios.verifica_int("\nDigite a CPU total: ")
            ID = 0
            novo_processo = Processo(ID, nome, prioridade, CPUtotal)
            escalonador.add_processo(novo_processo)
            print("\033[0;32mProcesso adicionado\033[m")
            continue
        
        if resultado == 3:
            escalonador.mostrador()
            continue
        
        if resultado == 4:
            break
    return -1

while True:
    system("cls")
    p1 = Processo(1, "Calculadora", 3, 7)
    p2 = Processo(2, "Valorant", 7, 3)
    p3 = Processo(3, "TFT", 6, 5)
    processos_base = [p1, p2, p3]
    resultado = utilitarios.menu("Você está em um simulador de escalonadores escolha o seu modelo", menu)

    if resultado == 1:
        mprioridade = menu_sjf()
        if mprioridade == -1:
            continue
    
    elif resultado == 2:
        mprioridade = menu_prioridade()
        if mprioridade == -1:
            continue

    elif resultado == 3:
        break

utilitarios.titulo_modlo("\033[0;32mTamo junto adeus!!!!\033[m")
