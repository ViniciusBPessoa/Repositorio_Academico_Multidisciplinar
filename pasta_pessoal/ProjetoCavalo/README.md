# Passeio do Cavalo (Knight's Tour)

Resolve o **Passeio do Cavalo**, em que o cavalo do xadrez tenta visitar o maior número possível de casas do tabuleiro sem repetir nenhuma.

## Como funciona

A classe `Tabuleiro` (`Tabuleiro.py`):

- Representa o tabuleiro 8×8 como uma lista, em que `0` é casa vazia, `1` é a posição atual do cavalo e `2` é casa já visitada.
- Começa numa posição inicial informada ou sorteada.
- A cada jogada, lista os movimentos válidos do cavalo e usa uma **busca prospectiva**: faz simulações aleatórias das jogadas seguintes até uma profundidade configurável (`profundidade_prospectiva`, 3 por padrão) para escolher o movimento mais promissor.
- `jogar_partida_completa()` joga até não haver mais movimentos e retorna a pontuação, que é o número de casas visitadas.

## Como usar

O `Main.py` ainda está vazio. O próprio `Tabuleiro.py` roda uma demonstração no final do arquivo (`python Tabuleiro.py`). Para usar a classe em outro código:

```python
from Tabuleiro import Tabuleiro

jogo = Tabuleiro(tamanho_tabuleiro=8, profundidade_prospectiva=3)
print(jogo.jogar_partida_completa())
```

## Tecnologias

Python
