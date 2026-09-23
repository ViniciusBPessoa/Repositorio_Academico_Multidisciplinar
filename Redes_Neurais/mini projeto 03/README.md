# Mini Projeto 04: Rede RBF para Aproximação de Função

> Apesar do nome da pasta, o conteúdo principal aqui é o **Mini Projeto 04** da disciplina de **Redes Neurais**.

Usa uma **rede de função de base radial (RBF)** com 4 centros para aproximar a função

```
f(x) = sen(x) + 4·cos(x) − 1
```

a partir de 21 pontos igualmente espaçados no intervalo [−2, 4]. No final, é gerado o gráfico da função original comparada com a aproximação da rede.

## Notebooks

- **`mini_projeto04.ipynb`**: versão principal em PyTorch (classe `RBFNet`), com o treino da rede e a análise da convergência conforme o número de épocas.
- **`main.ipynb`**: outras versões do mesmo exercício (uma calculando os pesos por mínimos quadrados em NumPy e duas em PyTorch) e um teste de mapa auto-organizável (SOM) com a base Breast Cancer Wisconsin, que depois foi continuado no [mini projeto 05](../mini%20projeto%2005/).

## Como executar

```bash
pip install torch numpy matplotlib pandas minisom jupyter
jupyter notebook mini_projeto04.ipynb
```

## Tecnologias

Python · PyTorch · NumPy · Matplotlib
