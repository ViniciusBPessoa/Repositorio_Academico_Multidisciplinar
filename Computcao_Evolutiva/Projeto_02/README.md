# Projeto 02: Neuroevolução vs. PPO

Projeto da disciplina de **Computação Evolutiva**. Compara duas formas de treinar uma rede neural para controlar ambientes do Gymnasium (`CartPole-v1` e `Acrobot-v1`):

- **Computação evolutiva (neuroevolução):** uma população de redes MLP evolui por seleção e mutação dos pesos, sem gradiente.
- **Aprendizado por reforço:** o algoritmo **PPO** do Stable-Baselines3.

## Como funciona a neuroevolução

1. É criada uma população de redes MLP (`redes_neurais/rede_MLP.py`, em PyTorch).
2. Cada rede joga um episódio, e a recompensa obtida é o seu fitness.
3. As melhores redes são selecionadas como pais (`seleciona_pais`).
4. A nova geração é formada por cópias dos pais com **mutação gaussiana nos pesos** (`aplica_mutacao`). Há duas variações: mantendo os pais na geração seguinte ou substituindo todos.
5. O desempenho de cada geração é salvo em arquivos `.pkl`, para ser analisado depois.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `main.ipynb` | experimentos de neuroevolução no CartPole e no Acrobot |
| `PPO_Main.ipynb` | treino e avaliação do PPO no CartPole |
| `graficos_comparativos.ipynb` | gráficos comparando os resultados |
| `func_aux/auxiliares.py` | seleção, mutação, escolha de ação e funções para salvar e carregar os dados |
| `redes_neurais/rede_MLP.py` | rede MLP configurável |
| `redes_analisadas_1..9.pkl` | resultados salvos de cada experimento |

## Como executar

```bash
pip install torch gymnasium stable-baselines3 numpy matplotlib pygame jupyter
jupyter notebook
```

Abra os notebooks a partir desta pasta, porque os módulos auxiliares são importados pelo caminho relativo.

## Tecnologias

Python · PyTorch · Gymnasium · Stable-Baselines3 (PPO) · NumPy · Matplotlib
