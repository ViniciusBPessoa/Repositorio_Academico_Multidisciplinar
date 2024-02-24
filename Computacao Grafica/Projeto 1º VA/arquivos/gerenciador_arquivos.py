import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auxiliares import operacoes_aux, matematica_aux

# esse codigo temo objetivo de carregar minha malha na memoria formando as duas tabelas em formato de dicionario

class Gerenciador_Modelo: # responsavel por gerenciar o carregamento do modelo
    def __init__(self):
        self.diretorio_modelos = os.path.dirname(os.path.abspath(__file__)) + "/modelos/" # Para executar sempre (Carrega a devida localização)
        self.nome_malha_atual = None # recebe o nome do arquivo da malha
        self.malha_atual = None # mantem a malha atravez de um dicionario

        self.malha_perspectiva = None # essa é a malha final (perpectiva e bem formada)
        self.rasteiros = None # total rasteiros
        self.preenchimento = None # todas as linhas que preenchem o modelo

        self.Z_buffer = []

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
        
    def projecao_malha(self, matriz_transfer, foco, distancia, normal_hx_hy, resolucao, Z_bff):
        lista_projetada = [] # carrega a lista com os vetores ate o fim (com as transiçoes corretas e a perspectiva)
        self.Z_buffer = Z_bff


        if self.malha_atual != None: # caso a malha ainda não esteja carregada 0
            lista_coordenadas = self.malha_atual["vertices"]

            for ponto in lista_coordenadas:
                # Transição linear
                ponto = matematica_aux.subtrair_listas(ponto, foco) # P - C
                ponto = [[ponto[0]], [ponto[1]], [ponto[2]]] # passa o ponto para uma matris de 1 coluna
                aux = matematica_aux.multiplicar_matrizes(matriz_transfer, ponto) # tudo agora esta na base correta (resta perspectiva)
                
                aux[0][0] = distancia[0] * (aux[0][0] / aux[2][0])
                aux[1][0] = distancia[0] * (aux[1][0] / aux[2][0])
                # perpectiva

                
                aux = [(aux[0][0]/normal_hx_hy[0]), (aux[1][0]/normal_hx_hy[1]), aux[2][0]] # adiciona perspectivaem x e continua o eixo Z para  o zbuffer
                
                aux = [int((((aux[0]+1) / 2) * resolucao[0]) + 0.5), 
                       int(resolucao[1] - (((aux[1]+1) / 2) * resolucao[1])  + 0.5),
                       int(aux[2] + 0.5)] # adiciona perspectivaem y e remove o eixo Z
                
                if 0 <= aux[0] <= resolucao[0] and 0 <= aux[1] <= resolucao[1]:
                    z_atual = self.Z_buffer[aux[0]][aux[1]]

                    if z_atual == -1 or z_atual > aux[2]:
                        self.Z_buffer[aux[0]][aux[1]] = aux[2]
                        
            
                lista_projetada.append(aux)
            self.malha_perspectiva = lista_projetada
            self.rasteirizacao() # já jera a rasterização
            return self.Z_buffer
        else:
            return -1
        
    def rasteirizacao(self): # rasteriza a malha
        faces = self.malha_atual["faces"] # carrega as faces da malha
        self.rasteiros = [] # armazena as linhas
        self.preenchimento = [] # armazena o conteudo dos triangulos
        for face in faces: # loop de faces
            
            # coletando os pontos
            a = self.malha_perspectiva[face[0] - 1]
            b = self.malha_perspectiva[face[1] - 1]
            c = self.malha_perspectiva[face[2] - 1]

            # gerando as linhas de cada face
            linhas = []
            linha_a_b = self.linha(a, b)
            linhas.append(linha_a_b)

            linha_b_c = self.linha(b, c)
            linhas.append(linha_b_c)

            linha_c_a = self.linha(c, a)
            linhas.append(linha_c_a)

            lista_pontos = [a,b,c] # armazena os tres pontos
            ponto_central = operacoes_aux.encontrar_centro(lista_pontos) # devolve o ponto no centro em y
            ponto_a_b_c = lista_pontos[ponto_central] # ponto central pode ser a, b, c tanto faz

            # gera o ponto D para cortar o triangulo
            if ponto_central == 0:
                ponto_d = operacoes_aux.item_central_D(linha_b_c, ponto_a_b_c[1])
            elif ponto_central == 1:
                ponto_d = operacoes_aux.item_central_D(linha_c_a, ponto_a_b_c[1])
            elif ponto_central == 2:
                ponto_d = operacoes_aux.item_central_D(linha_a_b, ponto_a_b_c[1])
            if ponto_d != -1:
                
                #Gera a linha que corta o triangulo para rasterizar o sentro
                listra_corte = self.linha(ponto_d, ponto_a_b_c)
                linhas.append(listra_corte)
                self.rasteiros.append(linhas) # adiciona todas as linhas a lista geral

                for id_inicial in range(len(lista_pontos)): # Gera o conteudo
                    if id_inicial != ponto_central: # verificação para impedir que o pondo gerador de D seja levado em consideração
                        ponto_referencia = lista_pontos[id_inicial] # um dos dois casos ou o ponto acima ou o ponto abaixo
                        if ponto_referencia[1] > ponto_a_b_c[1]: # ponto acima
                            
                            linha_1 = self.linha(ponto_referencia, ponto_d) # gera uma linha de apoio entre o ponto d e a referencia 
                            linha_2 = self.linha(ponto_referencia, ponto_a_b_c) # O mesmo
                            
                            y = ponto_referencia[1] # y = o y da referencia 
                            pontos_plot = [] # lista com listas de pontos 
                            linha = [] # lista de po9nto para cada linha
                            
                            while True: # loop principal
                                if y == ponto_d[1]: # trava a rasteirização quando acha o ponto D
                                    break
                                x_lado_1 = linha_1[operacoes_aux.encontrar_lista_por_Y(linha_1, y)] # calcula x_min e x_max
                                x_lado_2 = linha_2[operacoes_aux.encontrar_lista_por_Y(linha_2, y)]
                                linha = self.linha(x_lado_1, x_lado_2)
                                
                                y -= 1 # caso o ponto seja aciam y -= 1
                                pontos_plot.append(linha)
                                self.preenchimento.append(linha)
                        else: # ponto abaixo (restante igual o anterior)
                            linha_1 = self.linha(ponto_referencia, ponto_d) # gera uma linha de apoio entre o ponto d e a referencia 
                            linha_2 = self.linha(ponto_referencia, ponto_a_b_c) # O mesmo
                            
                            y = ponto_referencia[1] # y = o y da referencia 
                            pontos_plot = [] # lista com listas de pontos 
                            linha = [] # lista de po9nto para cada linha
                            
                            while True: # loop principal
                                if y == ponto_d[1]: # trava a rasteirização quando acha o ponto D
                                    break
                                x_lado_1 = linha_1[operacoes_aux.encontrar_lista_por_Y(linha_1, y)] # calcula x_min e x_max
                                x_lado_2 = linha_2[operacoes_aux.encontrar_lista_por_Y(linha_2, y)]
                                linha = self.linha(x_lado_1, x_lado_2)
                                
                                y += 1 # caso o ponto seja aciam y -= 1
                                pontos_plot.append(linha)
                                self.preenchimento.append(linha)

    def linha(self, ponto1, ponto2): # gera uma linha
        lista = [] # armazerna a linha
        x1, y1, z1 = ponto1 # carrega os pontos
        x2, y2, z2 = ponto2
        
        deltax = abs(x2 - x1) # valor absoluto
        deltay = abs(y2 - y1)
        deltaz = abs(z2 - z1)
        
        if x1 < x2: # verifica para qual lado a linha deve ir
            sx = 1
        else:
            sx = -1
        if y1 < y2:
            sy = 1
        else:
            sy = -1
        if z1 < z2:
            sz = 1
        else:
            sz = -1
        
        erro = deltax - deltay # gera o erro
        
        x = x1 # x, y a serem adicionados
        y = y1
        z = z1
        
        while True: # loop que cria a linha
            lista.append([x, y]) # adiciona o ponto
            if x == x2 and y == y2: # trava a linha no ponto final
                break
            
            erro2 = 2 * erro # calcula o erro

            if erro2 > -deltay: # verifica o erro para alterar x e y
                erro -= deltay
                x += sx
            
            if erro2 < deltax:
                erro += deltax
                y += sy


        z_uper = ((deltaz / len(lista)) + 0.5) * sz
        for item in lista:
            z += int(z_uper)
            item.append(z)

            if 0 <= item[0] <= len(self.Z_buffer) and 0 <= item[1] <= len(self.Z_buffer[0]):
                z_atual = self.Z_buffer[item[0]][item[1]]
                if z_atual == -1 or z_atual > item[2]:
                    self.Z_buffer[item[0]][item[1]] = item[2]

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

        self.Z_buffer = []

    def carregar_Z_buffer(self, resolucao):
        self.Z_buffer = [[-1] * resolucao[1] for _ in range(resolucao[0])] # preenche meu zbuffer com os valores que não serão dezenhados
        return self.Z_buffer

    def carregar_camera(self, camera = "camera01", ortogonalizar = True, resolucao = [750, 750]): # Responsavel por carregar as informaçoes da camera
        # Caso ortogonalizar seja verdadeiro a variavel camera_atual sera completa com (V, N, U) carregados e ortonormalizados  caso seja falsa ele apenas carrega da memoria  
        self.carregar_Z_buffer(resolucao)
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
    