from prettytable import PrettyTable
from os import system
import utilitarios

class Prioridades:
    
    def __init__(self, fila = []):
        self.fila = fila
        self.procc_atual = None
        self.concluidos = []
        self.table = PrettyTable()   

    def add_processo(self, procc):
        novo_id = self.auto_increment()
        procc.ID = novo_id
        self.fila.append(procc)
        self.esc_priori()
        self.mostrador()
    
    def esc_priori(self):
        if len(self.fila) > 0:
            for i in self.fila:
                aux = i.CPUtotal * 0.5
                aux += (20 - i.prioridade)
                i.Vl_importancia = aux
            fila_ordenada = sorted(self.fila, key=lambda processo: processo.Vl_importancia)
            self.fila = fila_ordenada[:]
        else: pass
            
    def exe_processo(self):
        if self.procc_atual == None:
            if self.fila == []:
                return -1
            else:
                self.esc_priori()
                self.procc_atual = self.fila[0]
                self.fila.pop(0)
                
        elif self.fila != []:
            self.procc_atual.CPUtotal -= 1
            self.procc_atual.custoTotal += 1
            self.acres_turnaround()
            
            if self.procc_atual.CPUtotal <= 0:
                self.procc_atual.CPUtotal = 0
                self.concluidos.append(self.procc_atual)
                self.procc_atual = self.fila[0]
                self.fila.pop(0)
        
        elif self.fila == []: 
            self.procc_atual.CPUtotal -= 1
            self.procc_atual.custoTotal += 1
            self.acres_turnaround()
            
            if self.procc_atual.CPUtotal <= 0:
                self.procc_atual.CPUtotal = 0
                self.concluidos.append(self.procc_atual)
                return -1
            

    def auto_increment(self):
        max = 0
        for i in self.fila:
            if i.ID > max:
                max = i.ID
        for i in self.concluidos:
            if i.ID > max:
                max = i.ID
        return max+1
    
    def mostrador(self):
        
        if self.procc_atual == None:
            self.exe_processo()
        
        system("cls")
        self.table.clear_rows()
        
        utilitarios.titulo_modlo("Processo a ser executado:")

        self.table.field_names = ["ID", "NOME", "PRIORIDADE", "TEMPO DE CPU", "ORDENADOR", "CUSTO TOTAL", "TURNAROUND"]
        if self.procc_atual == None:
            self.table.add_rows([["","","","","","",""]])
        else:self.table.add_rows([[self.procc_atual.ID, self.procc_atual.nome, self.procc_atual.prioridade, 
                                self.procc_atual.CPUtotal, self.procc_atual.Vl_importancia, self.procc_atual.custoTotal, self.procc_atual.turnaround]])
        
        print(self.table)
        print()
        
        self.table.clear_rows()
        
        utilitarios.titulo_modlo("Processos em fila:")
        self.table.field_names = ["ID", "NOME", "PRIORIDADE", "TEMPO DE CPU", "ORDENADOR", "CUSTO TOTAL", "TURNAROUND"]
        for c in self.fila:
            self.table.add_rows([[c.ID, c.nome, c.prioridade, c.CPUtotal, c.Vl_importancia, c.custoTotal, c.turnaround]])
        print(self.table)
        
        self.mostrador_concluidos()
        
        prox = input("Aperte enter para retornar: ")
    
    def mostrador_sequencial(self):

        while True:
            
            test = self.exe_processo()
            
            if test == -1:
                system("cls")
                self.mostrador_concluidos()
                self.procc_atual = None
                utilitarios.titulo_modlo(f"O tempo médio de espera de todos os processos foi de: {self.concluidos[-1].turnaround/len(self.concluidos)}")
                prox = input("Aperte para retornar ao menu: ")
                return 1
            
            system("cls")
            
            self.table.clear_rows()
            
            utilitarios.titulo_modlo("Processo em execução atualmente:")
            self.table.field_names = ["ID", "NOME", "PRIORIDADE", "TEMPO DE CPU", "ORDENADOR", "CUSTO TOTAL", "TURNAROUND"]
            self.table.add_rows([[self.procc_atual.ID, self.procc_atual.nome, self.procc_atual.prioridade, 
                                self.procc_atual.CPUtotal, self.procc_atual.Vl_importancia, self.procc_atual.custoTotal, self.procc_atual.turnaround]])
            print(self.table)
            print()
            
            self.table.clear_rows()
            
            utilitarios.titulo_modlo("Processos em fila:")
            self.table.field_names = ["ID", "NOME", "PRIORIDADE", "TEMPO DE CPU", "ORDENADOR", "CUSTO TOTAL", "TURNAROUND"]
            for c in self.fila:
                self.table.add_rows([[c.ID, c.nome, c.prioridade, c.CPUtotal, c.Vl_importancia, c.custoTotal, c.turnaround]])
            print(self.table)

            self.table.clear_rows()
            
            self.mostrador_concluidos()
            
            prox = input("Aperte enter para continuar ou p para parar: ").upper()
            
            if prox == "P":
                return 1
            else:
                continue
            
    def mostrador_concluidos(self):
        
        self.table.clear_rows()
        
        utilitarios.titulo_modlo("Processos concluidos:")
        self.table.field_names = ["ID", "NOME", "PRIORIDADE", "TEMPO DE CPU", "ORDENADOR", "CUSTO TOTAL", "TURNAROUND"]

        if self.concluidos == []:
            self.table.add_rows([["","","","","","",""]])
        else:
            for c in self.concluidos:
                self.table.add_rows([[c.ID, c.nome, c.prioridade, c.CPUtotal, c.Vl_importancia, c.custoTotal, c.turnaround]])
        
        print(self.table)
        
        self.table.clear_rows()
        
    def acres_turnaround(self):
        self.procc_atual.turnaround += 1
        for i in self.fila:
            i.turnaround += 1
        