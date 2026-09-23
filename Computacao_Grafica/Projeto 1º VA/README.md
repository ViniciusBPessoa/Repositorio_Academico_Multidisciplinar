# Visualizador 3D com Pygame: Projeto 1ª VA

Projeto da disciplina de **Computação Gráfica**. É um visualizador de malhas 3D em que todo o pipeline de projeção é implementado à mão, sem OpenGL: o Pygame serve só para desenhar os pixels na tela.

## Como funciona

1. **Carrega a malha** de um arquivo `.byu` (vértices e triângulos).
2. **Carrega a câmera** de um arquivo de texto (`arquivos/cameras/camera01.txt`), com os vetores N e V, a distância d, os parâmetros hx e hy e a posição C. A câmera é ortogonalizada por Gram-Schmidt para gerar a base (U, V, N).
3. **Muda as coordenadas** dos vértices para o sistema da câmera e aplica a **projeção em perspectiva**.
4. **Rasteriza** a malha: desenha os pontos, as arestas (rasterização de linhas) e o preenchimento dos triângulos, linha a linha.

## Controles do Teclado

| Tecla | Ação |
|---|---|
| `1` | exibe só os pontos |
| `2` | exibe os pontos e as linhas |
| `3` | exibe a malha preenchida |
| `R` | recarrega a malha atual |
| `T` | pede no console o nome de outra malha para carregar |
| `Espaço` | mostra no console todos os valores da malha |
| `7` | abre o vídeo de referência no navegador |
| `Esc` | fecha o programa |

## Estrutura

```
Projeto 1º VA/
├── Main.py                       # loop principal e controles
└── arquivos/
    ├── gerenciador_arquivos.py   # leitura de malhas e câmeras, projeção e rasterização
    ├── auxiliares/               # operações de matrizes e vetores e funções de apoio
    ├── cameras/camera01.txt      # parâmetros da câmera
    └── modelos/                  # malhas .byu (calice2, maca, maca2, piramide, triangulo, vaso)
```

## Como Executar

```bash
pip install pygame
python Main.py
```

## Tecnologias

Python · Pygame
