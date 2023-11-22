import numpy as np

def projecao_ortogonal(N, V):
    N = np.array(N)
    V = np.array(V)
    
    # Calcula o produto escalar entre u e v
    produto_escalar = np.dot(N, V)
    
    # Calcula o produto escalar entre u e u
    produto_escalar_nn = np.dot(N, N)
    
    # Calcula a projeção ortogonal de v sobre u
    proj_n_v = (produto_escalar / produto_escalar_nn) * N
    
    return proj_n_v.tolist()

def novo_v(V, proj_N_V):
    V = np.array(V)
    proj = np.array(proj_N_V)
    return (V - proj).tolist()


def ortogonalizador(N, V):
    return novo_v(V, projecao_ortogonal(N, V))

def gerador_U(N, V_ortogonalizado):
    N = np.array(N)
    V_ortogonalizado = np.array(V_ortogonalizado)
    
    # Calcula o produto vetorial entre u e v
    produto = np.cross(N, V_ortogonalizado)
    
    return produto.tolist()

def normalizador(vetor):
    vetor_quad = np.power(vetor, 2)
    norma = np.sum(vetor_quad) ** 0.5
    return vetor / norma

# Exemplo de utilização da função
vetor_n = [-1, -1, -1]
vetor_v = [0, 0, 1]

print(gerador_U(vetor_n, ortogonalizador(vetor_n, vetor_v)))