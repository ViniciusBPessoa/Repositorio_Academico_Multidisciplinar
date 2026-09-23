# Lista 11: Simulador de Sistema de Arquivos

Prática da disciplina de **Sistemas Operacionais**: um simulador de **sistema de arquivos** em linha de comando, com diretórios em árvore e uma memória dividida em partições.

## Como funciona

1. O usuário informa o tamanho total da memória e o tamanho de cada partição, em KB.
2. O sistema começa com o diretório raiz `C:`.
3. Pelo menu principal, é possível:

| Opção | Ação |
|---|---|
| 1 | listar o conteúdo do diretório atual |
| 2 | entrar em um subdiretório |
| 3 | voltar para o diretório anterior |
| 4 | adicionar um arquivo (nome e tamanho) |
| 5 | adicionar um diretório |
| 6 | remover um item |
| 7 | sair |

Ao criar ou remover arquivos, o espaço é reservado ou liberado nas partições da memória simulada, e o tamanho de cada diretório é recalculado a partir do seu conteúdo.

## Estrutura

```
Lista_11_arquivos/
├── MAIN.py                  # menu principal e navegação
├── Ajudadores/
│   ├── controlador.py       # listagem e criação de itens
│   └── utilitarios.py       # menus e validação de entradas
├── memoria/memoria.py       # classe Memoria (alocação em partições)
└── tipos_arquivos/
    ├── arquivos.py          # classe Arquivo
    └── diretorio.py         # classe Diretorio (árvore de diretórios)
```

## Como executar

```bash
pip install prettytable
python MAIN.py
```

> O programa limpa a tela com o comando `cls`, então foi feito para rodar no terminal do Windows.

## Tecnologias

Python
