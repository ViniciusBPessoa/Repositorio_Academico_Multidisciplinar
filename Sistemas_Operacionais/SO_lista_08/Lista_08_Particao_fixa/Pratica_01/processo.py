class Processo:
    def __init__(self, ID, nome, custoCPU, tamanho):
        self.ID = ID
        self.nome = nome
        self.custoCPU = custoCPU
        self.tamanho = tamanho
        self.espacos_memoria = []
        self.local_memoria = "Memoria_p"
