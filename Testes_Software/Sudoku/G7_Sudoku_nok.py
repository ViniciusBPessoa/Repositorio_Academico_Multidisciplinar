class G7_Sudoku_nok:
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
        # IMPLEMENTAÇÃO COM DEFEITO: não verifica subgrades 3x3
        # Verificar linhas
        for i in range(9):
            if len(set(self.tabuleiro[i])) != 9:
                return False
        
        # Verificar colunas
        for j in range(9):
            coluna = [self.tabuleiro[i][j] for i in range(9)]
            if len(set(coluna)) != 9:
                return False
        
        # DEFEITO: Não verifica as subgrades 3x3!
        # Um tabuleiro com erro apenas nas subgrades passará como válido
        
        return True