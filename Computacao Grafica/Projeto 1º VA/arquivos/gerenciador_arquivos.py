import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auxiliares import operacoes_aux, matematica_aux

# esse codigo temo objetivo de carregar minha malha na memoria formando as duas tabelas em formato de dicionario

class Gerenciador_Modelo: # responsavel por gerenciar o carregamento do modelo
    def __init__(self):
        self.diretorio_modelos = os.path.dirname(os.path.abspath(__file__)) + "/modelos/" # Para executar sempre (Carrega a devida localização)
        self.iluminacao = Gerenciador_inuminacao()
        self.iluminacao.carregar_iluminacão()

        self.nome_malha_atual = None # recebe o nome do arquivo da malha
        self.malha_atual = None # mantem a malha atravez de um dicionario

        self.malha_pontos_perspectiva = None # essa é a malha final (perpectiva e bem formada)
        self.linhas_rasteirizadas = None # total rasteiros
        self.pontos_preenchimento_triangulo = None # todas as linhas que preenchem o modelo

        self.normais_triangulos = None # recebe a normal de cada triandulo na ordem da memoria
        self.normais_vertices = None # armazena as normais de cada um dos vertices armazenados


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
                ponto = matematica_aux.subtrair_matrizes(ponto, foco) # P - C
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

                    if z_atual == -1 or z_atual[0] > aux[2]:
                        self.Z_buffer[aux[0]][aux[1]] = [aux[2], [255,255,255]]
                        
            
                lista_projetada.append(aux)
            self.malha_pontos_perspectiva = lista_projetada
            self.rasteirizacao() # já jera a rasterização
            return self.Z_buffer
        else:
            return -1
    
    def calcula_normais_TRIANGULOS_geral(self):
        faces = self.malha_atual["faces"] # carrega as faces da malha
        
        self.normais_triangulos = [] # inicializa a lista de normais de triangulos
        for face in faces: # loop de faces
            
            # coletando os pontos
            v1 = self.malha_pontos_perspectiva[face[0] - 1]
            v2= self.malha_pontos_perspectiva[face[1] - 1]
            v3 = self.malha_pontos_perspectiva[face[2] - 1]

            normal_triangulo = self.calcula_normal_triangulo(v1, v2, v3)
            self.normais_triangulos.append(normal_triangulo)
        
        self.calcula_normais_VERTICES()
    
    def calcula_normais_VERTICES(self):
        self.normais_vertices = []
        for vertice in range(1, len(self.malha_atual["vertices"]) + 1): # percorre todos os vertices calculando as nmormais deles
            triangulos = operacoes_aux.encontrar_indices_triângulos_do_vértice(vertice, self.malha_atual["faces"])
            
            normal_final_vertice = [0, 0, 0]

            for indice_triangulo in triangulos:
                normal_atual_triangulo = self.normais_triangulos[indice_triangulo]
                normal_final_vertice = matematica_aux.somar_vetores(normal_final_vertice, normal_atual_triangulo)
            
            self.normais_vertices.append(matematica_aux.normaliza_matriz(normal_final_vertice))
        
    def calcula_normal_triangulo(self, v1, v2, v3):
        sub_v2_v1 = matematica_aux.subtrair_matrizes(v2, v1) # calcula a subtração dos vertices 
        sub_v3_v1 = matematica_aux.subtrair_matrizes(v3, v1)
        normal_triangulo = matematica_aux.produto_vetorial(sub_v2_v1, sub_v3_v1) # calcula a normal não normalizada
        
        normal_triangulo_normalizada = matematica_aux.normaliza_matriz(normal_triangulo)  # normaliza a normal do triângulo
        
        return normal_triangulo_normalizada
    
    def calculate_barycentric_coordinates(self, P, P1, P2, P3):
        area_0 = matematica_aux.area_triangulo(P1, P2, P3)
        area_1 = matematica_aux.area_triangulo(P, P1, P2)
        area_2 = matematica_aux.area_triangulo(P, P1, P2)

        alpha = area_1/area_0
        beta = area_2/ area_0
        gamma = 1 - alpha - beta
        
        return alpha, beta, gamma

    def calcula_coordenadas_vista_ponto(self, P, vertices_agora, vertices_antes):
        alpha, beta, gamma = self.calculate_barycentric_coordinates(P, vertices_agora[0], vertices_agora[1], vertices_agora[2])
        aux_alpha = matematica_aux.multiplicar_constante_lista(alpha, vertices_antes[0])
        aux_beta = matematica_aux.multiplicar_constante_lista(beta, vertices_antes[1])
        aux_gamma = matematica_aux.multiplicar_constante_lista(gamma, vertices_antes[2])
        return matematica_aux.somar_vetores(aux_alpha, matematica_aux.somar_vetores(aux_beta, aux_gamma))

    def rasteirizacao(self): # rasteriza a malha

        self.calcula_normais_TRIANGULOS_geral() # antes de gerar os pontos calcula cada uma das normais 

        faces = self.malha_atual["faces"] # carrega as faces da malha
        self.linhas_rasteirizadas = [] # armazena as linhas
        self.pontos_preenchimento_triangulo = [] # armazena o conteudo dos triangulos[]
        
        for face in faces: # loop de faces
            
            # coletando os pontos
            v1 = self.malha_pontos_perspectiva[face[0] - 1]
            v2 = self.malha_pontos_perspectiva[face[1] - 1]
            v3 = self.malha_pontos_perspectiva[face[2] - 1]
            lista_pontos = [v1,v2,v3] # armazena os tres pontos

            # gerando as linhas de cada face
            linhas = []
            linha_a_b = self.linha(v1, v2, lista_pontos, face)
            linhas.append(linha_a_b)

            linha_b_c = self.linha(v2, v3, lista_pontos, face)
            linhas.append(linha_b_c)

            linha_c_a = self.linha(v3, v1, lista_pontos, face)
            linhas.append(linha_c_a)

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
                listra_corte = self.linha(ponto_d, ponto_a_b_c, lista_pontos, face)
                linhas.append(listra_corte)
                self.linhas_rasteirizadas.append(linhas) # adiciona todas as linhas a lista geral

                for id_inicial in range(len(lista_pontos)): # Gera o conteudo
                    if id_inicial != ponto_central: # verificação para impedir que o pondo gerador de D seja levado em consideração
                        ponto_referencia = lista_pontos[id_inicial] # um dos dois casos ou o ponto acima ou o ponto abaixo
                        if ponto_referencia[1] > ponto_a_b_c[1]: # ponto acima
                            
                            linha_1 = self.linha(ponto_referencia, ponto_d, lista_pontos, face) # gera uma linha de apoio entre o ponto d e a referencia 
                            linha_2 = self.linha(ponto_referencia, ponto_a_b_c, lista_pontos, face) # O mesmo
                            
                            y = ponto_referencia[1] # y = o y da referencia 
                            pontos_plot = [] # lista com listas de pontos 
                            linha = [] # lista de po9nto para cada linha
                            
                            while True: # loop principal
                                if y == ponto_d[1]: # trava a rasteirização quando acha o ponto D
                                    break
                                x_lado_1 = linha_1[operacoes_aux.encontrar_lista_por_Y(linha_1, y)] # calcula x_min e x_max
                                x_lado_2 = linha_2[operacoes_aux.encontrar_lista_por_Y(linha_2, y)]
                                linha = self.linha(x_lado_1, x_lado_2, lista_pontos, face)
                                
                                y -= 1 # caso o ponto seja aciam y -= 1
                                pontos_plot.append(linha)
                                self.pontos_preenchimento_triangulo.append(linha)
                        else: # ponto abaixo (restante igual o anterior)
                            linha_1 = self.linha(ponto_referencia, ponto_d, lista_pontos, face) # gera uma linha de apoio entre o ponto d e a referencia 
                            linha_2 = self.linha(ponto_referencia, ponto_a_b_c, lista_pontos, face) # O mesmo
                            
                            y = ponto_referencia[1] # y = o y da referencia 
                            pontos_plot = [] # lista com listas de pontos 
                            linha = [] # lista de po9nto para cada linha
                            
                            while True: # loop principal
                                if y == ponto_d[1]: # trava a rasteirização quando acha o ponto D
                                    break
                                x_lado_1 = linha_1[operacoes_aux.encontrar_lista_por_Y(linha_1, y)] # calcula x_min e x_max
                                x_lado_2 = linha_2[operacoes_aux.encontrar_lista_por_Y(linha_2, y)]
                                linha = self.linha(x_lado_1, x_lado_2, lista_pontos, face)
                                
                                y += 1 # caso o ponto seja aciam y -= 1
                                pontos_plot.append(linha)
                                self.pontos_preenchimento_triangulo.append(linha)

    
    def linha(self, ponto1, ponto2, lista_pontos, face): # gera uma linha
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
                if z_atual == -1 or z_atual[0] > item[2]:
                    

                    self.add_Zbuffer(item, lista_pontos, face)

                    self.Z_buffer[item[0]][item[1]] = [item[2], [255,255,255]]

        return lista

    
    def add_Zbuffer(self, ponto, pontos_novos, face): # muita coisa sksksksksksk
        ponto_em_vista = self.calcula_coordenadas_vista_ponto(ponto, pontos_novos, [self.malha_atual["vertices"][face[0]], self.malha_atual["vertices"][face[1]], self.malha_atual["vertices"][face[2]]]) # encontra o ponto em coordenadas de vista
        alpha, beta, gamma = self.calculate_barycentric_coordinates(ponto_em_vista, pontos_novos[0], pontos_novos[1], pontos_novos[2]) # procura alpha beta e gama

        aux_normal_1 = matematica_aux.multiplicar_constante_lista(alpha, self.normais_vertices[face[0]]) # busca as normais
        aux_normal_2 = matematica_aux.multiplicar_constante_lista(beta, self.normais_vertices[face[1]])
        aux_normal_3 = matematica_aux.multiplicar_constante_lista(gamma, self.normais_vertices[face[2]])
        normal_ponto = matematica_aux.somar_vetores(aux_normal_1, matematica_aux.somar_vetores(aux_normal_2, aux_normal_3)) # cria a normal do ponto
        normal_ponto = matematica_aux.normaliza_matriz(normal_ponto) #normaliza

        V_ponto = matematica_aux.negativar_vetor(ponto_em_vista) # busca V
        V_ponto = matematica_aux.normaliza_matriz(V_ponto) # normaliza

        L_camera = self.iluminacao.procura_L(ponto_em_vista) # busca L
        L_camera = matematica_aux.normaliza_matriz(L_camera) # normaliza

        R_iluminacao = self.iluminacao.calcula_R(normal_ponto, L_camera) # Busca R, ja esta normalizado

        Id = matematica_aux.produto_vetorial(normal_ponto, L_camera)
        Id = matematica_aux.produto_vetorial(Id, self.iluminacao.iluminacao_atual["Kd"])
        Id = matematica_aux.produto_vetorial(Id, self.iluminacao.iluminacao_atual["O"])
        Id = matematica_aux.produto_vetorial(Id, self.iluminacao.iluminacao_atual["Il"]) # carrega e calcula ID componente difusa

        Is = matematica_aux.produto_vetorial(R_iluminacao, V_ponto)
        Is = matematica_aux.elevador_matriz(Is, self.iluminacao.iluminacao_atual["N"][0])
        Is = matematica_aux.multiplicar_constante_lista(self.iluminacao.iluminacao_atual["Ks"][0], Is)
        Is = matematica_aux.produto_vetorial(Is, self.iluminacao.iluminacao_atual["Il"]) # carrega e calcula Is componente especular

        Il = matematica_aux.somar_vetores(Is, self.iluminacao.iluminacao_atual["Iamb"])
        Il = matematica_aux.somar_vetores(Il, Id) # soma de todas para calcular a cr final

        for c in range(len(Il)):
            if Il[c] > 255:
                Il[0] = 255
        
        self.Z_buffer[ponto[0]][ponto[1]] = [ponto[2], Il]

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
    
class Gerenciador_inuminacao:
    def __init__(self) -> None:
        self.diretorio_iluminacao = os.path.dirname(os.path.abspath(__file__)) + "/iliminacoes/"
        self.iluminacao_atual = None
        self.nome_iluminacao_atual = None


    def carregar_iluminacão(self, iluminacao = "iluminacao01"):

        arquivo_iluminacao = self.diretorio_iluminacao + f"{iluminacao}.txt"

        try:  # verifica se o arquivo esta ou não na memoria
            with open(arquivo_iluminacao, 'r') as camera_iluminacao:
                linhas = camera_iluminacao.readlines()
                possiveis_parametros = ['Iamb', 'K', 'Il', 'P', 'Kd', 'O', 'Ks', 'N']
                parametros_iluminacao = {}

                for linha, conterudo in enumerate(possiveis_parametros):  # caso o mesmo esteja, essa parte anexa todos os itens a um dicionario
                    valor = linhas[linha].split() # função magica do python
                    parametros_iluminacao[conterudo] = [float(x) for x in valor]
                
                self.iluminacao_atual = parametros_iluminacao
                self.nome_iluminacao_atual = iluminacao
                return self.iluminacao_atual

        except FileNotFoundError:
            return -1  # Retorna -1 caso o arquivo não seja encontrado
        
    def procura_L(self, ponto):
        return matematica_aux.subtrair_matrizes(self.iluminacao_atual["P"], ponto)
    
    def calcula_R(self, N, L):
        auxiliar = matematica_aux.produto_vetorial(N, L)
        auxiliar = matematica_aux.multiplicar_constante_lista(2, auxiliar)
        auxiliar = matematica_aux.subtrair_matrizes(auxiliar, L)
        return auxiliar
    