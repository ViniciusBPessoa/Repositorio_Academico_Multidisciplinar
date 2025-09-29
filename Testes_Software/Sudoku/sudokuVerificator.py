class G7_Sudoku_ok:
    def __init__(self, arquivo):
        self.tabuleiro = self.carregar_tabuleiro(arquivo)
    
    def carregar_tabuleiro(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
        
        tabuleiro = []
        for linha in linhas:
            if linha.strip():
                numeros = [int(x.strip()) for x in linha.split(",")]
                tabuleiro.append(numeros)
        return tabuleiro
    
    def validacao(self):    
        # Verificar linhas
        for linha in self.tabuleiro:
            if len(set(linha)) != 9:
                return False
        
        # Verificar colunas
        for j in range(9):
            coluna = [self.tabuleiro[i][j] for i in range(9)]
            if len(set(coluna)) != 9:
                return False
        
        # Verificar regiões 3x3
        for regiao_i in range(3):
            for regiao_j in range(3):
                regiao = []
                for i in range(3):
                    for j in range(3):
                        regiao.append(self.tabuleiro[regiao_i*3 + i][regiao_j*3 + j])
                if len(set(regiao)) != 9:
                    return False
        
        return True


class G7_Sudoku_nok:
    def __init__(self, arquivo):
        self.tabuleiro = self.carregar_tabuleiro(arquivo)
    
    def carregar_tabuleiro(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
        
        tabuleiro = []
        for linha in linhas:
            if linha.strip():
                # Mesmo ajuste para as vírgulas
                numeros = [int(x.strip()) for x in linha.split(",")]
                tabuleiro.append(numeros)
        
        return tabuleiro
    
    def validacao(self):    
        # Verificar linhas
        for linha in self.tabuleiro:
            if len(set(linha)) != 9:
                return False
        
        # Verificar colunas
        for j in range(9):
            coluna = [self.tabuleiro[i][j] for i in range(9)]
            if len(set(coluna)) != 9:
                return False
        
        # Verificar regiões 3x3
        for regiao_i in range(3):
            for regiao_j in range(3):
                regiao = []
                for i in range(3):
                    for j in range(3):
                        regiao.append(self.tabuleiro[regiao_i*3 + i][regiao_j*3 + j])
                if len(set(regiao)) != 9:
                    return False
        
        return True

teste_ai = G7_Sudoku_ok("sudoku_ok.txt")