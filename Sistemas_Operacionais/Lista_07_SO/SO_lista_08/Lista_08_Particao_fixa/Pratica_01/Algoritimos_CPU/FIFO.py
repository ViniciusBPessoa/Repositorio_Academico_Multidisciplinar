from prettytable import PrettyTable
import processo
import utilitarios

class FIFO:
    def __init__(self) -> None:
        
        self.processos = []
        self.em_execucao = None
        self.table = PrettyTable() 
        self.id_part = 1
    
    def add_proc(self, nome, custoCPU, tamanho):
    
        proc = processo.Processo(self.id_part, nome, custoCPU, tamanho)
        self.id_part += 1
        self.processos.append(proc)
    
    def cosumidor(self):
        if self.em_execucao == None:
            if len(self.processos) >= 1:
                self.em_execucao = self.processos[0]
                self.processos.pop(0)
                return 2
            else:
                return 1
        
        else:
            self.em_execucao.custoCPU -= 1
            
            if self.em_execucao.custoCPU == 0:
                aux = self.em_execucao.espacos_memoria
                self.em_execucao = None
                return aux
            else:
                return 1
    
    def to_string(self):
        
        self.table.clear_rows()
        utilitarios.titulo_modelo("Processo em execução")
        self.table.field_names = ["ID", "Nome", "Custo de CPU", "Tamanho", "Espacos da Memoria"]
        
        if self.em_execucao == None:
            self.table.add_rows([["","","","",""]])
        
        else:
            self.table.add_rows([[str(self.em_execucao.ID), self.em_execucao.nome, self.em_execucao.custoCPU, self.em_execucao.tamanho, self.em_execucao.espacos_memoria]])

        print(self.table)
        
        self.table.clear_rows()
        
        utilitarios.titulo_modelo("Processos na Fila")
        self.table.field_names = ["ID", "Nome", "Custo de CPU", "Tamanho", "Espacos da Memoria"]
        
        
        if self.processos == []:
            self.table.add_rows([["","","","",""]])
        
        else:
            for c in self.processos:
                self.table.add_rows([[str(c.ID), c.nome, c.custoCPU, c.tamanho, c.espacos_memoria]])

        print(self.table)
        self.table.clear_rows()