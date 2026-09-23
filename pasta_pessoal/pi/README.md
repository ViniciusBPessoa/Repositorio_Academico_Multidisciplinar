# Busca de Sequência nos Dígitos de π

Script que calcula **π com milhões de casas decimais** e procura a primeira ocorrência de uma sequência de dígitos, dividindo a busca entre vários processos.

## Como funciona (`po.py`)

1. Calcula π com a precisão pedida usando o `mpmath` (10 milhões de casas no exemplo).
2. Divide os dígitos em partes iguais, uma para cada processo (`multiprocessing`), com uma sobreposição do tamanho da sequência para não perder ocorrências na fronteira entre as partes.
3. Cada processo procura a sequência na sua parte e mostra o progresso.
4. No final, mostra a posição encontrada e o tempo de execução. Como cada processo grava o resultado assim que encontra a sequência na sua parte, a posição mostrada pode não ser a primeira ocorrência quando há mais de uma.

O exemplo do arquivo procura a sequência `40028922` nos primeiros 10 milhões de dígitos, com 4 processos.

## Como executar

```bash
pip install mpmath
python po.py
```

O `requirements.txt` da pasta lista só o ambiente do Jupyter (sem o `mpmath`), e o `pi.ipynb` está vazio.

> No Windows, o `multiprocessing` exige que a chamada principal fique dentro de um bloco `if __name__ == "__main__":`.

## Tecnologias

Python · mpmath · multiprocessing
