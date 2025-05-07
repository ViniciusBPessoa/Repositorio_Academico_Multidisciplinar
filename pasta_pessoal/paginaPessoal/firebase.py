import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

# Configuração inicial
load_dotenv()  # Carrega variáveis do .env

# Verifica se o arquivo de credenciais existe
SERVICE_ACCOUNT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "serviceAccountKey.json")
if not os.path.exists(SERVICE_ACCOUNT_PATH):
    raise FileNotFoundError(f"Arquivo de credenciais não encontrado em: {SERVICE_ACCOUNT_PATH}")

# Inicializa o Firebase
cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)

# Acesso ao Firestore
db = firestore.client()

# Dados em inglês para a coleção "Informations"
ENGLISH_DATA = {
    "Github": "ViniciusBPessoa",
    "description": "I am a Computer Science student at the Federal Rural University of Pernambuco (UFRPE), currently in my seventh semester. My passion for artificial intelligence guided my choice of optional courses throughout the program. I am seeking my first professional experience where I can apply the knowledge I've acquired and continue learning.",
    "knowledge": "Knowledge",
    "knowledge-description": "Bachelor's degree in Computer Science at the Federal Rural University of Pernambuco (UFRPE). For more information about languages and frameworks, visit my GitHub:",
    "name": "Vinicius Bezerra",
    "presentation": "Hello, I'm",
    "language": "english"
}

def create_english_document():
    try:
        # Referência ao documento específico "english" na coleção "Informations"
        doc_ref = db.collection("Informations").document("english")
        
        # Define os dados do documento
        doc_ref.set(ENGLISH_DATA)
        
        print(f"✅ Documento 'english' criado/atualizado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar documento: {str(e)}")
        return False

if __name__ == "__main__":
    print("="*50)
    print("Iniciando criação do documento 'english' no Firestore")
    print("="*50)
    
    # Verifica variáveis de ambiente essenciais
    required_vars = ["REACT_APP_FIREBASE_API_KEY", "REACT_APP_FIREBASE_PROJECT_ID"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"⚠️ Variáveis de ambiente faltando: {', '.join(missing_vars)}")
    else:
        success = create_english_document()
        if success:
            print("🎉 Operação concluída com sucesso!")
        else:
            print("🔴 Falha na operação. Verifique os logs acima.")