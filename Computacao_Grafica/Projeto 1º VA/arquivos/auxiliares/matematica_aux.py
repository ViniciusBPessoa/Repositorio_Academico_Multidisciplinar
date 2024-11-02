def subtrair_matrizes(lista1, lista2):
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


def produto_vetorial(vetor1, vetor2): # produto vetorial
    x = vetor1[1] * vetor2[2] - vetor1[2] * vetor2[1]
    y = vetor1[2] * vetor2[0] - vetor1[0] * vetor2[2]
    z = vetor1[0] * vetor2[1] - vetor1[1] * vetor2[0]
    
    return [x, y, z]

def normaliza_matriz(vetor): # Normaliza um vetor
    vetor_quad = elevador_matriz(vetor, 2)
    norma = sum(vetor_quad) ** 0.5
    return dividir_matriz(vetor, norma)

def somar_vetores(vetor1, vetor2):
    return [vetor1[0] + vetor2[0], vetor1[1] + vetor2[1], vetor1[2] + vetor2[2]]


def calcula_distancia(N):
    distancia = elevador_matriz(N, 2)
    distancia = sum(distancia)
    return distancia ** 0.5

def area_triangulo(P1, P2, P3):
    calc_b_a = subtrair_matrizes(P2, P1)
    calc_c_a = subtrair_matrizes(P3, P1)

    

    prod = produto_vetorial(calc_b_a, calc_c_a)
    
    return calcula_distancia(prod)


def multiplicar_constante_lista(constante, lista):

    resultado = [constante * elemento for elemento in lista]
    return resultado

def somar_vetores(vetor1, vetor2):
 
    # Verifica se os vetores têm o mesmo comprimento
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo comprimento.")

    # Realiza a soma dos vetores elemento por elemento
    resultado = [vetor1[i] + vetor2[i] for i in range(len(vetor1))]
    
    return resultado

def negativar_vetor(vetor):
    # Negativa cada elemento do vetor
    resultado = [-elemento for elemento in vetor]
    
    return resultado

def multiplicar_matrizes_especial(matriz1, matriz2):
    print(matriz1, matriz2)
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("As dimensões das matrizes não são compatíveis para multiplicação.")
    
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    
    # Verificar se matriz1 é uma matriz de vetores ou uma matriz normal
    if isinstance(matriz1[0][0], list):
        # Multiplicação de matrizes de vetores
        resultado = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                produto_componente = [matriz1[i][j][k] * matriz2[i][j][k] for k in range(3)]
                linha.append(produto_componente)
            resultado.append(linha)
    else:
        # Tratar matriz1 como uma matriz normal e realizar multiplicação
        # Convertendo matriz1 temporariamente em uma matriz coluna
        matriz1_coluna = [[[matriz1[i][j]] for i in range(linhas)] for j in range(colunas)]
        resultado = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                produto_componente = [matriz1_coluna[j][i][0] * matriz2[i][j][k] for k in range(3)]
                linha.append(produto_componente)
            resultado.append(linha)
    
    return resultado