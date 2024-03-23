from OpenGL.GL import *
from OpenGL.GLUT import *

# Função de renderização
def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)  # Canto inferior esquerdo
    glVertex2f(0.5, -0.5)   # Canto inferior direito
    glVertex2f(0.5, 0.5)    # Canto superior direito
    glVertex2f(-0.5, 0.5)   # Canto superior esquerdo
    glEnd()
    glFlush()

# Função de inicialização
def initialize():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Define a cor de fundo para preto
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)   # Define as coordenadas da janela de visualização

# Função principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Quadrado em OpenGL")
    glutDisplayFunc(draw_square)
    initialize()
    glutMainLoop()

# Chama a função principal
if __name__ == "__main__":
    main()
