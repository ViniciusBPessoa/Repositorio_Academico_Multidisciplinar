# Visualizador 3D Interativo com Pygame: Projeto 2ª VA

Evolução do [Projeto 1ª VA](../Projeto%201º%20VA/), feita para a disciplina de **Computação Gráfica**. O visualizador carrega malhas 3D, projeta com a câmera virtual e agora também calcula a **iluminação** e usa **Z-buffer** para esconder as superfícies que ficam atrás de outras. Todo o pipeline é implementado à mão, e o Pygame serve só para desenhar na tela.

## Funcionalidades Principais

- Carregar e exibir modelos de malha 3D (`.byu`).
- Projeção em perspectiva a partir de uma câmera definida em arquivo.
- Cálculo das normais de cada triângulo e de cada vértice.
- Iluminação (modelo de Phong) com os parâmetros lidos de `arquivos/iliminacoes/iluminacao01.txt`: intensidade da luz ambiente (Iamb) e coeficiente ambiente (Ka), cor (Il) e posição (P) da fonte de luz, coeficiente difuso (Kd), cor difusa do objeto (O), coeficiente especular (Ks) e expoente de rugosidade (η).
- Z-buffer para remover as superfícies ocultas. Ele começa ligado e pode ser desligado com a tecla `Z`.
- Alternar entre os modos de exibição (pontos, linhas e malha preenchida).

## Controles do Teclado

| Tecla | Ação |
|---|---|
| `1`, `2`, `3` | alternam o modo de exibição (pontos, pontos e linhas, malha preenchida); só têm efeito com o Z-buffer desligado |
| `Z` | liga e desliga o Z-buffer |
| `R` | recarrega a malha atual |
| `T` | pede no console o nome de outra malha para carregar |
| `Espaço` | mostra no console todos os valores da malha |
| `8` | mostra no console as normais dos vértices |
| `7` | abre o vídeo de referência no navegador |
| `Esc` | fecha o programa |

## Estrutura

```
Projeto 2º VA/
├── Main.py                           # loop principal e controles
└── arquivos/
    ├── gerenciador_arquivos.py       # malha, câmera, iluminação, projeção, rasterização e Z-buffer
    ├── auxiliares/                   # operações de matrizes e vetores
    ├── cameras/camera01.txt          # parâmetros da câmera
    ├── iliminacoes/iluminacao01.txt  # parâmetros de iluminação
    └── modelos/                      # malhas .byu
```

## Como Usar

Instale o Pygame:

```bash
pip install pygame
```

Execute o programa a partir da pasta do projeto:

```bash
python Main.py
```

As malhas precisam estar em `arquivos/modelos` para serem carregadas.

## Referências

- [Documentação do Pygame](https://www.pygame.org/docs/)
- [Vídeo de referência (tecla 7)](https://www.youtube.com/watch?v=VBJvDgBZEi4)
