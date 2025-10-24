from sudoku import Sudoku
from random import randint

class GeradorSudoku():
    def __init__(self, name: str, is_defective: bool = False):
        if not is_defective:
            self.tabuleiro = self.gerador_tabuleiro_sudoku()
        else:
            self.tabuleiro = self.gerador_tabuleiro_sudoku_nok()
        
        self.salvar_tabuleiro(name)

    def gerador_tabuleiro_sudoku(self, seed=None):
        if seed is None:
            seed = randint(0, 2**64)
        
        puzzle = Sudoku(3, seed=seed).solve()
        # Garantir que não há células vazias
        tabuleiro = [[cell for cell in row] for row in puzzle.board]
        return tabuleiro
    
    def gerador_tabuleiro_sudoku_nok(self):
        tabuleiro = self.gerador_tabuleiro_sudoku()
        # Criar um defeito óbvio: duplicar um número na mesma linha
        tabuleiro[0][0] = tabuleiro[0][1]
        return tabuleiro
    
    def salvar_tabuleiro(self, arquivo):
        with open(arquivo, 'w') as f:
            for linha in self.tabuleiro:
                # Usar espaço simples (formato MiniZinc)
                f.write(' '.join(map(str, linha)) + '\n')


# Exemplo de uso:

Sudoku_ok = GeradorSudoku("sudoku_ok.txt", is_defective = False)
Sudoku_nok = GeradorSudoku("sudoku_nok.txt", is_defective = True)
