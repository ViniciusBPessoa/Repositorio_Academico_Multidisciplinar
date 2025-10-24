tarefas = []

while True:
    print(" GERENCIADOR DE TAREFAS")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}")

    elif opcao == "2":
        nova = input("Digite a nova tarefa: ")
        tarefas.append(nova)
        print("Tarefa adicionada!")

    elif opcao == "3":
        if not tarefas:
            print("A lista está vazia")
        else:
            indice = int(input("Digite o índice da tarefa para remover: "))
            if 0 <= indice < len(tarefas):
                tarefas.pop(indice)
                print("Tarefa removida")
            else:
                print("Índice inválido.")

    elif opcao == "4":
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida")