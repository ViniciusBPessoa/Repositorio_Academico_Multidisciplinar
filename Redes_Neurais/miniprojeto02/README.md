# Mini Projeto 02: MLP do Zero com NumPy

Mini projeto da disciplina de **Redes Neurais**, feito a partir do notebook-base do curso de Deep Learning ([filiperobotic/cursoDL](https://github.com/filiperobotic/cursoDL)).

O exercício é implementar uma rede **MLP com uma camada escondida**, sem frameworks de deep learning, para a classificação binária do dataset planar *"flower"* (pontos vermelhos e azuis em formato de flor).

> **Status:** incompleto. Só as funções `layer_sizes` e `initialize_parameters` estão implementadas; as demais ainda estão com os trechos `### START CODE HERE ###` em branco.

## Etapas do exercício (`Cópia de MLP_code_v2.ipynb`)

- Inicialização dos parâmetros da rede.
- *Forward propagation* com ativação `tanh` na camada escondida e sigmoide na saída.
- Cálculo da função de custo (*cross-entropy*).
- *Backward propagation* e atualização dos pesos por gradiente descendente.
- Previsão e visualização da fronteira de decisão aprendida pela rede.

## Como executar

O notebook foi feito para o **Google Colab**, e o link está no início do arquivo. Ele importa os módulos auxiliares `testCases_v2` e `planar_utils` do repositório do curso, que são baixados por `git clone` no próprio notebook. Localmente:

```bash
pip install numpy scikit-learn matplotlib jupyter
jupyter notebook
```

## Tecnologias

Python · NumPy · scikit-learn · Matplotlib
