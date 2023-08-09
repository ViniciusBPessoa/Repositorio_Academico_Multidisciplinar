from prettytable import PrettyTable
import Ajudadores.utilitarios as utilitarios

class Diretorio:
    def __init__(self, nome, pai) -> None:
        self.nome = "/" + nome
        self.arquivos = []
        self.tamanho = self.caucula_tamanho()
        self.pai = pai
        self.table = PrettyTable()
        
    def caucula_tamanho(self):
        aux = 0
        if len(self.arquivos) > 0:
            for x in self.arquivos:
                aux += x.tamanho

        return aux

    def listar_itens(self):
        
        self.table.clear_rows()
        utilitarios.titulo_modelo("Itens na pasta")
        self.table.field_names = ["Posição", "Nome", "Tipo", "Tamanho"]
        
        if len(self.arquivos) == 0:
            self.table.add_rows([["", "","",""]])
        
        else:
            posi = 1
            for x in self.arquivos:
                
                nome_classe = x.__class__.__name__
                
                self.table.add_rows([[posi, x.nome[1:], nome_classe, x.tamanho]])
                posi += 1
            
        print(self.table)
        self.table.clear_rows()
        
    
    def listar_diretorios(self):
        verificador = 0
        self.table.clear_rows()
        utilitarios.titulo_modelo("Itens na pasta")
        self.table.field_names = ["Posição", "Nome", "Tipo", "Tamanho"]
        
        numero_pastas = 0
        if len(self.arquivos) > 0:
            for x in self.arquivos:
                    if x.__class__.__name__ == "Diretorio":
                        numero_pastas += 1
        
        if len(self.arquivos) == 0:       
            self.table.add_rows([["", "","",""]])
            verificador = -1
        
        else:
            
            if numero_pastas != 0:
                posi = 1
                
                for x in self.arquivos:
                    
                    nome_classe = x.__class__.__name__
                    
                    if nome_classe == "Diretorio":
                    
                        self.table.add_rows([[posi, x.nome[1:], nome_classe, x.tamanho]])
                        posi += 1

                verificador = posi
                
            else:
                self.table.add_rows([["", "","",""]])
                verificador = -1
            
        print(self.table)
        self.table.clear_rows()
        return verificador
        
    def adicionar_diretorio(self, nome):
        
        self.arquivos.append(Diretorio(nome, self))
        
    def retorna_diretorio(self, posição):
        posi = 1
        
        for x in self.arquivos:
            if x.__class__.__name__ == "Diretorio":
                if posi == posição:
                    return x
                else:
                    posi += 1
    
    def adiciona_arquivo(self, arquivo):
        self.arquivos.append(arquivo)
        self.atualiza_tamanho_geral()
    
    def atualiza_tamanho_geral(self):
        aux = self
        
        while True:
            if aux.pai == None:
                break
            aux.tamanho = aux.caucula_tamanho()
            aux = aux.pai
            
    def remover_arquivo(self, item):
        item -= 1
        self.arquivos.pop(item)
        self.atualiza_tamanho_geral()
        