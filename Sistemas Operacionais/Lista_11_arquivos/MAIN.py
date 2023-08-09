import Ajudadores.utilitarios as utilitarios
from tipos_arquivos.arquivos import Arquivo
from tipos_arquivos.diretorio import Diretorio
import Ajudadores.controlador as control
import memoria.memoria as memoria
from os import system


lista_menu_principal = ["Listar diretorio", "Entrar em diretorio", "Voltar para o diretorio anterior", 
                        "Adicionar arquivo", "Adicionar diretorio", "Remover ITEM", "Sair"]

utilitarios.titulo_modelo("Seja bem vindo ao sistema de arquivos")

while True:
    tamanho = utilitarios.verifica_int("Qual o tamanho totoal da sua memoria em KB: ")
    tamanho_p = utilitarios.verifica_int("Qual o tamanho da partição da sua memoria em KB: ")
    if tamanho > tamanho_p:
        break
    else:
        utilitarios.titulo_modelo("A partição não pode ser maior que a memoria")
memoria = memoria.Memoria(tamanho, tamanho_p)

menu = input("Aperte enter para iniciar! ")

pai_de_todos = Diretorio("C", None) 
diretorio_atual = pai_de_todos

while True:
    system("cls")
    menu = utilitarios.menu(f'Você esta em "{control.lista_diretorio(diretorio_atual)}":', lista_menu_principal)
    system("cls")
    
    if menu == 1:
        utilitarios.titulo_modelo(f'Você esta em "{control.lista_diretorio(diretorio_atual)}":')
        control.lista_itens(diretorio_atual)
    
    elif menu == 2: # ENTRAR
        utilitarios.titulo_modelo(f'Você esta em "{control.lista_diretorio(diretorio_atual)}":')
        print("Voce esta na tela de entrar em diretorio!")
        
        result = diretorio_atual.listar_diretorios()
        
        if result == -1:
            print("\033[0;31mEssa pasta não possui diretorios\033[m")
            input("Aperte enter para continuar!")
            continue
        
        diretorio = utilitarios.verifica_int("Dijite a pasta que você quer abrir: ")
        
        if diretorio >= result or diretorio <= 0:
            print("\033[0;31mDiretorio selecionado não existe\033[m")
            continue
        
        aux = diretorio_atual.retorna_diretorio(diretorio)
        diretorio_atual = aux
        continue
    
    elif menu == 3:
        if diretorio_atual.pai != None:
            diretorio_atual = diretorio_atual.pai
        else:
            input("\033[0;31mVocê ja esta no diretorio base ou '/C' aperte enter para retornar\033[m")
    
    elif menu == 4:
        utilitarios.titulo_modelo("Você esta na parte de craição de arquivos")
        nome = input("Diga o nome do arquivo: ")
        tamanho = utilitarios.verifica_int("Diga o tamanho do arquivo: ")
        novo_arquivo = Arquivo(nome, tamanho, diretorio_atual)
        diretorio_atual.adiciona_arquivo(novo_arquivo)
    
    elif menu == 5:
        utilitarios.titulo_modelo("Voce esta na tela de adição de diretorios!")
        nome = input("Qual o nome do seu diretorio: ")
        control.adicionar_diretorio(diretorio_atual, nome)
        print("Diretorio adicionado com sucesso!")
    
    elif menu == 6:
        utilitarios.titulo_modelo(f'Você esta em "{control.lista_diretorio(diretorio_atual)}":')
        diretorio_atual.listar_itens()
        
        while True:
            item = utilitarios.verifica_int("Qual o ITEM que voce deseja deletar: ")
            
            if item <= 0 or item >= len(diretorio_atual.arquivos) + 1:
                print("\033[0;31mEsse arquivo não existe\033[m")
                continue
            else:
                break
        
        diretorio_atual.remover_arquivo(item)
    
    else:
        break
    
    
system("cls")
utilitarios.titulo_modelo("VLW e ate a proxima!")