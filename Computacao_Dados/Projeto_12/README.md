# Atividade 12: Análise e Visualização de Dados em R

Atividade da disciplina de **Computação para Análise de Dados**. Um relatório em R Markdown com 10 questões de visualização de dados, cada uma numa aba do HTML gerado.

## Conteúdo

- **Questão 1:** tempo médio de resposta (MRT) de um sistema com diferentes quantidades de nós de *fog computing* (1, 3, 5, 10 e 15, e sem fog) em função do intervalo entre as requisições. Tem gráfico de linhas e gráficos de barras em escala logarítmica.
- **Questão 2:** barras empilhadas da avaliação de qualidade de refeições por faixa de preço.
- **Questão 3:** distribuição das temperaturas de maio (dataset `airquality`, convertidas para °C).
- **Questão 5:** boxplot da eficácia de inseticidas (dataset `InsectSprays`).
- As abas das **Questões 4 e 6** estão vazias.
- **Questões 7 a 10:** análise do catálogo da Netflix (`netflix_titles.csv`): países com mais títulos, conteúdo por década de lançamento e lançamentos de 2000 a 2010 por gênero, com gráficos interativos em `plotly`.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `Projeto_12.Rmd` | código e texto do relatório |
| `Projeto_12.html` | relatório gerado |
| `netflix_titles.csv` | catálogo da Netflix usado nas questões 7 a 10 |
| `monitoringCloudData_*.csv` | dados de monitoramento de nuvem que acompanham a atividade |

## Como executar

Abra o `Projeto_12.Rmd` no RStudio, instale os pacotes usados (`ggplot2`, `dplyr`, `tidyr` e `plotly`) e clique em **Knit** para gerar o HTML.

## Tecnologias

R · R Markdown · ggplot2 · dplyr · plotly
