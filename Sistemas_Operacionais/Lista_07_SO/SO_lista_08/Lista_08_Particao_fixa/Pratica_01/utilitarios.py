# Função que verifica se o valor digitado esta dentro do range da lista e se é um inteiro
from os import system

def verifica_Int_lista (valor, lista):
    try: 
        test = int(valor) - 1
        
        if test < 0 or test > len(lista) - 1:
            return -1
        else:
            return test
    except:
        
        return -1

# Printa ana tela um menu e aguarda o input do usuario 
def menu(titulo, lista):
    system("cls")
    titulo_modelo(titulo)
    for c in range(0, len(lista)):
        print(f"\033[0;34m|{c+1:02}|\033[m - \033[0;32m{lista[c]}\033[m")
    
    while True:
        
        print()
        valor = verifica_Int_lista(input("Qual a opção: "), lista) + 1
        if valor == 0:
            print(f"\033[0;31mValor insrido é invalido!\033[m")
            continue
        else:
            break
    print("-"*20)
    return valor

def titulo_modelo(nome):
    espacos = " " * ((len(nome) + 10 - len(nome)) // 2)  # Determina a quantidade de espaços antes e depois do nome
    print("-" * (len(nome) + 10))
    print(f"\033[0;33m{espacos}{nome}{espacos}\033[m".center(len(nome) + 10))
    print("-" * (len(nome) + 10))

def verifica_int(str):
    while True:
        try:
            valor = int(input(str))
            break
        except:
            print(f"\033[0;31mValor invalido!\033[m")
    
    return valor
