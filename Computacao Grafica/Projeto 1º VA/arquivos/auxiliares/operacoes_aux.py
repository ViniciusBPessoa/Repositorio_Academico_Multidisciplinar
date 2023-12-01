import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import matematica_aux

def produto_escalar(vetor1, vetor2): # produto escalar
    return sum(x * y for x, y in zip(vetor1, vetor2))


def projecao_ortogonal(N, V): # calcula projeção
    produto_escalar_nv = produto_escalar(N, V)
    produto_escalar_nn = produto_escalar(N, N)
    
    proj_n_v = [(produto_escalar_nv / produto_escalar_nn) * x for x in N]
    
    return proj_n_v

def novo_v(V, proj_N_V): # gera um novo V
    return [x - y for x, y in zip(V, proj_N_V)]

def ortogonalizador(N, V): # ortogonalizador
    proj_N_V = projecao_ortogonal(N, V)
    return novo_v(V, proj_N_V)

def produto_vetorial(vetor1, vetor2): # produto vetorial
    x = vetor1[1] * vetor2[2] - vetor1[2] * vetor2[1]
    y = vetor1[2] * vetor2[0] - vetor1[0] * vetor2[2]
    z = vetor1[0] * vetor2[1] - vetor1[1] * vetor2[0]
    
    return [x, y, z]

def gerador_U(N, V_ortogonalizado): # Gera um U para a camera
    return produto_vetorial(N, V_ortogonalizado)


def normalizador(vetor): # Normaliza um vetor
    vetor_quad = matematica_aux.elevador_matriz(vetor, 2)
    norma = sum(vetor_quad) ** 0.5
    return matematica_aux.dividir_matriz(vetor, norma)

def item_central(lista): # acha o item central de um vetor
    indice_central = len(lista) // 2
    return lista[indice_central]

def encontrar_centro(lista):
    # Extrair o segundo valor de cada sublista
    segundos_valores = [sublista[1] for sublista in lista]
    ordenado = sorted(segundos_valores)
    valor_meio = ordenado[len(ordenado) // 2]
    
    # Retornar o índice da sublista cujo segundo valor é o valor do meio
    for i in range(len(lista)):
        if lista[i][1] == valor_meio:
            return i

def item_central_D(lista, estado): # ajuda na criação do ponto D
    tamanho = len(lista)
    if tamanho != 0:
        for x in lista:
            if x[1] == estado:
                return x
    else: return -1

def encontrar_lista_por_Y(lista, valor_procurado): # devolve o indice do da lita onde [[], [x,y], ...] y = valor_procurado
    for sublista in lista:
        if sublista[1] == valor_procurado:
            return lista.index(sublista)
    return None  # Retorna None se o valor não for encontrado
