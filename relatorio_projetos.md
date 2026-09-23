# Relatório de Projetos — Repositório Acadêmico Multidisciplinar

> Levantamento gerado em 2026-08-28 a partir da investigação do conteúdo de cada
> pasta do repositório. Curso: Bacharelado em Ciências da Computação (BCC) — UFRPE.
> Autor: Vinícius Bezerra Pessoa (`ViniciusBPessoa`).
>
> **Observação metodológica:** várias pastas de disciplina contêm mais de um
> projeto/atividade independente. Este relatório separa os projetos individuais,
> não as pastas. Listas de exercícios e materiais de aula foram agrupados quando
> não constituem um "projeto" fechado, mas estão registrados para completude.

---

## 1. Inteligência Artificial / Machine Learning

### 1.1. Projeto Atari — DQN e PPO para Space Invaders

- **Caminho:** [Aprendizagem_Refoco/Projeto_Atari/](Aprendizagem_Refoco/Projeto_Atari/)
- **Disciplina/contexto:** Aprendizagem por Reforço (Aprendizagem_Refoco)
- **Tecnologias:** Python, PyTorch, Gymnasium (ALE/Atari), Stable-Baselines3,
  TensorBoard, Optuna (`stud_PPO2.db`), OpenCV, NumPy, Matplotlib
- **Descrição:** Implementa e compara agentes de aprendizado por reforço profundo
  no ambiente Space Invaders do Atari. Há uma implementação própria de DQN
  (rede convolucional em [modelos/dqn_models.py](Aprendizagem_Refoco/Projeto_Atari/modelos/dqn_models.py),
  buffer de replay e wrappers de pré-processamento de frames em
  [wrappers/atari_wrappers.py](Aprendizagem_Refoco/Projeto_Atari/wrappers/atari_wrappers.py))
  e uma versão com PPO via Stable-Baselines3 com busca de hiperparâmetros. Entrega
  agentes treinados, logs de TensorBoard (`runs/`, `log_dir/`) e vídeos do agente
  jogando (`videos/`, `dqn-atari/`).
- **Status:** Finalizado / funcional. Último commit em jan/2025 ("otimização do
  tamanho dos arquivos"). Notebooks `main.ipynb` (29 células), `main_PPO.ipynb`
  (18 células) e `main AD_INFINITUN.ipynb` (30 células) completos; múltiplos
  modelos salvos.

### 1.2. Comparação Computação Evolutiva vs. Aprendizagem por Reforço

- **Caminho:** [Computcao_Evolutiva/Projeto_02/](Computcao_Evolutiva/Projeto_02/)
- **Disciplina/contexto:** Computação Evolutiva (Projeto 02)
- **Tecnologias:** Python, PyTorch (MLP própria), Stable-Baselines3 (PPO),
  Gymnasium, NumPy, Matplotlib, pickle
- **Descrição:** Compara a otimização de redes neurais (MLP) por um algoritmo
  evolutivo/neuroevolução (seleção de pais, mutação de pesos, gerações — em
  [func_aux/auxiliares.py](Computcao_Evolutiva/Projeto_02/func_aux/auxiliares.py))
  contra o treinamento por PPO no mesmo problema de controle. Salva as populações
  de redes avaliadas (`redes_analisadas_1..9.pkl`) e gera gráficos comparativos de
  desempenho ao longo das iterações.
- **Status:** Finalizado. `main.ipynb` (24 células), `PPO_Main.ipynb` e
  `graficos_comparativos.ipynb` (16 células) presentes, com artefatos de resultado
  serializados. Commit nov/2024.

### 1.3. Lista 01 de Computação Evolutiva — Algoritmos Genéticos

- **Caminho:** [Computcao_Evolutiva/Lista 01/](Computcao_Evolutiva/Lista%2001/)
- **Disciplina/contexto:** Computação Evolutiva (lista de exercícios)
- **Tecnologias:** Python, DEAP, NumPy, Matplotlib
- **Descrição:** Conjunto de exercícios resolvidos com algoritmos genéticos:
  problema das 8 rainhas (`questao01.ipynb`, com AG próprio — criação de população,
  fitness, seleção, mutação swap) e, em `questao02.ipynb`, quebra de senha por AG,
  problema do caixeiro-viajante (TSP com 10 cidades) e maximização de sequência
  binária usando a biblioteca DEAP.
- **Status:** Finalizado (exercícios). Não é um projeto único fechado, mas
  entrega soluções completas para 3–4 problemas clássicos.

### 1.4. `evolutionary_computation` — pacote esboçado

- **Caminho:** [Computcao_Evolutiva/evolutionary_computation/](Computcao_Evolutiva/evolutionary_computation/)
- **Disciplina/contexto:** Computação Evolutiva
- **Tecnologias:** Python
- **Descrição:** Esboço de um módulo `genetic_algorithm.py` com a classe
  `Genetc_AI` — apenas o esqueleto (`__init__` com `pass`).
- **Status:** Protótipo abandonado / stub (sem implementação).

---

### 1.5. Redes Neurais — Mini Projeto 02: MLP do zero (dataset "flower")

- **Caminho:** [Redes_Neurais/miniprojeto02/](Redes_Neurais/miniprojeto02/)
- **Disciplina/contexto:** Redes Neurais (mini projeto 02)
- **Tecnologias:** Python, NumPy, scikit-learn, Matplotlib
- **Descrição:** Implementação de uma MLP com uma camada escondida **sem
  frameworks** — forward/backward propagation manuais, ativação `tanh`, perda de
  cross-entropy — para classificação binária no dataset planar "flower". Baseado em
  material de curso (notebook de 53 células, adaptado do curso de Deep Learning do
  prof. Filipe).
- **Status:** Finalizado (exercício guiado completo).

### 1.6. Redes Neurais — Mini Projeto 03: MLP em PyTorch para MNIST

- **Caminho:** [Redes_Neurais/Mini Projeto 03 Redes neurais/](Redes_Neurais/Mini%20Projeto%2003%20Redes%20neurais/)
- **Disciplina/contexto:** Redes Neurais (mini projeto 03)
- **Tecnologias:** Python, PyTorch, torchvision, Matplotlib
- **Descrição:** MLP em PyTorch para classificar dígitos manuscritos (MNIST).
  Inclui um estudo sistemático de hiperparâmetros documentado no
  [readme.md](Redes_Neurais/Mini%20Projeto%2003%20Redes%20neurais/readme.md)
  (variação de épocas, neurônios da camada oculta e taxa de aprendizado, com
  justificativas). Entrega o modelo treinado (`modelo_salvo.pth`) e atinge
  **97,54% de acurácia de teste**.
- **Status:** Finalizado e documentado. Notebook de 33 células + README com
  resultados.

> **Nota:** a pasta [Redes_Neurais/mini projeto 03/](Redes_Neurais/mini%20projeto%2003/)
> (minúscula) é distinta e contém rascunhos do **Mini Projeto 04** (ver abaixo) e
> um teste de SOM com o dataset Breast Cancer Wisconsin — provavelmente pasta com
> nome trocado.

### 1.7. Redes Neurais — Mini Projeto 04: Rede RBF para aproximação de função

- **Caminho:** [Redes_Neurais/mini projeto 03/mini_projeto04.ipynb](Redes_Neurais/mini%20projeto%2003/mini_projeto04.ipynb)
  (e variações em `main.ipynb` na mesma pasta)
- **Disciplina/contexto:** Redes Neurais (mini projeto 04)
- **Tecnologias:** Python, PyTorch, NumPy, Matplotlib
- **Descrição:** Rede de Função de Base Radial (RBF) com 4 centros para aproximar
  a função `sen(x) + 4·cos(x) − 1` em 21 pontos do intervalo [−2, 4]. Gera o
  gráfico da função original vs. a aproximada. Há várias implementações da mesma
  ideia (NumPy via `lstsq`, PyTorch com `nn.Module`).
- **Status:** Finalizado (várias versões do mesmo exercício).

### 1.8. Redes Neurais — Mini Projeto 05: SOM para detecção de outliers

- **Caminho:** [Redes_Neurais/mini projeto 05/miniprog.ipynb](Redes_Neurais/mini%20projeto%2005/miniprog.ipynb)
- **Disciplina/contexto:** Redes Neurais (mini projeto 05)
- **Tecnologias:** Python, MiniSom, scikit-learn, pandas, NumPy, Matplotlib
- **Descrição:** Mapas Auto-Organizáveis (SOM) aplicados ao dataset Breast Cancer
  Wisconsin. Faz busca em grade de `sigma`, taxa de aprendizado e nº de iterações,
  identifica outliers pela distância no mapa e visualiza o mapa de ativação dos
  neurônios com marcadores por classe (benigno/maligno).
- **Status:** Finalizado (5 células, com grid search e visualização).

### 1.9. Redes Neurais — Mini Projeto 06: CNN própria vs. transfer learning (CIFAR-10)

- **Caminho:** [Redes_Neurais/mini projeto 06/RN_proj_6.ipynb](Redes_Neurais/mini%20projeto%2006/RN_proj_6.ipynb)
- **Disciplina/contexto:** Redes Neurais (mini projeto 06)
- **Tecnologias:** Python, PyTorch, torchvision (`models`), Matplotlib
- **Descrição:** Define uma CNN própria (`Minha_cnn`, 3 conv + pooling) e a
  compara com modelos pré-treinados do torchvision no dataset CIFAR-10.
- **Status:** Finalizado (16 células).

### 1.10. Redes Neurais — "Projetão": comparação de arquiteturas CNN (Simpsons)

- **Caminho:** [Redes_Neurais/Projetao/](Redes_Neurais/Projetao/)
- **Disciplina/contexto:** Redes Neurais (projeto final da disciplina)
- **Tecnologias:** Python, PyTorch, torchvision (VGG16, ResNet18, DenseNet121,
  MobileNetV2), scikit-learn (matriz de confusão), OpenCV, pandas
- **Descrição:** Classificação de personagens de "Os Simpsons" a partir de
  imagens. [preparando_dados.ipynb](Redes_Neurais/Projetao/preparando_dados.ipynb)
  faz o pré-processamento (seleção dos personagens com mais imagens, resize 75×75,
  data augmentation por rotação 45°/90°) e
  [Modelos_CNN.ipynb](Redes_Neurais/Projetao/Modelos_CNN.ipynb) treina e compara
  uma CNN própria contra 4 redes pré-treinadas. Entrega os pesos treinados
  (`redes/cnn.pth`, `resnet.pth`, `densenet.pth`, `mobilenet.pth`).
- **Status:** Finalizado. Modelos salvos; commit nov/2024. (Caminhos de dataset
  são absolutos da máquina do autor — precisa de ajuste para reexecução.)

---

### 1.11. Contagem de Multidões — reprodução da WAFNet

- **Caminho:** [visao_Computacional/Projeto_Conting/](visao_Computacional/Projeto_Conting/)
- **Disciplina/contexto:** Visão Computacional (projeto)
- **Tecnologias:** Python, PyTorch, OpenCV, NumPy, Matplotlib, tqdm
- **Descrição:** Reprodução da arquitetura **WAFNet** (Zhou & Hu, 2025) para
  estimar o número de pessoas em imagens de multidão. O modelo tem dois estágios
  encadeados: WGN (gera mapa de peso separando pessoas do fundo) e DRN (regride o
  mapa de densidade). Módulos em
  [modules/](visao_Computacional/Projeto_Conting/modules/) (`wafnet.py`, `wgn.py`,
  `drn.py`, `wgn`), com `train.py` e `infer.py` (visualização de mapas de peso e
  densidade sobre a imagem). Ground-truth por borrões gaussianos nas cabeças
  anotadas.
- **Status:** Em andamento / funcional parcial. Estrutura de treino e inferência
  completa, mas a pasta `data/` está vazia e os imports (`from models...`,
  `from data.dataset...`) divergem da árvore de pastas — precisa de fiação.
  Existe uma versão mais madura e separada deste trabalho no repositório externo
  `crowd-counting` (fora desta pasta), com README, checkpoints e resultados
  (MAE ~175 na época 60, benchmark ShanghaiTech Part A).

### 1.12. Visão Computacional — Projeto Final (vazio)

- **Caminho:** [visao_Computacional/ProjetoFinal/](visao_Computacional/ProjetoFinal/)
- **Disciplina/contexto:** Visão Computacional
- **Descrição:** Apenas uma subpasta `data/` vazia.
- **Status:** Não iniciado / placeholder.

---

### 1.13. Mineração de Textos — Projeto 01: classificação de sentimentos (Disaster Tweets)

- **Caminho:** [Mineracao_Textos/projeto01/](Mineracao_Textos/projeto01/)
- **Disciplina/contexto:** Mineração de Textos (projeto 01)
- **Tecnologias:** Python, TensorFlow/Keras, NLTK, scikit-learn, pandas, Matplotlib
- **Descrição:** Pipeline de PLN para classificar tweets (base `train.csv`/`test.csv`,
  tipo "Real or Not? NLP with Disaster Tweets"): remoção de stopwords,
  vetorização e uma rede densa (Keras `Sequential`) para a classificação binária.
  Entrega `resultado.csv` com as predições. Há várias iterações do notebook
  (`main.ipynb`, `main2.ipynb`, `main_final.ipynb` com 44 células).
- **Status:** Finalizado (`main_final.ipynb`). Commit ago/2024 ("conclusão de AT
  de MT").

### 1.14. Mineração de Textos — Fine-tuning de Sentence Transformers e NER com Gemini

- **Caminho:** [Mineracao_Textos/Finetuning Sentence Transformer models/](Mineracao_Textos/Finetuning%20Sentence%20Transformer%20models/)
- **Disciplina/contexto:** Mineração de Textos (projeto/atividade)
- **Tecnologias:** Python, Hugging Face `transformers` + `datasets`,
  `sentence-transformers`, DistilBERT/TinyBERT, PyTorch, scikit-learn,
  `google-generativeai` (Gemini), spaCy (formato de entidades)
- **Descrição:** Dois experimentos: (1) classificação de emoções no dataset
  `dair-ai/emotion` comparando modelos pré-treinados (`distilbert-base-uncased`,
  `TinyBERT`, `bert-base-uncased`) com fine-tuning e métricas de
  precisão/recall/F1; (2) reconhecimento de entidades nomeadas (MARCA, MODELO,
  MEMÓRIA) em títulos de anúncios de smartphones usando IA generativa (Gemini) para
  gerar/rotular dados. Notebooks: `Classification_Pre_Traned.ipynb` (11 células),
  `Classificação_Pre_traned.ipynb` (5 células), `Generative_ai.ipynb`.
- **Status:** Finalizado / experimental. Commit ago/2024.

---

## 2. Ciência de Dados / Estatística

### 2.1. Análise de Crimes em Los Angeles (2020–presente)

- **Caminho:** [Computacao_Dados/Projeto_FINAL/](Computacao_Dados/Projeto_FINAL/)
- **Disciplina/contexto:** Computação para Análise de Dados (projeto final)
- **Tecnologias:** R, R Markdown, `dplyr`, `ggplot2`, `leaflet`/`leaflet.extras`,
  `lubridate`, `rmdformats`
- **Descrição:** Análise exploratória e visual de dados abertos do LAPD sobre
  crimes em Los Angeles: tendências temporais, mapeamento geográfico das áreas de
  maior incidência e relação entre tipo de crime, local e horário. Entrega um
  relatório HTML publicado no RPubs
  (rpubs.com/Vinicius_Bezerra/CrimesLosAngeles) e código R complementar.
- **Status:** Finalizado e publicado. README completo; commit jun/2025.

### 2.2. Prova 1ª VA — Análise de Dados (relatório)

- **Caminho:** [Computacao_Dados/Prova1VA/](Computacao_Dados/Prova1VA/)
- **Disciplina/contexto:** Computação para Análise de Dados (avaliação)
- **Tecnologias:** R Markdown, `ggplot2`, `reshape2`, `HSAUR3`
- **Descrição:** Relatório de prova com análises sobre os datasets `VADeaths`,
  `bdims` e `flu.csv` — visualizações e estatística descritiva, com saída HTML
  temada (`darkly`).
- **Status:** Finalizado (entregue como avaliação).

### 2.3. Atividade 12 — Análise de desempenho Fog Computing

- **Caminho:** [Computacao_Dados/Projeto_12/](Computacao_Dados/Projeto_12/)
- **Disciplina/contexto:** Computação para Análise de Dados (atividade 12)
- **Tecnologias:** R Markdown, gráficos base do R
- **Descrição:** Análise de tempo de resposta (MRT) de um sistema com diferentes
  quantidades de "fogs" (1, 3, 5, 10, 15 e sem fog) em função do intervalo entre
  requisições, com gráficos de linha e de barras em escala log. Inclui também uso
  do dataset `netflix_titles.csv`.
- **Status:** Finalizado (atividade). Saída HTML gerada.

### 2.4. Projeto MLP em R — ENEM e Iris

- **Caminho:** [Computacao_Dados/projeto/](Computacao_Dados/projeto/)
- **Disciplina/contexto:** Computação para Análise de Dados
- **Tecnologias:** R, `keras` (R), `tm`, `stringr`, `SnowballC`, `datasets`
- **Descrição:** Dois scripts: `MLP_flores.R` treina uma rede densa Keras para
  classificar espécies de flores (Iris); `MLP_ENEM.R` faz pré-processamento de
  texto em português (lowercase, remoção de pontuação, stopwords PT, stemming,
  lista de termos-chave por disciplina) sobre questões do ENEM
  (`alternativas_separadas.csv`, `tudo_junto.csv`) para alimentar uma MLP.
- **Status:** Em andamento / parcial. Scripts presentes; os CSVs do ENEM não
  estão versionados na pasta.

### 2.5. Atividades e datasets de Análise de Dados (exercícios)

- **Caminho:** [Computacao_Dados/Atividade_03..08/](Computacao_Dados/),
  [Computacao_Dados/Pasta_foda/](Computacao_Dados/Pasta_foda/)
- **Disciplina/contexto:** Computação para Análise de Dados (listas)
- **Tecnologias:** R (`.RData`, `.Rhistory`)
- **Descrição:** Pastas de exercícios pontuais com datasets (`Sparrows.csv`,
  `genomes.csv`, `tb.csv`, `Catfish.csv`, `Forbes2000_V2.csv`, `Treatment.csv`
  etc.) e histórico de sessão R. Não são projetos fechados — material de estudo.
- **Status:** Exercícios / material de apoio.

---

## 3. Processamento de Imagens

### 3.1. Classificação de Tumores Cerebrais — impacto do pré-processamento (CNN vs. MLP)

- **Caminho:** [Processamento_imagens/preprocessamento_cnn_mlp/](Processamento_imagens/preprocessamento_cnn_mlp/)
- **Disciplina/contexto:** Processamento de Imagens (projeto; ligado a projeto de
  extensão da UFRPE)
- **Tecnologias:** Python, TensorFlow/Keras (`modelo_cnn.h5`, `modelo_mlp.h5`),
  OpenCV, scikit-learn, NumPy, Matplotlib; features de Hu e LBP
- **Descrição:** Estuda como diferentes técnicas de pré-processamento
  (equalização de histograma, ajuste de brilho, limiarização, filtros gaussiano/
  mediana/laplaciano, normalização, componentes conectados — e combinações)
  afetam a classificação de MRIs de tumor cerebral em 4 classes (glioma,
  meningioma, sem tumor, pituitária). Compara uma CNN (3 conv + pooling) com uma
  MLP. Entrega ~10 pares de histórico de treino + matriz de confusão por
  combinação (`historicos/`), modelos `.h5` e um
  [README](Processamento_imagens/preprocessamento_cnn_mlp/readme.md) detalhado
  com o pipeline e a base (5.249 MRIs do Kaggle).
- **Status:** Finalizado e bem documentado. Commit jun/2025. Notebook principal de
  33 células + notebook de análise de resultados.

### 3.2. Mini Programa 1ª VA — Lista de exercícios práticos de PI

- **Caminho:** [Processamento_imagens/mini_prog_1va/1ª_Lista_de_Exercícios_Práticos.ipynb](Processamento_imagens/mini_prog_1va/1%C2%AA_Lista_de_Exerc%C3%ADcios_Pr%C3%A1ticos.ipynb)
- **Disciplina/contexto:** Processamento de Imagens (mini-prova / lista 1ª VA)
- **Tecnologias:** Python, OpenCV, NumPy, Matplotlib
- **Descrição:** Lista de exercícios práticos: redução de ruído com operações
  básicas, filtros, etc. A subpasta `processamento_imagens/` é um clone do
  repositório de material da disciplina (aulas em PDF + notebooks de
  Introdução, Filtros, Operações e Segmentação).
- **Status:** Finalizado (lista resolvida — 18 células). Material de aula anexo.

### 3.3. Classificador de imagens (aula 04)

- **Caminho:** [Processamento_imagens/aula04/classificador.ipynb](Processamento_imagens/aula04/classificador.ipynb)
- **Disciplina/contexto:** Processamento de Imagens (aula/atividade 04)
- **Tecnologias:** Python, OpenCV, TensorFlow/Keras, scikit-learn, pandas
- **Descrição:** Carrega uma base de imagens organizada em subpastas por classe,
  monta o dataset (contagem por pasta, encoding one-hot) e treina uma CNN Keras
  para classificação.
- **Status:** Finalizado (29 células).

### 3.4. Experimentos avulsos de PI (`pequenasCoisas`, `arquivos de beckap`)

- **Caminho:** [Processamento_imagens/pequenasCoisas/](Processamento_imagens/pequenasCoisas/),
  [Processamento_imagens/arquivos de beckap/](Processamento_imagens/arquivos%20de%20beckap/)
- **Disciplina/contexto:** Processamento de Imagens
- **Tecnologias:** Python, OpenCV, Matplotlib
- **Descrição:** Notebooks curtos de teste (histograma, testes diversos, backup de
  aula de OpenCV).
- **Status:** Rascunhos / scratch.

---

## 4. Computação Gráfica

### 4.1. Visualizador 3D Interativo — Projeto 1ª VA

- **Caminho:** [Computacao_Grafica/Projeto 1º VA/](Computacao_Grafica/Projeto%201%C2%BA%20VA/)
- **Disciplina/contexto:** Computação Gráfica (Projeto 1ª VA)
- **Tecnologias:** Python, Pygame, matemática própria (sem OpenGL)
- **Descrição:** Renderizador 3D que carrega malhas no formato `.byu` (cálice,
  maçã, pirâmide, vaso, triângulo), aplica a câmera definida em arquivo texto e
  projeta os modelos em tela, desenhando pontos, arestas (rasterização de linhas)
  e preenchimento de triângulos. Pipeline implementado à mão em
  [arquivos/](Computacao_Grafica/Projeto%201%C2%BA%20VA/arquivos/) (gerenciador de
  malhas/câmeras, `matematica_aux`, `operacoes_aux`). Modos de exibição
  alternáveis por teclado.
- **Status:** Finalizado e funcional.

### 4.2. Visualizador 3D Interativo com Iluminação e Z-buffer — Projeto 2ª VA

- **Caminho:** [Computacao_Grafica/Projeto 2º VA/](Computacao_Grafica/Projeto%202%C2%BA%20VA/)
- **Disciplina/contexto:** Computação Gráfica (Projeto 2ª VA)
- **Tecnologias:** Python, Pygame
- **Descrição:** Evolução do projeto 1ª VA: adiciona **iluminação** (modelo
  carregado de [arquivos/iliminacoes/iluminacao01.txt](Computacao_Grafica/Projeto%202%C2%BA%20VA/arquivos/iliminacoes/iluminacao01.txt),
  normais por triângulo e por vértice) e **Z-buffer** para remoção de superfícies
  ocultas. Controles de teclado para recarregar malha, digitar novo arquivo,
  alternar modos e inspecionar valores. Documentado no
  [README](Computacao_Grafica/Projeto%202%C2%BA%20VA/README.md).
- **Status:** Finalizado. Commit set/2025 ("Alterações no projeto e visualização
  do mesmo"). Existem ainda `Projeto 1º VA.zip` e `Projeto 3º VA .zip` (este
  último sem pasta descompactada — projeto da 3ª VA provavelmente não versionado
  em código aberto).

---

## 5. Sistemas / Arquitetura / Sistemas Operacionais

### 5.1. Arquitetura — Projeto 1ª VA: "VIA-shell" em MIPS Assembly com MMIO

- **Caminho:** [Arquitetura_Computadores/Projeto-1VA-AOC-2022.1/](Arquitetura_Computadores/Projeto-1VA-AOC-2022.1/)
- **Disciplina/contexto:** Arquitetura e Organização de Computadores (2022.1) —
  trabalho em grupo (Vinícius, Irlan, Apolo, João Vitor)
- **Tecnologias:** MIPS Assembly (MARS), Memory-Mapped I/O (MMIO), manipulação de
  arquivo em disco
- **Descrição:** Shell de linha de comando (`VIA-shell>>`) rodando via MMIO que
  gerencia um "condomínio": comandos para adicionar/remover moradores e
  automóveis, limpar apartamento, exibir informações de um AP ou gerais, e
  salvar/recarregar/formatar os dados em arquivo (`C:/aps.txt`). Inclui
  `final.asm`, versão sem MMIO (`final(S_MMIO).asm`), as questões da lista
  (substituição de caracteres em string, etc.) e versões individuais de cada
  integrante.
- **Status:** Finalizado (entregue em 2022.1).

### 5.2. Arquitetura — Projeto 2ª VA: processador MIPS monociclo em Verilog

- **Caminho:** [Arquitetura_Computadores/Projeto-2VA-AOC-2022.1/](Arquitetura_Computadores/Projeto-2VA-AOC-2022.1/)
- **Disciplina/contexto:** Arquitetura e Organização de Computadores (2022.1) —
  mesmo grupo
- **Tecnologias:** Verilog HDL
- **Descrição:** Implementação de um núcleo **MIPS monociclo** em Verilog: PC,
  memória de instruções e de dados, banco de registradores, ULA + controle da ULA,
  unidade de controle, extensor de sinal, somadores de PC e de jump, e o
  top-level `MIPS.v`. Acompanha um programa de teste em binário
  (`instruction.list`).
- **Status:** Finalizado (entregue em 2022.1).

### 5.3. SO — Lista 02: exclusão mútua e escalonador preemptivo

- **Caminho:** [Sistemas_Operacionais/SO-Lista-02/](Sistemas_Operacionais/SO-Lista-02/)
- **Disciplina/contexto:** Sistemas Operacionais (Lista 02)
- **Tecnologias:** Python (`threading`, semáforos)
- **Descrição:** Dois programas. **Questão 1:** simulação de atendimento em um
  estabelecimento — 5 threads concorrendo por 2 recursos compartilhados (listas
  de espera e de atendidos), com semáforos demonstrando condição de corrida e
  exclusão mútua via logs. **Questão 2:** mini-simulador de escalonamento
  preemptivo de processos por linha de comando, com algoritmos **Prioridade** e
  **SJF** (com preempção), quantum configurável, fila de prontos dinâmica e
  cálculo de turnaround e tempo médio de espera.
- **Status:** Finalizado e documentado no
  [README](Sistemas_Operacionais/SO-Lista-02/README.md).

### 5.4. SO — Lista 08: gerência de memória com partição fixa

- **Caminho:** [Sistemas_Operacionais/SO_lista_08/](Sistemas_Operacionais/SO_lista_08/)
  (cópia também em [Sistemas_Operacionais/Lista_07_SO/SO_lista_08/](Sistemas_Operacionais/Lista_07_SO/SO_lista_08/))
- **Disciplina/contexto:** Sistemas Operacionais (Lista 08)
- **Tecnologias:** Python
- **Descrição:** Simulador interativo de alocação de memória com **partição
  fixa**, implementando estratégias First-fit / Next-fit / Worst-fit e um
  escalonador de CPU FIFO. Módulos separados para memória, processo, menu e
  utilitários.
- **Status:** Em andamento / parcial. Estrutura e menus prontos, mas há ramos de
  ação ainda vazios (`pass`) no `Main.py`. A pasta `Lista_07_SO` contém uma cópia
  aninhada da Lista 08 (organização confusa).

### 5.5. SO — Lista 11: simulador de sistema de arquivos

- **Caminho:** [Sistemas_Operacionais/Lista_11_arquivos/](Sistemas_Operacionais/Lista_11_arquivos/)
- **Disciplina/contexto:** Sistemas Operacionais (Lista 11)
- **Tecnologias:** Python
- **Descrição:** Simulador de sistema de arquivos por linha de comando: navegação
  em diretórios (entrar, voltar, listar), criação e remoção de arquivos e
  diretórios, com um modelo de memória de partições (tamanho total e de partição
  configuráveis). Estrutura hierárquica de diretórios (`Diretorio`, `Arquivo`) e
  camada de controle/utilitários.
- **Status:** Finalizado / funcional (menu completo com 7 operações).

---

## 6. Testes de Software

### 6.1. Testes de um verificador/gerador de Sudoku (grupo 7)

- **Caminho:** [Testes_Software/Sudoku/](Testes_Software/Sudoku/)
- **Disciplina/contexto:** Testes de Software (atividade em grupo — G7)
- **Tecnologias:** Python, pytest, biblioteca `py-sudoku`
- **Descrição:** Exercício de teste de software sobre duas implementações de um
  verificador de Sudoku — uma correta (`G7_Sudoku_ok`) e uma com defeito
  proposital (`G7_Sudoku_nok`, que não detecta erros nas subgrades 3×3). Inclui um
  gerador de tabuleiros válidos e inválidos (`GeradorSudoku.py`) e a suíte de
  testes (`Teste_7.py`) que evidencia o defeito — testes projetados para passar na
  versão correta e falhar na defeituosa. Arquivos de fixture `sudoku_ok.txt` /
  `sudoku_nok.txt`.
- **Status:** Finalizado. Commit out/2025; `.pytest_cache` presente (testes
  executados).

### 6.2. SudokuProject (Java / Eclipse)

- **Caminho:** [Testes_Software/SudokuProject/](Testes_Software/SudokuProject/)
- **Disciplina/contexto:** Testes de Software
- **Tecnologias:** Java (projeto Eclipse)
- **Descrição:** Projeto Java praticamente vazio — apenas `module-info.java` e o
  esqueleto do projeto Eclipse. Provavelmente o ponto de partida abandonado antes
  de migrar o trabalho para Python.
- **Status:** Não iniciado / stub.

---

## 7. Monitoria (material didático)

### 7.1. Monitoria de Programação II — exemplos em Java (OO)

- **Caminho:** [Monitoria/ProgII/Java/JavaProgII/](Monitoria/ProgII/Java/JavaProgII/)
- **Disciplina/contexto:** Monitoria de Introdução à Programação II / POO
- **Tecnologias:** Java (Eclipse)
- **Descrição:** Conjunto de exemplos didáticos de orientação a objetos para os
  alunos: **Sistema Bancário** (`Banco`, `ContaBancaria`, `ContaEspecial`,
  `ContaPoupanca` — herança, extrato, transferência) e **Biblioteca**
  (`Biblioteca`, `Livro`, `Revista` — polimorfismo, empréstimo/devolução). Há uma
  pasta `correcaoAtts/` com versões de correção das atividades e testes
  (`TesteSistemaBancario.java`, `TesteBiblioteca.java`), e um esqueleto `Empresa`.
- **Status:** Finalizado / em uso na monitoria. Commit out/2025 ("Resposta de
  atividades voltadas a monitoria IP2").

### 7.2. Monitoria de Programação I — exercícios Python

- **Caminho:** [Monitoria/Prog1/](Monitoria/Prog1/),
  [pasta_pessoal/monitoria/](pasta_pessoal/monitoria/)
- **Disciplina/contexto:** Monitoria de Introdução à Programação I
- **Tecnologias:** Python
- **Descrição:** Resoluções de exercícios básicos (estatísticas sobre listas de
  altura/sexo) e um "Menu do Planner" de tarefas em linha de comando usado como
  exemplo introdutório.
- **Status:** Finalizado (material de apoio).

---

## 8. Desenvolvimento Web

### 8.1. API de Usuários — arquitetura de microsserviços (NestJS)

- **Caminho:** [Desenvolvimento_WEB/desenv-web/](Desenvolvimento_WEB/desenv-web/)
- **Disciplina/contexto:** Desenvolvimento Web (projeto exemplo)
- **Tecnologias:** TypeScript, NestJS, Sequelize (migrations/seeders),
  PostgreSQL, NATS (mensageria entre serviços), JWT/Passport (auth), Docker /
  docker-compose, Biome/ESLint/Prettier, Webpack, monorepo (`apps/` + `libs/`)
- **Descrição:** Aplicação de referência com **Clean Architecture** e separação em
  camadas (domain / application / infrastructure / interface). Dois apps —
  `users` (regras de negócio: casos de uso de criar, atualizar, trocar senha,
  buscar por id/email, listar) e `api-users` (camada REST + autenticação JWT e
  login local) — comunicando-se por NATS. Lib `common` extensa com decorators,
  interceptors, filtros de exceção, middlewares e módulos compartilhados.
  Infra de deploy com Dockerfiles por serviço e scripts de migração.
- **Status:** Em andamento / esqueleto avançado. Commit set/2025 ("adição do
  projeto exemplo"). Estrutura muito completa (padrões, auth, mensageria, deploy),
  mas escopo funcional limitado ao CRUD de usuários; sem testes versionados.

---

## 9. Projeto de Extensão

### 9.1. Post técnico — Integrando Python com a API do Google Gemini

- **Caminho:** [Extencao/Post_01/](Extencao/Post_01/),
  [Extencao/post_comparacao/](Extencao/post_comparacao/)
- **Disciplina/contexto:** Extensão universitária (produção de conteúdo para blog)
- **Tecnologias:** Python, `google-generativeai` (Gemini 1.5 Flash/Pro), Jupyter
- **Descrição:** Material de um artigo/post ensinando a usar a API do Google
  Gemini em Python (configuração, pré-requisitos, primeira chamada, instruções de
  sistema, modo JSON), com uma seção de **comparação entre modelos** Gemini
  (limites de tokens, RPM/TPM, capacidades multimodais) e as especificações
  detalhadas de cada modelo. Versões com e sem comentários do notebook.
- **Status:** Finalizado. Commit "última atualização da at de PI".

### 9.2. Integração com a API do Google Calendar

- **Caminho:** [Extencao/API_google_calendar/](Extencao/API_google_calendar/)
- **Disciplina/contexto:** Extensão universitária
- **Tecnologias:** Python, Google Calendar API (`google-api-python-client`,
  OAuth2 via `google-auth-oauthlib`)
- **Descrição:** Notebook que autentica via OAuth2 (fluxo com `credentials.json` /
  `token.pickle`) e cria eventos no Google Calendar com local, descrição, horário
  (fuso America/Sao_Paulo) e lembretes por e-mail e popup.
- **Status:** Finalizado / funcional (10 células).

---

## 10. Pessoal (`pasta_pessoal`)

### 10.1. Passeio do Cavalo (Knight's Tour) com busca prospectiva

- **Caminho:** [pasta_pessoal/ProjetoCavalo/](pasta_pessoal/ProjetoCavalo/)
- **Tecnologias:** Python
- **Descrição:** Classe `Tabuleiro` que resolve o problema do passeio do cavalo
  no tabuleiro de xadrez com heurística de profundidade prospectiva configurável;
  joga a partida completa automaticamente e retorna a pontuação (casas visitadas).
- **Status:** Parcial. `Tabuleiro.py` implementado; `Main.py` está vazio.
  Commit recente (fev/2026 na árvore) — nome aparece em "mudança projeto do cavalo".

### 10.2. Jogo da Velha (biblioteca)

- **Caminho:** [pasta_pessoal/Jogo_Velha/](pasta_pessoal/Jogo_Velha/)
- **Tecnologias:** Python
- **Descrição:** Classe `jogo_velha` com verificação de vitória (linhas, colunas,
  diagonais), jogada, reset e testes embutidos no próprio módulo.
- **Status:** Funcional como biblioteca; `main.py` vazio (sem loop de jogo /
  interface).

### 10.3. Catálogo pessoal de filmes/séries

- **Caminho:** [pasta_pessoal/Vini/](pasta_pessoal/Vini/) (`main.py`, `Luc.py`,
  `Utilitarios/padrao.py`)
- **Tecnologias:** Python
- **Descrição:** Sistema de linha de comando para cadastrar usuários e avaliar
  filmes/séries por usuário, com um utilitário de menu reaproveitável (`padrao`).
  `Luc.py` é uma variação com catálogo fixo e sorteio.
- **Status:** Em andamento (arquivos não versionados ainda — aparecem como
  untracked no git).

### 10.4. Busca de sequência nos dígitos de π (paralelizada)

- **Caminho:** [pasta_pessoal/pi/](pasta_pessoal/pi/)
- **Tecnologias:** Python, `mpmath`, `multiprocessing`
- **Descrição:** Calcula π com milhões de casas decimais (`mpmath`) e procura a
  primeira ocorrência de uma sequência de dígitos dividindo o intervalo entre
  vários processos, com barra de progresso.
- **Status:** Funcional (`po.py`).

### 10.5. Página pessoal — backend Firebase + tradução automática

- **Caminho:** [pasta_pessoal/paginaPessoal/](pasta_pessoal/paginaPessoal/)
- **Tecnologias:** Python, Firebase Admin SDK / Firestore, `google-generativeai`
  (Gemini 1.5 Pro), `python-dotenv`
- **Descrição:** Scripts que populam uma coleção `Informations` no Firestore com
  os dados do portfólio pessoal (bio, conhecimentos) e um tradutor
  (`firebaseTradutor.py`) que traduz automaticamente os textos PT→EN via Gemini
  preservando o markdown, para servir a versão em inglês do site.
- **Status:** Funcional. **Atenção de segurança:** `serviceAccountKey.json` e uma
  chave de API do Gemini estão hardcoded/versionados — devem ser revogados e
  removidos do histórico.

### 10.6. OCR / segmentação de redação manuscrita

- **Caminho:** [pasta_pessoal/redacao/](pasta_pessoal/redacao/)
- **Tecnologias:** Python, OpenCV, NumPy
- **Descrição:** Notebook que binariza (Otsu) e recorta regiões de uma imagem de
  redação manuscrita — primeiros passos de um pipeline de OCR/segmentação de
  texto. Salva as regiões recortadas e binarizadas.
- **Status:** Protótipo inicial (7 células).

### 10.7. Desafios de programação

- **Caminho:** [pasta_pessoal/Desafios/](pasta_pessoal/Desafios/)
- **Tecnologias:** Python
- **Descrição:** 5 exercícios curtos de lógica (manipulação de listas, strings,
  padrões).
- **Status:** Finalizado (exercícios isolados).

### 10.8. Transcritor de combinadores SKI e outros rascunhos

- **Caminho:** [pasta_pessoal/nao_sei_oque_faz_aqui/](pasta_pessoal/nao_sei_oque_faz_aqui/)
- **Tecnologias:** Python (`pyttsx3` para TTS num dos arquivos)
- **Descrição:** Pasta de rascunhos: transcritor de expressões de lógica
  combinatória (SKI calculus) para tokens (`PT_2.py`), texto-para-voz lendo
  arquivo (`test_voice.py`), geradores de triângulos e testes diversos.
- **Status:** Rascunhos / scratch (o próprio nome da pasta é "não sei o que faz
  aqui").

---

## Resumo Geral

### Contagem de projetos

Considerando **projetos individuais** (não pastas), e classificando por
substância:

| Categoria | Qtde |
|---|---|
| Projetos acadêmicos "de verdade" (entregáveis de disciplina, com escopo fechado) | **~22** |
| Listas de exercícios / atividades resolvidas tratadas como conjunto | ~6 |
| Projetos pessoais | 8 |
| Stubs / vazios / não iniciados | 4 (`evolutionary_computation`, `ProjetoFinal` de VC, `SudokuProject` Java, esqueletos de `Main.py`) |
| **Total de itens catalogados** | **~40** |

Distribuição dos projetos acadêmicos por área:

- **IA / ML / Dados:** ~14 (Aprendizagem por Reforço, Computação Evolutiva ×2,
  Redes Neurais ×6, Visão Computacional, Mineração de Textos ×2, mais os projetos
  em R de Ciência de Dados)
- **Ciência de Dados / Estatística (R):** 4
- **Processamento de Imagens:** 3
- **Computação Gráfica:** 2
- **Arquitetura de Computadores:** 2
- **Sistemas Operacionais:** 3
- **Testes de Software:** 1
- **Desenvolvimento Web:** 1
- **Extensão:** 2
- **Monitoria (material):** 2

### Tecnologias mais recorrentes

1. **Python** — linguagem dominante, presente na grande maioria dos projetos.
2. **PyTorch** — framework de deep learning mais usado (Atari/DQN, Computação
   Evolutiva, Redes Neurais 03–06, Projetão, WAFNet).
3. **NumPy + Matplotlib** — onipresentes em qualquer projeto numérico/ML.
4. **scikit-learn** — pré-processamento e métricas em quase todos os projetos de ML.
5. **OpenCV** — todos os projetos de imagem/visão.
6. **TensorFlow/Keras** — projetos de PI (tumores cerebrais, classificador aula 04)
   e Mineração de Textos projeto 01.
7. **Pygame** — os dois projetos de Computação Gráfica.
8. **R** (+ `ggplot2`, `dplyr`, R Markdown, `leaflet`) — toda a disciplina de
   Computação para Análise de Dados.
9. **Gymnasium + Stable-Baselines3** — projetos de RL e a comparação evolutiva.
10. **Hugging Face (`transformers`, `datasets`, `sentence-transformers`)** —
    Mineração de Textos.
11. **Google Gemini API (`google-generativeai`)** — Extensão ×2, página pessoal,
    Mineração de Textos (NER).
12. **Java** — Arquitetura (não; Verilog), Monitoria ProgII, stub de Testes.
13. **TypeScript / NestJS / Sequelize / Docker / NATS** — projeto de
    Desenvolvimento Web.
14. **MIPS Assembly** e **Verilog** — os dois projetos de Arquitetura (2022.1).
15. **Firebase / Firestore** — página pessoal.

### Projetos mais relevantes para destacar em currículo

Em ordem aproximada de valor de portfólio:

1. **Classificação de Tumores Cerebrais — CNN vs. MLP com estudo de
   pré-processamento** ([Processamento_imagens/preprocessamento_cnn_mlp/](Processamento_imagens/preprocessamento_cnn_mlp/)) —
   projeto completo, metodologicamente rigoroso (dezenas de combinações
   avaliadas com matriz de confusão), tema de impacto (apoio a diagnóstico
   médico), ligado a extensão da UFRPE, README excelente. **Melhor cartão de
   visita.**

2. **Reprodução da WAFNet — Contagem de Multidões** (versão madura no repo
   externo `crowd-counting`; versão inicial em
   [visao_Computacional/Projeto_Conting/](visao_Computacional/Projeto_Conting/)) —
   reprodução de um paper de 2025 (revista *Image and Vision Computing*),
   arquitetura de dois estágios não trivial, com benchmark e discussão de
   resultados. Demonstra capacidade de ler literatura recente e implementá-la.

3. **Projeto Atari — DQN próprio + PPO para Space Invaders**
   ([Aprendizagem_Refoco/Projeto_Atari/](Aprendizagem_Refoco/Projeto_Atari/)) —
   RL profundo com implementação from-scratch (replay buffer, wrappers de frame,
   rede convolucional) e comparação com biblioteca padrão + tuning de
   hiperparâmetros. Tema atraente e resultado visual (vídeos do agente).

4. **Comparação Neuroevolução vs. PPO**
   ([Computcao_Evolutiva/Projeto_02/](Computcao_Evolutiva/Projeto_02/)) —
   combina dois paradigmas de otimização de políticas e mede empiricamente, com
   artefatos de resultado salvos.

5. **Redes Neurais — "Projetão" (comparação de 5 arquiteturas CNN, Simpsons)**
   ([Redes_Neurais/Projetao/](Redes_Neurais/Projetao/)) — transfer learning,
   data augmentation, pipeline de dados e avaliação comparativa; entrega 4
   modelos treinados.

6. **API de Usuários em NestJS com Clean Architecture + microsserviços**
   ([Desenvolvimento_WEB/desenv-web/](Desenvolvimento_WEB/desenv-web/)) — único
   projeto de engenharia de software "de produção" (TypeScript, mensageria NATS,
   JWT, Docker, migrations). Bom para vagas de back-end, se o escopo funcional
   for expandido e ganhar testes.

7. **Análise de Crimes em Los Angeles (R + relatório publicado)**
   ([Computacao_Dados/Projeto_FINAL/](Computacao_Dados/Projeto_FINAL/)) — data
   storytelling completo com mapas interativos e entregável público (RPubs).
   Ótimo para vagas de Ciência/Análise de Dados.

8. **Processador MIPS monociclo em Verilog + VIA-shell em Assembly com MMIO**
   ([Arquitetura_Computadores/](Arquitetura_Computadores/)) — mais antigos
   (2022.1) e em grupo, mas mostram fundamentos sólidos de arquitetura/hardware.

**Menção — Mineração de Textos (fine-tuning de BERT + NER com LLM):** relevante
para PLN, mas está em estado mais experimental/desorganizado; valeria consolidar
num único notebook limpo antes de expor.

### Ações recomendadas antes de usar como portfólio

- **Segurança:** revogar e remover do histórico o `serviceAccountKey.json` e a
  API key do Gemini hardcoded em
  [pasta_pessoal/paginaPessoal/](pasta_pessoal/paginaPessoal/); revisar
  `Extencao/*/credentials.json` e arquivos `.env` versionados.
- **Reprodutibilidade:** substituir caminhos absolutos
  (`C:\Users\Pichau\...`) por caminhos relativos nos notebooks de Redes Neurais
  (Projetão) e adicionar `requirements.txt`/`environment.yml` onde faltam.
- **Organização:** resolver as duplicações e pastas com nome trocado
  (`mini projeto 03` vs `Mini Projeto 03 Redes neurais`; `Lista_07_SO` contendo a
  Lista 08; `Computcao_Evolutiva` grafado sem "a").
- **Completar ou remover** os stubs (`Main.py` vazios em ProjetoCavalo/Jogo_Velha,
  `SudokuProject` Java, `evolutionary_computation`).
