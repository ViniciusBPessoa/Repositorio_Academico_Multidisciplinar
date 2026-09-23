# Fine-tuning de Modelos Transformer

Experimentos de classificação de texto com modelos pré-treinados e de uso de IA generativa para montar dados de treinamento de NER.

## Notebooks

### `Classification_Pre_Traned.ipynb`: classificação de emoções

Classificação de frases em 6 emoções usando o dataset [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion), em duas abordagens:

1. **Fine-tuning do DistilBERT** (`distilbert-base-uncased`) com o `Trainer` do Hugging Face: 3 épocas, textos de até 128 tokens, avaliados por acurácia, F1, precisão e recall (média ponderada). O notebook também deixa comentadas as alternativas `bert-base-uncased` e `TinyBERT_General_4L_312D`.
2. **Baseline em Keras**: tokenização com vocabulário de 10 mil palavras, camada de embedding, `GlobalAveragePooling1D` e camadas densas, treinada por 10 épocas (cerca de 70% de acurácia na validação).

O `Classificação_Pre_traned.ipynb` é uma versão anterior e mais curta do mesmo experimento. A pasta `logs/` guarda os logs de treino do TensorBoard.

### `Generative_ai.ipynb`: anotação de NER com Gemini

Usa o Gemini (`gemini-1.5-flash`) para gerar automaticamente anotações de entidades em títulos de anúncios de smartphones, no formato usado para treinar modelos de NER:

```python
('Smartphone Motorola G3 4G 64GB ...', {'entities': [(11, 19, 'MARCA'), (20, 22, 'MODELO'), (26, 30, 'MEMORIA')]})
```

No final, o notebook destaca no terminal as entidades encontradas em cada texto, para conferir as anotações.

## Como executar

```bash
pip install torch transformers datasets sentence-transformers scikit-learn tensorflow google-generativeai python-dotenv termcolor jupyter
jupyter notebook
```

Para o notebook do Gemini, defina a chave no arquivo `.env`:

```
GOOGLE_API_KEY=sua_chave_aqui
```
