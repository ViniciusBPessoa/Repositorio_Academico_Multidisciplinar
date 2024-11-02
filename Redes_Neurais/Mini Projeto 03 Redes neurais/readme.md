# Projeto: Implementação de uma MLP para Classificação da Base MNIST usando PyTorch

## Descrição
Este projeto consiste na implementação de uma Multi-Layer Perceptron (MLP) utilizando a biblioteca PyTorch para realizar a classificação da base de dados MNIST, que contém imagens de dígitos escritos à mão. 

## Requisitos
- PyTorch
- torchvision
- matplotlib

## Instruções de Uso
1. Baixar o conjunto de dados MNIST.
2. Importar as bibliotecas necessárias.
3. Definir a classe MLP.
4. Treinar o modelo.
5. Avaliar o desempenho do modelo.

## Arquivos do Projeto
- `mlp_mnist.py`: Código fonte do modelo MLP.
- `README.md`: Este arquivo.

## Parâmetros do Modelo Base
- Tamanho de Entrada: 784 (28x28 pixels)
- Número de neurônios na camada oculta: 500
- Número de classes: 10
- Inicialização dos pesos: Aleatória
- Otimizador: SGD (sem momentum)
- Número de Épocas: 5
- Tamanho do Batch: 128
- Taxa de Aprendizado: 0.001

## Modificações Realizadas e Justificativas
- Modificação 1: Aumento do número de épocas para 10.
  - Justificativa: Observou-se que o modelo ainda estava melhorando significativamente após 5 épocas.

- Modificação 2: Redução do número de neurônios na camada oculta para 258.
  - Justificativa: Para reduzir a complexidade do modelo e possivelmente acelerar o treinamento.

- Modificação 3: Redução adicional do número de neurônios na camada oculta para 120.
  - Justificativa: Continuar reduzindo a complexidade do modelo para verificar o impacto no desempenho.

- Modificação 4: Aumento do número de épocas para 25 e aumento do número de neurônios na camada oculta para 150.
  - Justificativa: Observou-se que o modelo ainda estava melhorando de forma linear após 15 épocas e aumentar o número de neurônios pode ajudar a capturar melhor as características dos dados.

- Modificação 5: Aumento da taxa de aprendizado para 0.06.
  - Justificativa: Tentativa de acelerar o processo de treinamento com uma taxa de aprendizado maior.

## Resultados Finais
Os resultados finais obtidos para o modelo otimizado são os seguintes:
- Acurácia de Treinamento: 98.22%
- Acurácia de Teste: 97.54%

## Observações
- Não foi realizada a aplicação de transformações nas imagens, pois não se mostrou benéfico para o modelo.
- O modelo alcançou uma acurácia de teste de 97.54% após as otimizações realizadas.

