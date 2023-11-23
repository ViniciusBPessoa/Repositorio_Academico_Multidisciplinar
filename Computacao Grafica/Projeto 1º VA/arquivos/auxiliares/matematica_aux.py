def subtrair_listas(lista1, lista2):
    return [a - b for a, b in zip(lista1, lista2)]

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
