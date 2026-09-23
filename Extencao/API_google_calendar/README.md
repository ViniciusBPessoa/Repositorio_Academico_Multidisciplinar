# Integração com a API do Google Calendar

Material do **projeto de extensão**: um notebook que mostra como usar a API do Google Calendar em Python para criar, buscar e apagar eventos na agenda.

## O que o notebook faz

- **Autenticação OAuth2** (`get_credentials`): usa o `credentials.json` do Google Cloud e guarda o token em `token.pickle`, para não precisar fazer login toda vez.
- **Criar evento** (`adicionar_evento`): com título, local, descrição, início e fim no fuso `America/Sao_Paulo`, e lembretes por e-mail (1 dia antes) e por popup (10 minutos antes).
- **Buscar eventos** dos próximos N dias (`buscar_eventos`) ou das próximas N horas (`buscar_eventos_por_horas`).
- **Apagar evento** pelo ID (`deletar_evento`).

A função `main()` testa o fluxo completo: cria um evento de teste, lista os eventos da semana e das próximas 24 horas e apaga o evento criado.

## Como executar

1. A pasta já tem um `credentials.json` (credenciais OAuth do tipo "web"). Para usar as suas, crie um projeto no [Google Cloud Console](https://console.cloud.google.com/), ative a **Google Calendar API**, gere as credenciais OAuth e salve como `credentials.json` nesta pasta. Como o notebook abre o login em `localhost:8080`, cadastre `http://localhost:8080/` como URI de redirecionamento autorizado.
2. Instale as dependências:

   ```bash
   pip install google-api-python-client google-auth-oauthlib google-auth-httplib2 jupyter
   ```

3. Abra o `API_CALENDAR.ipynb` e execute as células. Na primeira vez, o navegador vai pedir para você autorizar o acesso à sua agenda.

## Tecnologias

Python · Google Calendar API · OAuth2 (`google-auth-oauthlib`)
