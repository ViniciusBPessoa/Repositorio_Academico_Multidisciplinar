# Prova 1ª VA: Análise de Dados em R

Avaliação da disciplina de **Computação para Análise de Dados**, resolvida em R Markdown. O HTML gerado usa o tema `darkly`, com sumário flutuante e uma aba para cada questão.

## Conteúdo

- **VADeaths:** taxas de mortalidade na Virgínia por faixa etária e grupo, reorganizadas com `reshape2` e plotadas em barras com `ggplot2`.
- **Classificação de doença:** frequência e gráfico de pizza com a porcentagem de pacientes em cada estágio de uma doença (leve, moderado e severo).
- **Teorema (Central do Limite):** histograma e curva de densidade das idades de óbito do dataset `flu.csv`, comparados com a distribuição de 200 médias amostrais (n = 35) para ilustrar o teorema.
- **Questão 06:** intervalo de confiança de 98,5% para a altura média das mulheres do dataset `bdims`.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `Prova_Final.Rmd` | código e respostas da prova |
| `Prova_Final.html` | relatório gerado |
| `flu.csv` | dados de óbitos por gripe |
| `bdims.RData` | medidas corporais (dataset `bdims`) |

## Como executar

1. Abra o `Prova_Final.Rmd` no RStudio.
2. Ajuste o `setwd(...)` do início para a pasta onde o projeto está no seu computador.
3. Instale os pacotes `ggplot2`, `reshape2` e `HSAUR3` e clique em **Knit**.

## Tecnologias

R · R Markdown · ggplot2 · reshape2 · HSAUR3
