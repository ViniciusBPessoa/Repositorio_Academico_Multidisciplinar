import pytest
from sudokuVerificator import G7_Sudoku_ok, G7_Sudoku_nok

def test_solucao_valida_ok():
    s = G7_Sudoku_ok("sudoku_ok.txt")
    assert s.validacao() is True   # deve passar, tabuleiro válido

def test_solucao_invalida_ok():
    s = G7_Sudoku_ok("sudoku_nok.txt")
    assert s.validacao() is False  # deve passar, tabuleiro inválido

def test_solucao_valida_nok():
    s = G7_Sudoku_nok("sudoku_ok.txt")
    assert s.validacao() is True   # passa porque está certo

def test_solucao_invalida_nok():
    s = G7_Sudoku_nok("sudoku_nok.txt")
    # A classe NOK tem defeito: ela não valida as regiões 3x3
    # Portanto, pode acabar aceitando tabuleiro inválido
    # Esse teste deve FALHAR -> é o esperado na atividade
    assert s.validacao() is False
