import processo

class FIFO:
    def __init__(self) -> None:
        
        self.processos = []
        self.em_execucao = None
    
    def add_proc(self, nome, custoCPU, tamanho):
        proc = processo.Processo(len(self.processos) + 1, nome, custoCPU, tamanho)
        self.processos.append(proc)
    
    def cosumidor(self):
        if self.em_execucao != None:
            if len(self.processos) >= 1:
                self.em_execucao = self.processos[0]
                self.processos.pop(0)
            else:
                return 1
        
        else:
            self.em_execucao.custoCPU -= 1
            
            if self.em_execucao.custoCPU == 0:
                self.em_execucao = None
                return self.processos[0].espacos_memoria

