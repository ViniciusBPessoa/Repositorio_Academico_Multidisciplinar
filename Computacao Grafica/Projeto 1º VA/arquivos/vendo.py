import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def original_function(x):
    return np.sin(x) + 4 * np.cos(x) - 1

# Gerando 21 pontos no intervalo [-2, 4]
num_points = 21
x_values = np.linspace(-2, 4, num_points)
y_values_original = original_function(x_values)

# Plot da função original
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values_original, label='Função Original')
plt.title('Gráfico da Função Original')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

from scipy.interpolate import Rbf

# Definindo os centros para a RBF
centers = np.linspace(-2, 4, 4)  # 4 centros no intervalo [-2, 4]

# Calculando os valores da função nos centros
y_values_centers = original_function(centers)

# Ajustando a rede neural RBF
rbf = Rbf(centers, y_values_centers, function='gaussian')

# Calculando a função aproximada nos pontos x_values
y_values_rbf = rbf(x_values)

# Plot da função original e da função aproximada pela RBF
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values_original, label='Função Original')
plt.plot(x_values, y_values_rbf, label='Função Aproximada (RBF)', linestyle='--')
plt.title('Aproximação da Função pela Rede Neural RBF')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
