# Redes Neurais (MLP) em R: Iris e ENEM

Projeto da disciplina de **Computação para Análise de Dados**, com redes neurais do tipo MLP feitas em R usando o pacote `keras`.

## Scripts

### `MLP_flores.R`

Classifica as três espécies do dataset **Iris**. Os dados são padronizados e divididos em 80% para treino e 20% para teste. A rede tem camadas densas de 64 e 32 neurônios com ReLU e saída *softmax*.

### `MLP_ENEM.R`

Classifica questões do **ENEM** por área de conhecimento (Linguagens, Ciências Humanas, Ciências da Natureza e Matemática). É a versão em R do trabalho feito no [TAIA_project](https://github.com/ViniciusBPessoa/TAIA_project).

- **Pré-processamento do texto:** caixa baixa, remoção de pontuação e de stopwords em português, *stemming* (`SnowballC`) e remoção de palavras curtas, mantendo uma lista de termos importantes de cada área.
- **Modelo:** MLP com número de camadas configurável, treinada sobre as bases `alternativas_separadas.csv` e `tudo_junto.csv` (e as versões pré-processadas `_pp`).

> As bases do ENEM não estão nesta pasta. Para rodar, coloque os CSVs aqui e ajuste o `setwd(...)` do início do script.

## Como executar

No R ou no RStudio:

```r
install.packages(c("keras", "tm", "stringr", "SnowballC", "dplyr", "caret"))
keras::install_keras()
source("MLP_flores.R")
```

## Tecnologias

R · keras (R) · tm · SnowballC · stringr · dplyr · caret
