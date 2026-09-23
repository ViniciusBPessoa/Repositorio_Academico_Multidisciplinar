# Lista 08: Gerência de Memória com Partição Fixa

Prática da disciplina de **Sistemas Operacionais**: um simulador em linha de comando de alocação de memória com **partições fixas**.

> **Status:** em desenvolvimento. O menu, a configuração da memória e a estrutura dos módulos estão prontos, mas os algoritmos de alocação ainda não foram implementados: os arquivos `first-fit.py` e `worst-fit.py` estão vazios, as funções `First_fit`/`Next_fit` do `Main.py` ainda têm trechos com `pass`, a função `add_proc` está incompleta e a opção Next-fit do menu ainda não é alcançada (os dois ramos testam a opção 1). A cópia em [`../Lista_07_SO`](../Lista_07_SO/) tem o First-fit mais avançado.

## Como funciona

1. O usuário informa o tamanho total da memória e o tamanho das partições, em MB (`menu.py`).
2. A memória é dividida em partições fixas (`memoria.py`).
3. Os processos (`processo.py`) seriam alocados nas partições de acordo com o algoritmo escolhido (First-fit ou Next-fit) e escalonados na CPU por **FIFO** (`Algoritimos_CPU/FIFO.py`).

## Estrutura

```
SO_lista_08/Lista_08_Particao_fixa/
├── Pratica_01/
│   ├── Main.py                 # menu de escolha do algoritmo e laço principal
│   ├── menu.py                 # configuração da memória e das partições
│   ├── memoria.py              # modelo da memória particionada
│   ├── processo.py             # modelo de processo
│   ├── utilitarios.py          # validação de entradas e menus
│   ├── Algoritimos_CPU/FIFO.py # escalonamento FIFO
│   └── Algoritmos_Memória/     # first-fit.py e worst-fit.py (vazios)
└── Pratica_02/
    └── utilitarios.py
```

## Como executar

```bash
cd Lista_08_Particao_fixa/Pratica_01
python Main.py
```

## Tecnologias

Python
