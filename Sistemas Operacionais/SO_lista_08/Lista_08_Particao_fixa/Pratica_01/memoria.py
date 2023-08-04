import random

class Memoria:
    def __init__(self, tamanho_max, tamanho_particoes):
        self.tamanho_max = tamanho_max
        self.tamanho_particoes = tamanho_particoes
        self.particoes = [] # [TAMANHO TOTAL DA PARTIÇÃO, OCUPADO, PROCESSO CONTIDO]
        self.ponteiro = 0
        self.memoria_secundaria = []

    def inicializador_particao(self):
        for i in range(0, self.tamanho_particoes//self.tamanho_particoes): # Com base na quantidade de partições
            self.particoes.append([self.tamanho_particoes, False, None]) # Instancia partições com apenas memória disponível

    def alocar_processo(self, alg, processo):
        match alg:
            case 1: # first-fit
                self.first_fit(processo)
            case 2: # next-fit
                self.next_fit(processo)
            case _:
                pass

    def remove_processo(self, list):
            for l in list: # Checa para cada index da lista
                posicao = self.particoes.index(l)
                self.particoes[posicao].espacos_memoria = []
                self.particoes[posicao][1] = False
                self.particoes[posicao][2] = None

    def checa_particao_livre(self):
        self.ponteiro = 0
        for p in self.particoes:
            if p[self.ponteiro][1] == False:
                self.ponteiro += 1

    def first_fit(self, processo):
        self.ponteiro = 0
        for p in self.particoes: # Checa cada partição
            if p[self.ponteiro][1] == False: # Checa se a partição vigente está ocupada
                for i in range(0, ((self.particoes[self.ponteiro].tamanho // self.tamanho_particoes)+1)+1): # Calculo para checagem de quantas vezes terá que ser alocado nas partições de acordo com o tamanho
                    self.particoes[self.ponteiro][1] = True 
                    self.particoes[self.ponteiro][2] = processo
                    self.particoes[self.ponteiro].espacos_memoria.append(self.ponteiro)
                    for p2 in self.particoes

            self.ponteiro += 1 # Incrementa ponteiro apontando pra próxima partição

    def first_fit(self, processo):
        self.ponteiro = 0
        for p in self.particoes: # Checa cada partição
            if p[self.ponteiro][1] == False: # Checa se a partição vigente está ocupada
                for i in range(0, ((self.particoes[self.ponteiro].tamanho // self.tamanho_particoes)+1)+1): # Calculo para checagem de quantas vezes terá que ser alocado nas partições de acordo com o tamanho
                    prox_particao = self.checa_particao_livre()
                    self.particoes[self.prox_particao][1] = True 
                    self.particoes[self.prox_particao][2] = processo
                    self.particoes[self.prox_particao].espacos_memoria.append(self.prox_particao)


    def next_fit(self, processo):
        for p in self.particoes: # Checa cada partição
            if p[self.ponteiro][1] == False:  # Checa se a partição vigente está ocupada, começando a checar a partir da última partição escolhida
                self.particoes[self.ponteiro][1] = True
                self.particoes[self.ponteiro][2] = processo
            self.ponteiro += 1 # Incrementa ponteiro apontando pra próxima partição

        if self.ponteiro >= range(0, self.tamanho_particoes//self.tamanho_particoes):
            self.ponteiro = 0
