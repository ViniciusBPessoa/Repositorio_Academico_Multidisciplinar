from Utilitarios import padrao

usuarios = {}

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")

    usuarios[nome] = {"filmes": {}}

    print("Usuário cadastrado com sucesso!")

def remover_usuario():
    nome = input("Digite o nome do usuário a ser removido: ")

    if nome in usuarios:
        del usuarios[nome]
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

def cadastrar_filme():
    if not usuarios:
        print("Erro: Nenhum usuário cadastrado no sistema.")
        return

    lista_nomes = list(usuarios.keys())
    
    print("\n--- Selecione o Usuário ---")
    indice_escolhido = padrao.menu(lista_nomes)
    
    nome_usuario = lista_nomes[indice_escolhido - 1]

    nome_filme = input(f"Digite o nome do filme para {nome_usuario}: ")
    
    try:
        nota_filme = float(input("Digite a nota do filme (0 a 10): "))
        if 0 <= nota_filme <= 10:
            usuarios[nome_usuario]["filmes"][nome_filme] = nota_filme
            print(f"Filme '{nome_filme}' cadastrado para {nome_usuario}!")
        else:
            print("Erro: Nota inválida.")
    except ValueError:
        print("Erro: Digite um valor numérico para a nota.")

while True:
    escolha = padrao.menu(["cadastrar_usuario", "cadastrar_filme", "remover_usuario", "sair"])

    if escolha == 1:
        cadastrar_usuario()

    elif escolha == 2:
        cadastrar_filme()

    elif escolha == 3:
        remover_usuario()

    elif escolha == 4:
        print("Opção: Sair")
        break  