# Aula 04: Classificador de Imagens por Histograma

Atividade da disciplina de **Processamento de Imagens**. Classifica imagens usando o **histograma em tons de cinza** como vetor de características e uma rede neural densa (MLP) em Keras.

## Como funciona

1. **Carregamento:** lê as imagens da pasta `data/`, em que cada subpasta é uma classe (`load_data_base`), e mostra quantas imagens tem cada classe.
2. **Divisão:** separa 80% das imagens para treino e 20% para teste, dentro de cada classe (`split_train_test`).
3. **Características:** calcula um histograma de 256 níveis de cada imagem com `cv2.calcHist` (`extract_histoI_gray`). Como as imagens são lidas em BGR e não são convertidas para cinza, o histograma usado é o do primeiro canal (azul).
4. **Modelo:** MLP com duas camadas densas de 128 neurônios (ReLU) e saída *softmax*, com os rótulos em one-hot.
5. **Treino e avaliação** do modelo nos dados de teste.

## Arquivos

- **`classificador.ipynb`**: notebook da atividade.
- **`test_desconsidera.ipynb`**: rascunho de testes (pode ser desconsiderado).

## Como executar

1. Coloque as imagens em `aula04/data/<nome_da_classe>/`. O caminho é montado no formato do Windows (`\data`).
2. Instale as dependências e abra o notebook:

   ```bash
   pip install opencv-python numpy pandas matplotlib scikit-learn tensorflow jupyter
   jupyter notebook classificador.ipynb
   ```

## Tecnologias

Python · OpenCV · TensorFlow/Keras · scikit-learn · pandas
