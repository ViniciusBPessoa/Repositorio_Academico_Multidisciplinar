# Jogo da Velha

Lógica do jogo da velha em Python, na classe `jogo_velha` (`jogo/jogo_velha.py`).

## Métodos

| Método | O que faz |
|---|---|
| `victory_checker()` | verifica se algum jogador venceu (linhas, colunas e diagonais) |
| `stap(location, player)` | faz uma jogada numa posição do tabuleiro (de 1 a 9); `player` é o número do jogador (1 ou 2) |
| `reset(players)` | reinicia o tabuleiro |

O tabuleiro é uma lista de 9 posições, em que `'N'` representa uma casa vazia. O final do arquivo tem alguns testes simples da classe.

> **Status:** só a lógica. O `main.py`, que teria o laço do jogo e a interface, ainda está vazio.

## Como executar os testes

```bash
python jogo/jogo_velha.py
```

## Tecnologias

Python
