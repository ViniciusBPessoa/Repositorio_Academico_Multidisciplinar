def subtrair_listas(lista1, lista2):
    return [a - b for a, b in zip(lista1, lista2)]

def multiplicar_matrizes(matriz_a, matriz_b):
    rows_a = len(matriz_a)
    cols_a = len(matriz_a[0])
    rows_b = len(matriz_b)
    cols_b = len(matriz_b[0])

    if cols_a != rows_b:
        raise ValueError("O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.")

    resultado = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado