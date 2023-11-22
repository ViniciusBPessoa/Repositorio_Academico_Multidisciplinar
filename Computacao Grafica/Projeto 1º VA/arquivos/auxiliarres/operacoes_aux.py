import numpy as np

def projecao_ortogonal(u, v):
    u = np.array(u)
    v = np.array(v)
    
    # Calcula o produto escalar entre u e v
    produto_escalar = np.dot(u, v)
    
    # Calcula o produto escalar entre u e u
    produto_escalar_uu = np.dot(u, u)
    
    # Calcula a projeção ortogonal de v sobre u
    proj_u_v = (produto_escalar / produto_escalar_uu) * u
    
    return proj_u_v

# Exemplo de utilização da função
vetor_u = [1, 2, 3]
vetor_v = [2.28571429, 4.57142857, 6.85714286]

projetado = projecao_ortogonal(vetor_u, vetor_v)
print("Projeção ortogonal de v sobre u:", projetado)
