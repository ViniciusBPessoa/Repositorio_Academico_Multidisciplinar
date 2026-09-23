# Mini Projeto 06: CNN Própria vs. Transfer Learning (CIFAR-10)

Mini projeto da disciplina de **Redes Neurais**. Compara uma **CNN criada do zero** com uma **ResNet-18 pré-treinada** (*transfer learning*) na classificação das 10 classes da base **CIFAR-10**.

## Etapas (`RN_proj_6.ipynb`)

1. **Dados:** baixa a CIFAR-10 pelo `torchvision` e normaliza as imagens.
2. **CNN própria (`Minha_cnn`):** camadas convolucionais (3 → 16 → 32 → 64 canais) com max pooling e uma camada totalmente conectada, treinada por 20 épocas.
3. **Transfer learning:** ResNet-18 pré-treinada na ImageNet, trocando só a última camada (`fc`) para 10 classes e treinando apenas ela.
4. **Comparação:** curvas de perda de cada modelo e acurácia calculada com a função `get_accuracy`.

## Como executar

```bash
pip install torch torchvision matplotlib jupyter
jupyter notebook RN_proj_6.ipynb
```

A base é baixada automaticamente na pasta `data/`.

## Tecnologias

Python · PyTorch · torchvision
