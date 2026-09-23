# Página Pessoal: Scripts do Firestore

Scripts de apoio ao meu site de portfólio, que guarda os dados no **Firebase Firestore**.

## Scripts

- **`firebase.py`**: cria e atualiza o documento `english` da coleção `Informations` com a versão em inglês dos meus dados de perfil (apresentação e conhecimentos).
- **`firebaseTradutor.py`**: apaga a coleção `projects-ing` e a recria a partir de `projects`, traduzindo os textos de português para inglês com o **Google Gemini** (`gemini-1.5-pro`). A tradução mantém o markdown e a formatação originais.

## Como executar

1. Baixe a chave da conta de serviço do Firebase como `serviceAccountKey.json` e coloque nesta pasta.
2. Crie um `.env` com `REACT_APP_FIREBASE_API_KEY` e `REACT_APP_FIREBASE_PROJECT_ID` (usados pelo `firebase.py`) e configure a chave da API do Gemini no `firebaseTradutor.py`.
3. Instale as dependências e rode o script desejado:

   ```bash
   pip install firebase-admin google-generativeai python-dotenv
   python firebaseTradutor.py
   ```

## Tecnologias

Python · Firebase Admin SDK (Firestore) · Google Gemini API · python-dotenv
