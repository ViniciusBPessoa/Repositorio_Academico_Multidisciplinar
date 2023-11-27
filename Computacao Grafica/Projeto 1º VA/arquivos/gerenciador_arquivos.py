import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auxiliares import operacoes_aux, matematica_aux

# esse codigo temo objetivo de carregar minha malha na memoria formando as duas tabelas em formato de dicionario

class Gerenciador_Modelo: # responsavel por gerenciar o carregamento do modelo
    def __init__(self):
        self.diretorio_modelos = os.path.dirname(os.path.abspath(__file__)) + "/modelos/" # Para executar sempre (Carrega a devida localização)
        self.nome_malha_atual = None # recebe o nome do arquivo da malha
        self.malha_perspectiva = None # essa é a malha final (perpectiva e bem formada)
        self.malha_atual = None # mantem a malha atravez de um dicionario
        self.rasteiros = None

    def carregar_malha(self, malha = "piramide"): # carrega a malha
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
        
    def projecao_malha(self, matriz_transfer, foco, normal_hx_hy, resolucao):
        lista_projetada = [] # carrega a lista com os vetores ate o fim (com as transiçoes corretas e a perspectiva)
        
        if self.malha_atual != None: # caso a malha ainda não esteja carregada 0
            lista_coordenadas = self.malha_atual["vertices"]

            for ponto in lista_coordenadas:
                # Transição linear
                ponto = matematica_aux.subtrair_listas(ponto, foco) # P - C
                ponto = [[ponto[0]], [ponto[1]], [ponto[2]]] # passa o ponto para uma matris de 1 coluna
                aux = matematica_aux.multiplicar_matrizes(matriz_transfer, ponto) # tudo agora esta na base correta (resta perspectiva)

                # perpectiva
                aux = [normal_hx_hy[0] * (aux[0][0]/aux[2][0]), normal_hx_hy[1] * (aux[1][0]/aux[2][0])] # adiciona perspectiva e remove o eixo Z

                aux = [ int(((aux[0]+1) / 2) * resolucao[0] + 0.5), 
                       int(resolucao[1] - (aux[1]+1 / 2) * resolucao[1] + 0.5)]

                lista_projetada.append(aux)
            print(lista_projetada)
            self.malha_perspectiva = lista_projetada
            self.rasteirizacao()
        else:
            return -1
        
    def rasteirizacao(self):
        faces = self.malha_atual["faces"]
        self.rasteiros = []
        print(faces)
        for face in faces:
            linhas = []
            linha = self.linha(self.malha_perspectiva[face[0] - 1], self.malha_perspectiva[face[1] - 1])
            linhas.append(linha)
            linha = self.linha(self.malha_perspectiva[face[1] - 1], self.malha_perspectiva[face[2] - 1])
            linhas.append(linha)
            linha = self.linha(self.malha_perspectiva[face[2] - 1], self.malha_perspectiva[face[0] - 1])
            linhas.append(linha)
            self.rasteiros.append(linhas)
    
    def linha(self, ponto1, ponto2):
        lista = []
        x1, y1 = ponto1
        x2, y2 = ponto2
        
        deltax = abs(x2 - x1)
        deltay = abs(y2 - y1)
        
        if x1 < x2:
            sx = 1
        else:
            sx = -1
        if y1 < y2:
            sy = 1
        else:
            sy = -1
        
        erro = deltax - deltay
        
        x = x1
        y = y1
        
        while True:
            lista.append((x, y))
            
            if x == x2 and y == y2:
                break
            
            erro2 = 2 * erro
            
            if erro2 > -deltay:
                erro -= deltay
                x += sx
            
            if erro2 < deltax:
                erro += deltax
                y += sy
        
        return lista


    def exibir_malha(self): # So printa bonitinho
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

    def carregar_camera(self, camera = "camera01", ortogonalizar = True): # Responsavel por carregar as informaçoes da camera
        # Caso ortogonalizar seja verdadeiro a variavel camera_atual sera completa com (V, N, U) carregados e ortonormalizados  caso seja falsa ele apenas carrega da memoria  


        arquivo_camera = self.diretorio_cameras + f"{camera}.txt"

        try:  # verifica se o arquivo esta ou não na memoria
            with open(arquivo_camera, 'r') as camera_carregada:
                linhas = camera_carregada.readlines()
                possiveis_parametros = ['N', 'V', 'd', 'Hx', 'Hy', "C"]
                parametros_camera = {}

                for linha, conterudo in enumerate(possiveis_parametros):  # caso o mesmo esteja, essa parte anexa todos os itens a um dicionario
                    valor = linhas[linha].split() # função magica do python
                    parametros_camera[conterudo] = [float(x) for x in valor]
                
                self.camera_atual = parametros_camera
                self.nome_camera_atual = camera
                if ortogonalizar: # sendo carregada verifica a ortonormalização 
                    self.completar_camera()
                return self.camera_atual

        except FileNotFoundError:
            return -1  # Retorna -1 caso o arquivo não seja encontrado
    
    def completar_camera(self):
        self.camera_atual["V"] = operacoes_aux.ortogonalizador(N=self.camera_atual["N"], V=self.camera_atual["V"]) # ortogonaliza V
        self.camera_atual["U"] = operacoes_aux.gerador_U(N=self.camera_atual["N"], V_ortogonalizado=self.camera_atual["V"]) # gera U
        # Agora vem a normalização

        self.camera_atual["V"] = operacoes_aux.normalizador(self.camera_atual["V"]) # Vetories sendo normalizados 
        self.camera_atual["U"] = operacoes_aux.normalizador(self.camera_atual["U"])
        self.camera_atual["N"] = operacoes_aux.normalizador(self.camera_atual["N"])

    def get_Matrix_mudanca(self):
        return [self.camera_atual["U"], self.camera_atual["V"], self.camera_atual["N"]]

    def exibir_camera(self): # so para printar bonitinho
        if self.camera_atual != None:
            for chave, valor in self.camera_atual.items():
                print(f'{chave}: {valor}')


if __name__ == "__main__":
    gerenciador_cameras = Gerenciador_camera()
    nome_arquivo_camera = "camera01"  # Substitua pelo nome do arquivo da câmera desejado
    malha = Gerenciador_Modelo()
    malha.carregar_malha()
    print(malha.malha_atual)
    parametros_camera = gerenciador_cameras.carregar_camera(nome_arquivo_camera)
    gerenciador_cameras.exibir_camera()
    print(gerenciador_cameras.get_Matrix_mudanca())

    