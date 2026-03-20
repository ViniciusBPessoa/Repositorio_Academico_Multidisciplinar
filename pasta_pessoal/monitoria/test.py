tarefas = []

while True:
    print("\n_MENU DO PLANNER_")
    print("1- Visualizar tarefas")
    print("2- Adicionar tarefas")
    print("3- Remover tarefas")
    print("4- Sair")
    
    opcao = input("Escolha sua opção: ")
    
    if opcao == "1":
        if len(tarefas) == 0:
            print("Não existe nenhuma tarefa na lista.")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}")
                
    elif opcao == "2":
        nova_tarefa = input("Qual tarefa você deseja adicionar?: ")
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")
        
    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não existe nenhuma tarefa para remover")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}")
            
            try:
                indice = int(input("Digite o número da tarefa que você quer remover: "))
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"A tarefa '{removida}' foi removida")
                else:
                    print("Índice inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")
                
    elif opcao == "4":
        print("Saindo do Menu do Planner")
        break
    
    else:
        print("Opção inválida! Por favor, escolha uma opção de 1 a 4.")