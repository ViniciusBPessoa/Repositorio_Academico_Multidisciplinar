import utilitarios

def menu_interativo():
    
    utilitarios.titulo_modelo("Seja bem vindo ao simulador de memoria!!!")
    
    valor_memoria = utilitarios.verifica_int("Digite o tamanho da sua memoria em MB: ")
    
    while True:
        valor_particaos = utilitarios.verifica_int("Dijite o tamanho de suas partições em MB: ")
        
        if valor_particaos > valor_memoria:
            print("Valor dijitado é invalido!")
            continue
        
        else:
            break
    
    return valor_memoria, valor_particaos