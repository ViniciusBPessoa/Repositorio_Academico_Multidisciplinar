class G7_Sudoku_ok:
    def __init__(self, arquivo):
        self.tabuleiro = self.carregar_tabuleiro(arquivo)
        
    def carregar_tabuleiro(self, arquivo):
        tabuleiro = []
        with open(arquivo, 'r') as f:
            for linha in f:
                numeros = [int(x) for x in linha.strip().split()]
                tabuleiro.append(numeros)
        return tabuleiro
    
    def valido(self):
        # Verificar linhas
        for i in range(9):
            if len(set(self.tabuleiro[i])) != 9:
                return False
        
        # Verificar colunas
        for j in range(9):
            coluna = [self.tabuleiro[i][j] for i in range(9)]
            if len(set(coluna)) != 9:
                return False
        
        # Verificar subgrades 3x3
        for bloco_i in range(3):
            for bloco_j in range(3):
                subgrade = []
                for i in range(3):
                    for j in range(3):
                        subgrade.append(self.tabuleiro[bloco_i*3 + i][bloco_j*3 + j])
                if len(set(subgrade)) != 9:
                    return False
        
        return True