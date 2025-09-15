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
        return "Não é possível multiplicar as matrizes"

    # Inicializa a matriz resultado com zeros
    resultado = [[0 for M in range(colunas_matriz2)] for M in range(linhas_matriz1)]

    # Multiplicação das matrizes
    for i in range(linhas_matriz1):
        for j in range(colunas_matriz2):
            for k in range(colunas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def elevador_matriz(lista, expoente): # eleva uma matriz ao expoente
    return [item ** expoente for item in lista]

def dividir_matriz(lista, divisor): # divide cada item de uma matriz por divisor
    return [item / divisor for item in lista]
