from prettytable import PrettyTable
import Ajudadores.utilitarios as utilitarios
class Memoria:
    def __init__(self, tamanhp_t, tamanho_i) -> None:
        self.memoria = []
        self.tamanho_total = tamanhp_t
        self.tamanho_bloco = tamanho_i
        self.inicializador_memoria()
        self.table = PrettyTable()
        
    def inicializador_memoria(self):
        aux = self.tamanho_total // self.tamanho_bloco
        
        for c in range(0, aux):
            self.memoria.append(None)
    
    def adicionar_memoria(self, item):
        
        verificador = False
        localizador = 0
        aux_tam = item.tamanho
        
        
        for c in self.memoria:
            if c != None:
                localizador = len(self.memoria) - self.memoria[::-1].index(c)
                verificador = False
                aux_tam = item.tamanho
            elif aux_tam == 0:
                verificador = True
                break
            else:
                if aux_tam <= self.tamanho_bloco:
                    verificador = True
                    break
                else:
                    aux_tam -= self.tamanho_bloco
        
        if verificador == False:
            self.desquebrar() 
            verificador = False
            localizador = 0
            aux_tam = item.tamanho
            
            
            for c in self.memoria:
                if c != None:
                    localizador = len(self.memoria) - self.memoria[::-1].index(c)
                    verificador = False
                    aux_tam = item.tamanho
                elif aux_tam == 0:
                    verificador = True
                    break
                else:
                    if aux_tam <= self.tamanho_bloco:
                        verificador = True
                        break
                    else:
                        aux_tam -= self.tamanho_bloco
        
        if verificador == True:
            aux_tam = item.tamanho
            while True:
                if aux_tam <= self.tamanho_bloco:
                    self.memoria[localizador] = (item, aux_tam)
                    break
                
                else:
                    aux_tam -= self.tamanho_bloco
                    self.memoria[localizador] = (item, self.tamanho_bloco)
                    
                localizador += 1
        
        return verificador
               
    def remover_memoria(self, dado):
        
        nome_classe = dado.__class__.__name__
        if nome_classe == "Diretorio":
            if len(dado.arquivos) > 0:
                for c in dado.arquivos:
                    self.remover_memoria(c)
        
        itens_removiveis = []
        for c in self.memoria:
            if c != None:
                if c[0] == dado:
                    itens_removiveis.append(c)
        
        for c in itens_removiveis:
            posi = self.memoria.index(c)
            self.memoria[posi] = None
    
    def desquebrar(self):
        nova_memoria = []
        
        for x in self.memoria:
            if x != None:
                nova_memoria.append(x)
        
        aux = len(self.memoria)
        
        aux = aux - len(nova_memoria)
        
        for c in range(0, aux):
            nova_memoria.append(None)
            
        self.memoria = nova_memoria[:]
    
    def printar(self):

        utilitarios.titulo_modelo("Estado atual da memória")
        
        self.table.clear_rows()
        self.table.field_names = ["ID", "Nome do item", "Oculpado", "Fragmentação interna?", "espaço"]
        
        posicao = 1
        
        for x in self.memoria:
            if x == None:
                self.table.add_rows([[posicao, "vazio", "vazio", "Não", f"0/{self.tamanho_bloco}"]])
            
            else:
                
                if x[1] != self.tamanho_bloco:
                    self.table.add_rows([[posicao, x[0].nome, "Sim", "Sim", f"{x[1]}/{self.tamanho_bloco}"]])
                
                else:
                    self.table.add_rows([[posicao, x[0].nome, "Sim", "Não", f"{self.tamanho_bloco}/{self.tamanho_bloco}"]])
            
            posicao += 1

        print(self.table)
        self.table.clear_rows()
        
        var = False
        jesus = False
        
        for c in self.memoria:
            if c == None:
                var = True
            if c != None and var == True:
                jesus = True
                
    
        utilitarios.titulo_modelo(f"Essa memoria possui fragmentação externa? {jesus}")
            
