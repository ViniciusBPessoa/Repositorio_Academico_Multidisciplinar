class G1_Sudoku_ok:
    def __init__(self, arquivo):
        self.tabuleiro = self.carregar_tabuleiro(arquivo)
    
    def carregar_tabuleiro(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
        
        tabuleiro = []
        for linha in linhas:
            if linha.strip():
                numeros = [int(x) for x in linha.split()]
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


class G1_Sudoku_nok:
    def __init__(self, arquivo):
        self.tabuleiro = self.carregar_tabuleiro(arquivo)
    
    def carregar_tabuleiro(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
        
        tabuleiro = []
        for linha in linhas:
            if linha.strip():
                numeros = [int(x) for x in linha.split()]
                tabuleiro.append(numeros)
        
        return tabuleiro
    
    def valido(self):
        # Verificar linhas (OK)
        for i in range(9):
            if len(set(self.tabuleiro[i])) != 9:
                return False
        
        # Verificar colunas (OK)
        for j in range(9):
            coluna = [self.tabuleiro[i][j] for i in range(9)]
            if len(set(coluna)) != 9:
                return False
        
        # DEFEITO: Não verifica as regiões 3x3
        # (código comentado propositalmente)
        # for regiao_i in range(3):
        #     for regiao_j in range(3):
        #         regiao = []
        #         for i in range(3):
        #             for j in range(3):
        #                 regiao.append(self.tabuleiro[regiao_i*3 + i][regiao_j*3 + j])
        #         if len(set(regiao)) != 9:
        #             return False
        
        return True