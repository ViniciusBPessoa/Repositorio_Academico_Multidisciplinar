# Testes de Software: Verificador de Sudoku (Grupo 7)

Atividade em grupo da disciplina de **Testes de Software**. O objetivo é mostrar como uma suíte de testes encontra um defeito, comparando duas implementações de um verificador de Sudoku:

- **`G7_Sudoku_ok`**: implementação correta. Verifica linhas, colunas e as subgrades 3×3.
- **`G7_Sudoku_nok`**: implementação com um **defeito proposital**. Não verifica as subgrades 3×3, então um tabuleiro com erro só nas subgrades passaria como válido.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `G7_Sudoku_ok.py` | verificador correto |
| `G7_Sudoku_nok.py` | verificador com defeito |
| `GeradorSudoku.py` | gera um tabuleiro válido e um inválido (com a biblioteca `py-sudoku`) e salva em `.txt` |
| `sudoku_ok.txt` / `sudoku_nok.txt` | tabuleiros de teste (válido e inválido) |
| `Teste_7.py` | suíte de testes com pytest |

## Os testes

A suíte `Teste_7.py` tem:

- testes das duas implementações com o tabuleiro válido e com o inválido;
- testes básicos de carregamento (tabuleiro 9×9, números de 1 a 9);
- testes parametrizados com várias combinações de tabuleiro e implementação;
- testes com *fixtures*;
- um teste que demonstra o defeito.

Os testes foram pensados para **passar na versão correta e falhar na versão com defeito**. Com os tabuleiros atuais, porém, o `sudoku_nok.txt` gerado também tem um número repetido numa linha, então as duas implementações o rejeitam. O resultado é que 10 dos 11 testes passam, e só o `test_demonstracao_defeito` falha, porque as duas versões concordam. Para evidenciar o defeito, o tabuleiro inválido precisa ter erro **apenas** nas subgrades 3×3.

## Como executar

```bash
pip install pytest py-sudoku
python GeradorSudoku.py     # (opcional) gera novos tabuleiros
pytest Teste_7.py -v
```

O arquivo de testes não segue o padrão `test_*.py`, por isso é preciso passar o nome dele para o pytest.

## Tecnologias

Python · pytest · py-sudoku
