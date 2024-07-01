from __future__ import print_function
import datetime
import os.path
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Se modificando esses escopos, apague o arquivo token.pickle
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    creds = None
    # O arquivo token.pickle armazena os tokens de acesso e atualização do usuário e é
    # criado automaticamente quando o fluxo de autorização é concluído pela primeira vez.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Se não houver credenciais válidas disponíveis, faça o login do usuário.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Salva as credenciais para a próxima execução
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Adiciona um evento ao Google Calendar
    event = {
        'summary': 'Reunião de Teste',
        'location': 'Remoto',
        'description': 'Reunião de teste via API do Google Calendar.',
        'start': {
            'dateTime': '2024-07-01T20:00:00-03:00',
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': '2024-07-01T21:00:00-03:00',
            'timeZone': 'America/Sao_Paulo',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Evento criado: %s' % (event.get('htmlLink')))

if __name__ == '__main__':
    main()
