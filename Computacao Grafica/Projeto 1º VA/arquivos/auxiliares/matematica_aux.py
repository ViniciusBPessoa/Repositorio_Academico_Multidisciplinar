def subtrair_listas(lista1, lista2):
    # Verifica se as listas têm o mesmo comprimento
    if len(lista1) != len(lista2):
        return "As listas têm comprimentos diferentes. Não é possível subtrair."

    # Realiza a subtração elemento por elemento
    resultado = [lista1[i] - lista2[i] for i in range(len(lista1))]

    return resultado

def multiplicar_matrizes(matriz1, matriz2):
    linhas_matriz1 = len(matriz1)
    colunas_matriz1 = len(matriz1[0])
    linhas_matriz2 = len(matriz2)
    colunas_matriz2 = len(matriz2[0])

    # Verifica se as matrizes podem ser multiplicadas
    if colunas_matriz1 != linhas_matriz2:
        return "Não é possível multiplicar as matrizes. O número de colunas da primeira matriz não é igual ao número de linhas da segunda matriz."

    # Inicializa a matriz resultado com zeros
    resultado = [[0 for _ in range(colunas_matriz2)] for _ in range(linhas_matriz1)]

    # Multiplicação das matrizes
    for i in range(linhas_matriz1):
        for j in range(colunas_matriz2):
            for k in range(colunas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def transpor_matriz(matriz):
    # Obtém o número de linhas e colunas da matriz original
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    # Inicializa a matriz transposta com zeros
    matriz_transposta = [[0 for _ in range(num_linhas)] for _ in range(num_colunas)]

    # Preenche a matriz transposta com os elementos da matriz original
    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz_transposta[j][i] = matriz[i][j]

    return matriz_transposta