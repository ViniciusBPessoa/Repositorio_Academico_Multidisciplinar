# 📊 Análise de Crimes em Los Angeles (2020 - Presente)

Este projeto realiza uma análise exploratória e visual de crimes ocorridos na cidade de **Los Angeles** a partir de 2020, utilizando dados abertos disponibilizados pelo **LAPD (Los Angeles Police Department)**.

🔗 **[Acesse o relatório publicado no RPubs](https://rpubs.com/Vinicius_Bezerra/CrimesLosAngeles)**

## 📁 Estrutura do Projeto

```
Projeto_FINAL/
│
├── CodigoPrncipal.R                      # Código R complementar com análises/visualizações
├── Crime_Data_from_2020_to_Present.csv  # Base de dados oficial do LAPD (não versionada, baixe no LAPD Open Data)
├── Projeto_FINAL.Rmd                     # Arquivo principal em R Markdown
├── Projeto_FINAL.html                    # Saída em HTML gerada a partir do Rmd
├── Readme.md                             # Este arquivo de descrição
│
├── rsconnect/                            # Configurações de publicação no RPubs
└── .RData, .Rhistory                     # Dados temporários da sessão R
```

## 🎯 Objetivo

Investigar **tendências temporais, padrões geográficos e fatores associados** à criminalidade urbana em Los Angeles, com foco nos seguintes pontos:
- Evolução dos crimes ao longo do tempo;
- Mapeamento das áreas com maior incidência;
- Relação entre tipo de crime, local, horário e outros fatores;
- Geração de insights para políticas públicas e segurança.

## 📚 Dados Utilizados

- **Fonte**: [LAPD Open Data](https://data.lacity.org/)
- **Arquivo**: `Crime_Data_from_2020_to_Present.csv`
- **Período**: de 2020 até o presente momento
- **Informações contidas**:
  - Tipo e descrição dos crimes;
  - Data, hora e localização;
  - Dados sobre a vítima;
  - Códigos e status da ocorrência.

## 🧪 Tecnologias e Pacotes Utilizados

- **Linguagem**: R
- **Ferramentas**: RStudio, R Markdown
- **Principais pacotes**:
  - `dplyr`, `ggplot2`: manipulação e visualização de dados
  - `leaflet`, `leaflet.extras`: mapas interativos
  - `lubridate`: tratamento de datas
  - `rmdformats`: formatação de relatórios

## 🚀 Como Executar

1. Abra o projeto no RStudio.
2. Certifique-se de que todos os pacotes estão instalados (`install.packages()` se necessário).
3. Baixe a base `Crime_Data_from_2020_to_Present.csv` no [LAPD Open Data](https://data.lacity.org/) e coloque na pasta do projeto.
4. Execute o arquivo `Projeto_FINAL.Rmd` (botão *Knit*) para gerar o relatório interativo `Projeto_FINAL.html`.

## ✍️ Autor

- **Vinícius Pessoa Bezerra**  
  Estudante de Ciência da Computação  
  Projeto acadêmico para disciplina da graduação
