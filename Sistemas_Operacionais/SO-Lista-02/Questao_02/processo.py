
class Processo:
    def __init__(self, ID, nome, prioridade, CPUtotal) -> None:
        self.ID = ID
        self.nome = nome
        self.prioridade = prioridade
        self.CPUtotal = CPUtotal                                         #Equivalente a CPU BURST nesse caso de simulação
        self.Vl_importancia = 0
        self.custoTotal = 0
        self.turnaround = 0
