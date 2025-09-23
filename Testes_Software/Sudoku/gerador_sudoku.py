from sudoku import Sudoku
import random

class Tabuleiros():
    def __init__(self, is_defective = False):

        if not is_defective:
            self.tabuleiro = self.gerador_tabuleiro_sudoku()
        else:
            self.tabuleiro = self.gerador_tabuleiro_sudoku_nok()

    def gerador_tabuleiro_sudoku(self, seed = None):
        if seed == None:
            seed = random.seed()

        tabuleiro = Sudoku(3, seed = seed).solve().board()
        return tabuleiro
    
    def gerador_tabuleiro_sudoku_nok(self):
        tabuleiro = self.gerador_tabuleiro_sudoku()
        tabuleiro[0][0], tabuleiro[0][1] = tabuleiro[0][1], tabuleiro[0][0]
        return tabuleiro