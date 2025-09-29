from sudoku import Sudoku
from random import randint

class GeradorSudoku():
    def __init__(self, name : str, is_defective : bool = False):

        if not is_defective:
            self.tabuleiro = self.gerador_tabuleiro_sudoku()
        else:
            self.tabuleiro = self.gerador_tabuleiro_sudoku_nok()

        self.salvar_tabuleiro(name)

    def gerador_tabuleiro_sudoku(self, seed = None):
        if seed == None:
            seed = randint(0, 2**64)
            print(f"Seed: {seed}")

        tabuleiro = Sudoku(3, seed = seed).solve().board
        return tabuleiro
    
    def gerador_tabuleiro_sudoku_nok(self):
        tabuleiro = self.gerador_tabuleiro_sudoku()
        tabuleiro[0][0], tabuleiro[0][1] = tabuleiro[0][1], tabuleiro[0][0]
        return tabuleiro
    
    def salvar_tabuleiro(self, arquivo):
        with open(arquivo, 'w') as f:
            for linha in self.tabuleiro:
                f.write(', '.join(map(str, linha)) + '\n')