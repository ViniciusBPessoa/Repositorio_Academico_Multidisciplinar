import os

class GerenciadorModelo:
    def __init__(self):
        self.diretorio_modelos = os.path.dirname(os.path.abspath(__file__)) + "/modelos/"
        self.malha_atual = None

    def carregar_malha(self, malha):
        arquivo_malha = self.diretorio_modelos + f"{malha}.byu"

        try:
            with open(arquivo_malha, 'r') as malha_carregada:
                linhas = malha_carregada.readlines()
                num_vertices, num_triangulos = map(int, linhas[0].split())
                vertices = []
                faces = []

                # Lendo os vértices
                for linha in linhas[1:num_vertices + 1]:
                    coordenadas = list(map(float, linha.split()))
                    vertices.append(coordenadas)

                # Lendo as faces (triângulos)
                for linha in linhas[num_vertices + 1 : num_vertices + num_triangulos + 1]:
                    indices = list(map(int, linha.split()))
                    faces.append(indices)

                self.malha_atual = {'vertices': vertices, 'faces': faces}
        
        except FileNotFoundError:
            print(f"O arquivo '{arquivo_malha}' não foi encontrado.")

    def exibir_malha(self):
        if self.malha_atual != None:
            print("Vértices da Malha Carregada:")
            for indice, vertice in enumerate(self.malha_atual['vertices'], start=1):
                print(f"Vértice {indice}: {vertice}")

            print("\nFaces (Triângulos) da Malha Carregada:")
            for indice, face in enumerate(self.malha_atual['faces'], start=1):
                print(f"Face {indice}: {face}")

# Exemplo de uso
ca = GerenciadorModelo()
ca.carregar_malha("piramide")
ca.exibir_malha()
