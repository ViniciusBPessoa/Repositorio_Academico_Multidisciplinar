# Recorte e Binarização de Redação Manuscrita

Protótipo com OpenCV para preparar a imagem de uma redação manuscrita para leitura automática (OCR).

## Etapas (`redacao.ipynb`)

1. Carrega a imagem da redação (`nwbufpqf.png`) em tons de cinza.
2. Binariza com o método de **Otsu**.
3. Recorta a área da escrita com uma **transformação de perspectiva**, a partir dos quatro cantos da folha.
4. Salva a região recortada e binarizada (`regiao_recortada_binarizada.png`) e mostra o resultado numa janela do OpenCV.

A pasta também guarda imagens de testes anteriores (`regiao_recortada.png` e `escrita_humana_recortada.png`), e a última célula do notebook é um teste avulso com Pygame, sem relação com a redação.

> **Status:** protótipo inicial.

## Como executar

```bash
pip install opencv-python numpy pygame jupyter
jupyter notebook redacao.ipynb
```

## Tecnologias

Python · OpenCV · NumPy · Pygame
