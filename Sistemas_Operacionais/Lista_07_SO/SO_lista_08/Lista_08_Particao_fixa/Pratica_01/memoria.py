import utilitarios
import math

class Memoria:
    def __init__(self, tamanho_max, tamanho_particoes):
        self.tamanho_max = tamanho_max
        self.tamanho_particoes = tamanho_particoes
        self.particoes = [] # [TAMANHO TOTAL DA PARTIÇÃO, OCUPADO, PROCESSO CONTIDO, TAMANHO OCUPADO]
        self.ponteiro = 0
        self.memoria_secundaria = []
        self.inicializador_particao()

    def inicializador_particao(self):
        for i in range(0, self.tamanho_max//self.tamanho_particoes): # Com base na quantidade de partições
            self.particoes.append([self.tamanho_particoes, False, None, None]) # Instancia partições com apenas memória disponível

    def remove_processo(self, list):
            for l in list: # Checa para cada index da lista
                self.particoes[l][1] = False
                self.particoes[l][2].espacos_memoria = []
                self.particoes[l][2] = None
                self.particoes[l][3] = None

    def checa_particao_livre(self, alg=0):
        if alg == 1: self.ponteiro = 0 # 1 = first_fit, não leva em consideração o ponteiro

        if self.ponteiro >= (self.tamanho_max//self.tamanho_particoes):
            self.ponteiro = 0

        for i in range(self.ponteiro, len(self.particoes)):
            if self.particoes[i][1] == False:
                break
            self.ponteiro += 1

        if self.ponteiro >= (self.tamanho_max//self.tamanho_particoes):
            self.ponteiro = 0

    def aloca_processo(self, processo, alg):
        tamanho_processo = processo.tamanho
        if tamanho_processo > self.tamanho_max: # Checa se o tamanho do processo é maior que o tamanho total da memória
            return False # Espaço insuficiente!!!

        for i in range(0, math.ceil(processo.tamanho/self.tamanho_particoes)): # Calculo para checagem de quantas vezes terá que ser alocado nas partições de acordo com o tamanho
            if alg == "First-fit": self.checa_particao_livre(1) # Ignora o ponteiro, insere a partir da primeira posição
            if alg == "Next-fit": self.checa_particao_livre() # Leva em consideração o ponteiro, inserindo a partir de onde o último processo foi alocado 

            self.particoes[self.ponteiro][1] = True # Marca como partição ocupada
            self.particoes[self.ponteiro][2] = processo # Salvao processo na partição
            
            if tamanho_processo > self.tamanho_particoes: # Verifica se o tamanho do processo é maior que o que cabe na partiçãp
                self.particoes[self.ponteiro][3] = self.tamanho_particoes # Caso sim salva o espaço total necessário para encher a partição
                tamanho_processo -= self.tamanho_particoes # E subtrai do valor total do espaço para o valor restante
            else: self.particoes[self.ponteiro][3] = tamanho_processo # Caso não salva o tamanho restante do processo na partição
            
            self.particoes[self.ponteiro][2].espacos_memoria.append(self.ponteiro) # Salva no processo em que posição da memória ele ta

    def tamanho_livre(self):
        aux = 0
        for k in self.particoes:
            if k[1] == True: # Verifica se a partição tem algo
                aux += self.tamanho_particoes # E pega o tamanho total da partição

        tamanho_livre = self.tamanho_max - aux # Calcula então o tamanho total da memória - tamanho de partições ocupadas

        return tamanho_livre

    def swapping(self, processo):
        processo.local_memoria = "Memoria_s"
        self.memoria_secundaria.append([processo.ID, processo.tamanho][:]) # Adiciona o processo à memória secundária
        self.remove_processo(processo.espacos_memoria) # Remove o processo da principal

    def remove_secundaria(self, id):
        for i in range(len(self.memoria_secundaria)):
            if self.memoria_secundaria[i][0] == id:
                self.memoria_secundaria.pop(i)

    def to_string(self):
        utilitarios.titulo_modelo("MEMÓRIA ATUAL")

        print("Tamanho máximo da memória: ", self.tamanho_max)
        print("Tamanho por partição: ", self.tamanho_particoes)

        print("\nAs partições atualmente estão assim:")
        for i in range(0, self.tamanho_max//self.tamanho_particoes):
            texto = ""
            if self.particoes[i][1] == True: texto = "OCUPADA"
            else: texto = "LIVRE"
            print(f"A partição {i} está {texto}.")
            try: print(f"O processo contido na partição: {self.particoes[i][2].nome}.")
            except: print("Não há processo contido na partição")
            print(f"Está sendo ocupada por um tamanho de: {self.particoes[i][3]}.")
            try: 
                if self.particoes[i][3] < self.tamanho_particoes: print("Há fragmentação Interna.")
            except: print("Não há fragmentação Interna")
            print()


        utilitarios.titulo_modelo("MEMÓRIA SECUNDÁRIA")
        
        print(self.memoria_secundaria)