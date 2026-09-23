# Post: Utilizando a API do Google Gemini com Python

Material do **projeto de extensão**: um artigo em formato de notebook que ensina, passo a passo, a integrar programas Python com a API do **Google Gemini**.

## Conteúdo do artigo

1. **Configurações iniciais:** pré-requisitos, como gerar a chave de API no Google AI Studio e como guardar a chave com segurança num arquivo `.env` (com `python-dotenv`).
2. **Uso textual:** listagem dos modelos disponíveis, testes e os primeiros prompts.
3. **Uso com imagens:** envio de imagens junto com o prompt (exemplos na pasta `Imagens/`).
4. **Chat:** conversas com histórico, usando o modo de chat do modelo.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `01 - Gemini - revisado.ipynb` | artigo completo, com explicações |
| `01 - Gemini - revisado sem coment.ipynb` | a mesma versão do artigo, sem os comentários |
| `especificacoes.ipynb` | especificações dos modelos Gemini 1.5 Flash e 1.5 Pro |
| `requirements.txt` | dependências do ambiente |
| `Imagens/` | imagens usadas nos exemplos |

A pasta [`../post_comparacao`](../post_comparacao/) tem o rascunho da continuação do artigo, com a comparação entre os modelos do Gemini.

## Como executar

```bash
pip install -r requirements.txt
pip install notebook
```

Configure a sua chave no arquivo `.env` desta pasta:

```
GOOGLE_API_KEY=sua_chave_aqui
```

Depois, abra o notebook no Jupyter e execute as células em ordem.

## Tecnologias

Python · Google Gemini API (`google-generativeai`) · python-dotenv · Jupyter
