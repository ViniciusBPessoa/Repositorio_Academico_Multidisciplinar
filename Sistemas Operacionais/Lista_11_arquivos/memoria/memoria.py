class Memoria:
    def __init__(self, tamanhp_t, tamanho_i) -> None:
        self.memoria = []
        self.tamanho_total = tamanhp_t
        self.tamanho_bloco = tamanho_i
        self.inicializador_memoria()
        
    def inicializador_memoria(self):
        aux = self.tamanho_total // self.tamanho_bloco
        
        for c in range(0, aux):
            self.memoria.append(None)
            