# Mini Projeto 05: Mapa Auto-Organizável (SOM)

Mini projeto da disciplina de **Redes Neurais**. Aplica um **Mapa Auto-Organizável (SOM)** à base **Breast Cancer Wisconsin (Diagnostic)** para visualizar como os tumores benignos e malignos se organizam no mapa.

## Etapas (`miniprog.ipynb`)

1. **Escolha dos parâmetros:** busca em grade com combinações de `sigma`, taxa de aprendizado e número de iterações de uma SOM 10×10, feita sobre dados simulados e avaliada pela distância média dos outliers.
2. **Dados:** carrega a base do repositório da UCI, converte o diagnóstico em 0 (benigno) e 1 (maligno) e normaliza os atributos com `MinMaxScaler`.
3. **Treino:** SOM 10×10 com `sigma=0.5`, taxa de aprendizado `0.01` e 2000 iterações.
4. **Visualização:** mapa de distâncias dos neurônios (*U-matrix*) com marcadores diferentes para cada classe. Regiões com distâncias altas ajudam a identificar amostras atípicas.

O notebook baixa a base *Diagnostic* (`wdbc.data`) direto da UCI. A pasta `archive.ics.uci.edu/` guarda uma cópia da versão *Original* da base (`breast-cancer-wisconsin.data`), que não é usada no notebook.

## Como executar

```bash
pip install minisom numpy pandas scikit-learn matplotlib jupyter
jupyter notebook miniprog.ipynb
```

## Tecnologias

Python · MiniSom · scikit-learn · pandas · Matplotlib
