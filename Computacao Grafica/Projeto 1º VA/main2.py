import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def load_object(filename):
    vertices = []
    triangles = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        num_vertices, num_triangles = map(int, lines[0].split())
        print("Número de vértices:", num_vertices)
        print("Número de triângulos:", num_triangles)
        for line in lines[1:num_vertices+1]:
            vertex = list(map(float, line.split()))
            vertices.append(vertex)
        for line in lines[num_vertices+1:]:
            triangle = list(map(int, line.split()))
            if len(triangle) == 3:  # Somente adiciona triângulos com 3 vértices
                print("Triângulo lido:", triangle)
                triangles.append(triangle)

    print("Vértices lidos:", len(vertices))
    print("Triângulos lidos:", len(triangles))
    return vertices, triangles

# Definindo parâmetros de câmera e iluminação
camera_params = {
    "C": (0, -500, 500),
    "N": (0, 1, -1),
    "V": (0, -1, -1),
    "fovy": 45,
    "aspect": 1.33,  # Aspect ratio depends on your screen resolution
    "near": 5,
    "far": 10000,
    "Pl": (0, 500, 200)
}

light_params = {
    "ambient": (0.4, 0.4, 0.4, 1.0),
    "diffuse": (0.5, 0.85, 1.0, 1.0),
    "specular": (0.5, 0.85, 1.0, 1.0)
}

material_params = {
    "ambient": (0.2, 0.2, 0.2, 1.0),
    "diffuse": (0.7, 0.5, 0.8, 1.0),
    "specular": (0.5, 0.5, 0.5, 1.0),
    "emissive": (0.0, 0.0, 0.0, 1.0),
    "eta": 100
}

# Função para desenhar o objeto 3D
def draw_object(vertices, triangles):
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        for vertex_index in triangle:
            vertex = vertices[vertex_index - 1]
            glVertex3fv(vertex)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(camera_params["fovy"], camera_params["aspect"], camera_params["near"], camera_params["far"])
    glTranslatef(0.0, 0.0, -500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    glTranslatef(0, 0, 10)
                elif event.key == pygame.K_s:
                    glTranslatef(0, 0, -10)
                elif event.key == pygame.K_a:
                    glTranslatef(-10, 0, 0)
                elif event.key == pygame.K_d:
                    glTranslatef(10, 0, 0)

        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_rel()
            glRotatef(x, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()

        # Configura iluminação e material
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_params["ambient"])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_params["diffuse"])
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_params["specular"])
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, material_params["ambient"])
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, material_params["diffuse"])
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, material_params["specular"])
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, material_params["emissive"])
        glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, material_params["eta"])

        # Desenha o objeto 3D
        vertices, triangles = load_object(r"C:\Users\Pichau\Desktop\Faculdade\Projects\Facul Repositorios\Repositorios_Universitarios\Computacao Grafica\Projeto 1º VA\arquivos\modelos\piramide.byu")
        draw_object(vertices, triangles)

        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
