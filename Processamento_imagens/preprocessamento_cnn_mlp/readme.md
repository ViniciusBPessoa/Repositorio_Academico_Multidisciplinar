# 🧠 Classificação de Tumores Cerebrais com CNN e MLP via Pré-processamento de Imagens

## Visão Geral do Projeto

Este projeto compara o impacto de diferentes técnicas de pré-processamento de imagens na classificação de tumores cerebrais em ressonâncias magnéticas. Utilizando redes neurais convolucionais (CNN) e redes multicamadas (MLP), o estudo analisa o desempenho de cada modelo frente a múltiplas combinações de filtros, limiarizações e ajustes de contraste. Desenvolvido como parte de um projeto de extensão da UFRPE, o trabalho busca contribuir para soluções mais precisas no apoio ao diagnóstico por imagem.

## Base de Dados

* **Fonte**: [Kaggle - Brain Tumor with Bounding Boxes](https://www.kaggle.com/datasets/ahmedsorour1/mri-for-brain-tumor-with-bounding-boxes)
* **Total de imagens**: 5.249 MRI rotuladas
* **Classes**:

  * Classe 0: Glioma
  * Classe 1: Meningioma
  * Classe 2: Sem Tumor
  * Classe 3: Pituitária

### Divisão dos Dados

| Classe     | Treinamento | Validação |
| ---------- | ----------- | --------- |
| Glioma     | 1.153       | 136       |
| Meningioma | 1.449       | 140       |
| Sem Tumor  | 711         | 100       |
| Pituitária | 1.424       | 136       |

## Técnicas de Pré-processamento Avaliadas

1. **Equalização de Histograma**
2. **Ajuste de Brilho**
3. **Limiarização Binária**
4. **Filtro Gaussiano**
5. **Filtro de Mediana**
6. **Filtro Laplaciano**
7. **Normalização**
8. **Componentes Conectados**

### Combinações de Técnicas

```mermaid
graph LR
    A[Entrada - MRI 512x512] --> B[Redimensionamento 224x224]
    B --> C[Pré-processamento]
    C --> D[Extração de Características: Hu e LBP]
    D --> E[Classificação com CNN ou MLP]
```

Exemplos de combinações:

* Equalização + Brilho
* Gaussiano + Limiarização
* Mediana + Normalização + Componentes Conectados
* Laplaciano + Componentes Conectados

## 🧠 Modelos Utilizados

### CNN - Rede Neural Convolucional

* 3 camadas convolucionais + pooling
* Foco na extração automática de padrões visuais

### MLP - Rede Neural Multicamadas

* Entradas vetoriais com Momentos de Hu + LBP
* Estrutura totalmente conectada
* Ideal para processamento rápido e leve

## 📊 Resultados

| Modelo | Acurácia (Validação) |
| ------ | -------------------- |
| CNN    | 92.96%               |
| MLP    | 85.53%               |

* CNN obteve melhor desempenho, principalmente pela capacidade de extrair características diretamente das imagens.
* MLP se destacou especialmente na classe "Sem Tumor", com acurácia competitiva.

## 🔍 Conclusão

O estudo demonstrou que a CNN é mais robusta para tarefas complexas como a classificação de tumores em imagens de ressonância. No entanto, a MLP pode ser uma alternativa viável em contextos com recursos computacionais limitados, principalmente se combinada com extração eficiente de características como Momentos de Hu e LBP.

## 📁 Arquivos

| Arquivo | Conteúdo |
| ------- | -------- |
| `principal_algoritimo.ipynb` | pré-processamento, extração de características e treino da CNN e da MLP para cada combinação de técnicas |
| `Analise_result.ipynb` | análise e comparação dos resultados |
| `historicos/` | histórico de treino (`.npy`) e matriz de confusão (`.png`) de cada combinação e modelo |

## ▶️ Como Executar

1. Baixe a base no [Kaggle](https://www.kaggle.com/datasets/ahmedsorour1/mri-for-brain-tumor-with-bounding-boxes) e organize em `Data/Train` e `Data/Val` (uma pasta por classe, com as imagens em `<classe>/images`). As imagens não estão versionadas neste repositório.
2. Instale as dependências:

   ```bash
   pip install tensorflow opencv-python scikit-image scikit-learn numpy matplotlib seaborn jupyter
   ```

3. Ajuste o caminho da base no `principal_algoritimo.ipynb` e execute as células em ordem.

## 👨‍💻 Autor

* **Vinícius Pessoa** — Ciência da Computação - UFRPE

## 📫 Contato

Para dúvidas, colaborações ou interesse em expandir o projeto:

* [vinicius.pessoa@ufrpe.br](mailto:vinicius.pessoa@ufrpe.br)

---

*"A combinação de processamento de imagem e redes neurais é o caminho para diagnósticos mais rápidos e precisos em ambientes clínicos assistidos por IA."*

---

📄 **Acesse o relatório completo em PDF**:
👉 [Clique aqui para abrir no Overleaf](https://www.overleaf.com/read/pghchwjvdxbn#3057fb)

📁 **Repositório**:
🔗 [GitHub - Repositorio\_Academico\_Multidisciplinar/Processamento\_imagens/preprocessamento\_cnn\_mlp](https://github.com/ViniciusBPessoa/Repositorio_Academico_Multidisciplinar/tree/main/Processamento_imagens/preprocessamento_cnn_mlp)

---
