# Projetão: Classificação de Personagens dos Simpsons com CNNs

Projeto final da disciplina de **Redes Neurais**. Classifica imagens de personagens de *Os Simpsons* e compara uma **CNN própria** com quatro redes pré-treinadas usadas com *transfer learning*: **VGG16**, **ResNet18**, **DenseNet121** e **MobileNetV2**.

## Etapas

### 1. Preparação dos dados (`preparando_dados.ipynb`)

- Seleção dos personagens com mais imagens na base.
- Recorte das imagens em 75×75 e *data augmentation* com rotações de 45° e 90°.
- Correção e organização da base de teste em pastas por personagem.
- Contagem das imagens de cada classe depois das modificações.

### 2. Modelos (`Modelos_CNN.ipynb`)

- **CNN própria:** 3 camadas convolucionais com pooling e camadas totalmente conectadas.
- **Redes pré-treinadas** do `torchvision`, usadas com as camadas finais originais.
- Treino, avaliação de *overfitting* e *underfitting* pelas curvas de perda e de acurácia e comparação das acurácias de treino e teste em gráfico de barras.
- Os pesos treinados ficam salvos em `redes/` (`cnn.pth`, `resnet.pth`, `densenet.pth` e `mobilenet.pth`).

## Como executar

```bash
pip install torch torchvision opencv-python pandas scikit-learn matplotlib jupyter
```

> A base de imagens não está versionada, e os notebooks usam caminhos absolutos do meu computador (`diretorio_treino` e `diretorio_teste`). Ajuste esses caminhos antes de rodar.

## Tecnologias

Python · PyTorch · torchvision · OpenCV · scikit-learn · pandas
