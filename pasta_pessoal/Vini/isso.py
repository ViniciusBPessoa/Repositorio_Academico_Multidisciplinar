import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Configurações iniciais
R = 1.0  # Raio da esfera 3D
z_inicial = 0.0  # Posição inicial da bola (eixo Z)

# Cria a janela e divide em duas partes (Esquerda 3D, Direita 2D)
fig = plt.figure(figsize=(12, 6))
ax3d = fig.add_subplot(121, projection='3d')
ax2d = fig.add_subplot(122)

# Ajusta o layout para dar espaço para a barra de controle embaixo
plt.subplots_adjust(bottom=0.2)

# --- DADOS PARA O 3D ---
# Plano que vai cortar a bola
xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 10), np.linspace(-1.5, 1.5, 10))
zz_plano = np.zeros_like(xx)

# Malha da Esfera
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 20)
x_esfera = R * np.outer(np.cos(u), np.sin(v))
y_esfera = R * np.outer(np.sin(u), np.sin(v))

def desenhar_graficos(posicao_z):
    # Limpa os dois gráficos para redesenhar o novo frame
    ax3d.clear()
    ax2d.clear()
    
    # --- RENDERIZAÇÃO 3D (Esquerda) ---
    ax3d.set_title("Visão 3D: Esfera Cortada pelo Plano")
    # Desenha o plano (translúcido)
    ax3d.plot_surface(xx, yy, zz_plano, alpha=0.4, color='gray')
    
    # Desenha a esfera na nova posição
    z_esfera = R * np.outer(np.ones(np.size(u)), np.cos(v)) + posicao_z
    ax3d.plot_wireframe(x_esfera, y_esfera, z_esfera, color='blue', alpha=0.3)
    
    # Trava os eixos 3D para a câmera não ficar pulando
    ax3d.set_xlim([-1.5, 1.5])
    ax3d.set_ylim([-1.5, 1.5])
    ax3d.set_zlim([-2.0, 2.0])
    
    # --- RENDERIZAÇÃO 2D (Direita) ---
    ax2d.set_title("Visão 2D: O Corte")
    ax2d.set_xlim([-1.5, 1.5])
    ax2d.set_ylim([-1.5, 1.5])
    ax2d.set_aspect('equal') # Mantém o gráfico quadrado pra não distorcer o círculo
    ax2d.grid(True, linestyle='--', alpha=0.6)
    
    # Verifica se a bola está tocando no plano
    if abs(posicao_z) <= R:
        # Matemática: Calcula o raio do corte usando Pitágoras
        raio_corte = np.sqrt(R**2 - posicao_z**2)
        circulo = plt.Circle((0, 0), raio_corte, color='red', fill=True, alpha=0.6)
        ax2d.add_patch(circulo)
        ax2d.text(-1.4, 1.3, f"Raio atual: {raio_corte:.2f}", color='red', weight='bold')
    else:
        ax2d.text(-0.8, 0, "A bola não encosta no plano", color='red', weight='bold')

# Desenha a tela inicial
desenhar_graficos(z_inicial)

# --- BARRA DE CONTROLE (SLIDER) ---
# Cria um eixo lá embaixo para colocar o slider
ax_slider = plt.axes([0.25, 0.05, 0.5, 0.03])
slider_z = Slider(ax_slider, 'Mover Bola (Z)', -1.5, 1.5, valinit=z_inicial)

# Função que é chamada toda vez que você mexe no slider
def atualizar(val):
    desenhar_graficos(slider_z.val)
    fig.canvas.draw_idle()

slider_z.on_changed(atualizar)

# Mostra o programa na tela
plt.show()