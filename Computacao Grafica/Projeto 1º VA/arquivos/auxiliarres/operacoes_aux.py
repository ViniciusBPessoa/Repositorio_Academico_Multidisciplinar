import numpy as np

# Seus dados
V = np.array([-1.0, -1.0, -1.0])
N = np.array([0.0, 0.0, 1.0])

# Processo de Gram-Schmidt
V -= np.dot(N, V) * N  # Remova a componente de V na direção de N
V /= np.linalg.norm(V)  # Normalize V

print("V corrigido:", V)
