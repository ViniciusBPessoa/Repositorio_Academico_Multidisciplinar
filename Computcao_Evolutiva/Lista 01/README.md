# Lista 01: Algoritmos Genéticos

Lista de exercícios da disciplina de **Computação Evolutiva**, com problemas clássicos resolvidos por algoritmos genéticos.

## Notebooks

### `questao01.ipynb`: Problema das 8 Rainhas

Algoritmo genético implementado do zero para posicionar 8 rainhas num tabuleiro 8×8 sem que nenhuma ataque outra. O notebook traz as funções de criação da população, de fitness (pares de rainhas que não se atacam, com máximo de 28), de seleção e de mutação por troca (*swap*), e compara quatro operadores de cruzamento: 1 ponto, 1 ponto com *swap*, 2 pontos e 2 pontos com *swap*.

### `questao02.ipynb`: problemas com DEAP

Três problemas resolvidos com a biblioteca **DEAP**:

1. **Maximização de uma sequência binária:** evoluir indivíduos até chegar ao máximo de bits 1.
2. **Quebra de senha:** encontrar uma senha-alvo a partir de indivíduos formados por caracteres aleatórios.
3. **Caixeiro-viajante (TSP):** encontrar a menor rota entre cidades com coordenadas aleatórias e plotar o melhor percurso.

## Como executar

```bash
pip install deap numpy matplotlib jupyter
jupyter notebook
```

## Tecnologias

Python · DEAP · NumPy · Matplotlib
