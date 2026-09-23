# Contagem de Multidões: WAFNet (primeira versão)

Projeto da disciplina de **Visão Computacional**: primeira versão da reprodução da **WAFNet** (Zhou e Hu, 2025), uma rede para estimar quantas pessoas aparecem em imagens de multidão.

> A versão completa e atualizada deste trabalho, com treino no ShanghaiTech, resultados e instruções de uso, está no repositório [crowd_counting](https://github.com/ViniciusBPessoa/crowd_counting).

## Como funciona

- Cada cabeça anotada vira um **borrão gaussiano** no mapa de densidade de referência (`utils/density.py`). A contagem é a soma do mapa.
- A rede tem dois estágios encadeados:
  - **WGN** (`modules/wgn.py`): gera um **mapa de peso** que separa as pessoas do fundo.
  - **DRN** (`modules/drn.py`): recebe esse mapa e regride o **mapa de densidade**.
- `modules/modules.py` traz os blocos auxiliares `LRFEM`, `MLFCM` e `GlobalAttention` (atenção global).
- `modules/wafnet.py` junta os dois estágios, e a perda combina densidade e peso (`lambda_w`).

## Estrutura

```
Projeto_Conting/
├── train.py          # treino (--data, --epochs, --bs, --lr)
├── infer.py          # inferência numa imagem, com visualização dos mapas (--img, --ckpt)
├── data/dataset.py   # CrowdDataset: imagens + anotações → mapas de densidade
├── modules/          # WAFNet, WGN, DRN e blocos auxiliares
└── utils/density.py  # geração do mapa de densidade gaussiano
```

> **Status:** em desenvolvimento. Os scripts importam de `models.wafnet`, mas os módulos estão na pasta `modules/`, então é preciso ajustar os imports (ou renomear a pasta) antes de rodar.

## Como executar

```bash
pip install torch torchvision opencv-python numpy matplotlib tqdm
python train.py --data caminho/para/dados --epochs 10
python infer.py --img foto.jpg --ckpt checkpoint.pth
```

A pasta de dados deve ter as subpastas `images/` e `annots/`.

## Tecnologias

Python · PyTorch · OpenCV · NumPy · Matplotlib
