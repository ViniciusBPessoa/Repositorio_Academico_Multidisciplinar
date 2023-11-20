import os

# esse codigo temo objetivo de carregar minha malha na memoria formando as duas tabelas em formato de dicionario

class Gerenciador_Modelo: # responsavel por gerenciar o carregamento do modelo
    def __init__(self):
        self.diretorio_modelos = os.path.dirname(os.path.abspath(__file__)) + "/modelos/" # Para executar sempre (Carrega a devida localização)
        self.nome_malha_atual = None # recebe o nome do arquivo da malha
        self.malha_atual = None # mantem a malha atravez de um dicionario

    def carregar_malha(self, malha = "piramide", busca = False): # carrega a malha
        arquivo_malha = self.diretorio_modelos + f"{malha}.byu" # localiza o arquivo

        try: # try (para n dar merda)
            with open(arquivo_malha, 'r') as malha_carregada: # abre o arquiivo
                linhas = malha_carregada.readlines() # carrega as linhas do arquivo
                num_vertices, num_triangulos = map(int, linhas[0].split()) 
                vertices = []
                faces = []

                # carregando os vertices
                for linha in linhas[1:num_vertices + 1]:
                    coordenadas = list(map(float, linha.split()))
                    vertices.append(coordenadas)

                # carregando as faces (triângulos)
                for linha in linhas[num_vertices + 1 : num_vertices + num_triangulos + 1]:
                    indices = list(map(int, linha.split()))
                    faces.append(indices)

                self.malha_atual = {'vertices': vertices, 'faces': faces} # adicionando o dicionario a variavel correta
                self.nome_malha_atual = malha
                return self.malha_atual

        except FileNotFoundError:
            return -1 # caso o retorno seja -1 o modelo não foi carregado com sucesso
    

    def exibir_malha(self): # so printa bonitinho
        if self.malha_atual != None:
            print("Vértices da Malha Carregada:")
            for indice, vertice in enumerate(self.malha_atual['vertices'], start=1):
                print(f"Vértice {indice}: {vertice}")

            print("\nFaces (Triângulos) da Malha Carregada:")
            for indice, face in enumerate(self.malha_atual['faces'], start=1):
                print(f"Face {indice}: {face}")

class Gerenciador_camera:
    def __init__(self) -> None:
        self.diretorio_cameras = os.path.dirname(os.path.abspath(__file__)) + "/cameras/" 
        self.nome_camera_atual = None 
        self.camera_atual = None 

    def carregar_camera(self, camera):
        arquivo_camera = self.diretorio_cameras + f"{camera}.txt"

        try:
            with open(arquivo_camera, 'r') as camera_carregada:
                linhas = camera_carregada.readlines()
                possiveis_parametros = ['N', 'V', 'd', 'Hx', 'Hy', "C"]
                parametros_camera = {}

                for linha, conterudo in enumerate(possiveis_parametros):
                    parametros_camera[conterudo] = linhas[linha].split()
                
                print(parametros_camera)
                self.camera_atual = parametros_camera
                self.nome_camera_atual = camera
                return self.camera_atual

        except FileNotFoundError:
            return -1  # Retorna -1 caso o arquivo não seja encontrado

if __name__ == "__main__":
    gerenciador_cameras = Gerenciador_camera()
    nome_arquivo_camera = "camera01"  # Substitua pelo nome do arquivo da câmera desejado
    parametros_camera = gerenciador_cameras.carregar_camera(nome_arquivo_camera)