import pytest
from G7_Sudoku_ok import G7_Sudoku_ok
from G7_Sudoku_nok import G7_Sudoku_nok

class Teste_7:
    
    def test_solucao_valida_ok(self):
        """Teste com tabuleiro válido - deve passar na implementação ok"""
        s = G7_Sudoku_ok("sudoku_ok.txt")
        assert s.valido()
    
    def test_solucao_invalida_ok(self):
        """Teste com tabuleiro inválido - deve falhar na implementação ok"""
        s = G7_Sudoku_ok("sudoku_nok.txt")
        assert not s.valido()
    
    def test_solucao_valida_nok(self):
        """Teste com tabuleiro válido - deve passar mesmo na implementação nok"""
        s = G7_Sudoku_nok("sudoku_ok.txt")
        assert s.valido()
    
    def test_solucao_invalida_nok(self):
        """Teste com tabuleiro inválido - DEVE FALHAR (defeito da implementação nok)"""
        s = G7_Sudoku_nok("sudoku_nok.txt")
        # Este teste vai falhar porque G7_Sudoku_nok não detecta erros nas subgrades
        assert not s.valido()  # Este assert vai FALHAR!

# Testes básicos de funcionalidade
def test_carregamento_correto():
    """Testa se o tabuleiro é carregado com 9x9"""
    s = G7_Sudoku_ok("sudoku_ok.txt")
    assert len(s.tabuleiro) == 9
    for linha in s.tabuleiro:
        assert len(linha) == 9

def test_elementos_1_a_9():
    """Testa se todos os elementos estão entre 1 e 9"""
    s = G7_Sudoku_ok("sudoku_ok.txt")
    for linha in s.tabuleiro:
        for numero in linha:
            assert 1 <= numero <= 9

# Testes parametrizados para múltiplos cenários
@pytest.mark.parametrize("arquivo,classe,esperado", [
    ("sudoku_ok.txt", G7_Sudoku_ok, True),
    ("sudoku_nok.txt", G7_Sudoku_ok, False),
    ("sudoku_ok.txt", G7_Sudoku_nok, True),
])
def test_combinacoes_tabuleiros(arquivo, classe, esperado):
    """Testa diferentes combinações de tabuleiros e classes"""
    s = classe(arquivo)
    assert s.valido() == esperado

# Fixture para reutilizar instâncias
@pytest.fixture
def sudoku_ok_instance():
    return G7_Sudoku_ok("sudoku_ok.txt")

@pytest.fixture
def sudoku_nok_instance():
    return G7_Sudoku_ok("sudoku_nok.txt")

def test_com_fixtures(sudoku_ok_instance, sudoku_nok_instance):
    """Teste usando fixtures"""
    assert sudoku_ok_instance.valido()
    assert not sudoku_nok_instance.valido()

# Teste que demonstra claramente o defeito
def test_demonstracao_defeito():
    """
    Teste que demonstra o defeito da implementação nok:
    - Se o sudoku_nok.txt tiver erro apenas nas subgrades 3x3
    - A implementação nok vai considerar válido (errado)
    - A implementação ok vai considerar inválido (correto)
    """
    ok = G7_Sudoku_ok("sudoku_nok.txt")
    nok = G7_Sudoku_nok("sudoku_nok.txt")
    
    # Se houver diferença, mostra o defeito
    assert ok.valido() != nok.valido(), "Defeito não detectado - ambas implementações concordam"
    
    # A ok deve ser False (detecta o erro)
    # A nok deve ser True (não detecta o erro nas subgrades)
    print(f"OK: {ok.valido()}, NOK: {nok.valido()}")