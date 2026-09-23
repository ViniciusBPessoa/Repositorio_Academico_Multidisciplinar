def menu(itens_no_menu: list):
    for x in range(len(itens_no_menu)):
        print(f"{x+1} - {itens_no_menu[x]}")
    
    while True:
        escolha = int(input("Escolha uma opção: "))

        if 1 <= escolha <= len(itens_no_menu):
            return escolha
        
        else:
            print("Erro: Opção inválida. Tente novamente.")