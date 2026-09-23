# Projeto 01: Classificação de Questões com TF-IDF e Rede Neural

Projeto da disciplina de **Mineração de Textos**. Classifica questões de prova em duas classes (`LABEL_QUESTAO` 0 ou 1), usando TF-IDF para vetorizar o texto e uma rede neural densa em Keras.

## Base de dados

| Arquivo | Conteúdo |
|---|---|
| `data/train.csv` | 303 questões rotuladas (`ID_QUESTAO`, `LABEL_QUESTAO`, `ENUNCIADO_QUESTAO`, `ALTERNATIVA_A` a `ALTERNATIVA_E`) |
| `data/test.csv` | 101 questões sem rótulo, para gerar a submissão |
| `resultado.csv` | previsões finais (`id`, `label`) para a base de teste |

## Como funciona

1. **Pré-processamento:** remoção de pontuação, conversão para minúsculas, tokenização com `RegexpTokenizer` do NLTK e remoção de stopwords em português.
2. **Vetorização:** TF-IDF (`TfidfVectorizer`).
3. **Modelo:** rede densa com 3 camadas de 128 neurônios (ReLU) e saída sigmoide, treinada por 100 épocas com *binary cross-entropy* e divisão de 80/20 entre treino e teste.
4. **Experimentos** (acurácia no conjunto de teste):

   | Texto usado | Acurácia |
   |---|---|
   | só o enunciado | ~92% |
   | só a alternativa A | ~70% |
   | enunciado + alternativa A concatenados | ~90% |

5. O modelo final gera o `resultado.csv` com as previsões da base de teste.

## Arquivos

- **`main_final.ipynb`**: versão final e comentada.
- **`main.ipynb`**, **`main2.ipynb`** e **`opa.ipynb`**: versões anteriores e testes.

## Como executar

```bash
pip install pandas nltk scikit-learn tensorflow matplotlib jupyter
jupyter notebook main_final.ipynb
```

Os caminhos dos CSVs usam o formato do Windows (`data\train.csv`). Execute a partir desta pasta.

## Tecnologias

Python · NLTK · scikit-learn (TF-IDF) · TensorFlow/Keras · pandas
