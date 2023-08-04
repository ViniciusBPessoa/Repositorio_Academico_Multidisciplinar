# Tamanho da memoria em MB = x
# Memória Fixa
# Frist-fis, Wort-fit
import utilitarios
import menu
import memoria
import Algoritimos_CPU.FIFO as fifo

mem = menu.menu_interativo()

def First_fit(mem):
    memoria_principal = memoria.Memoria(mem[0], mem[1])
    processador = fifo.FIFO()
    while True:
        
        resulti = utilitarios.menu("Esta em First_fit, oque deseja fazer?", ["Executar","Adicionar Item", "Verificar", "Voltar"])

        if resulti == 1:
            pass
        elif resulti == 2:
            add_proc()
        elif resulti == 3:
            pass
        else:
            break
        
        
def Next_fit(mem):
    memoria_principal = memoria.Memoria(mem[0], mem[1])
    processador = fifo.FIFO()
    while True:
        
        resulti = utilitarios.menu("Esta em Next_fit, oque deseja fazer?", ["Executar","Adicionar Item", "Verificar", "Voltar"])

        if resulti == 1:
            pass
        elif resulti == 2:
            pass
        elif resulti == 3:
            pass
        else:
            break

def add_proc(fifo):
    uti

while True:
    algoritimo = utilitarios.menu("Qual o algoritimo sera executado", ["First_fit", "Next_fit", "Sair"])

    if algoritimo == 1:
        First_fit(mem)
    
    elif algoritimo == 1:
        Next_fit(mem)
    
    else:
        break
    

utilitarios.titulo_modelo("Fiim da apresentação")
