def lista_diretorio(diretorio_atual):
    lista_diretorios = []
    while True:
        lista_diretorios.append(diretorio_atual.nome)
        if diretorio_atual.pai == None:
            break
        else:
            diretorio_atual = diretorio_atual.pai
        
    streng = ""
    for x in reversed(lista_diretorios):
        streng += x
    
    return streng

def lista_itens(diretorio):
    
    diretorio.listar_itens()
    input("aperte enter para continuar!")
    
def adicionar_arquivo():
    pass

def adicionar_diretorio(atual, novo):
    
    verificador = 0
    aux = "/" + novo
    
    for c in atual.arquivos:
        if aux == c.nome:
            verificador = 1
            break
    
    if verificador == 1:
        print("\033[0;31mJá existe uma pasta com esse nome nesse diretorio!\033[m")
        input("Aperte enter para continuar!")
    else:
        atual.adicionar_diretorio(novo)

def remover_diretorio():
    pass

def remover_arquivo():
    pass