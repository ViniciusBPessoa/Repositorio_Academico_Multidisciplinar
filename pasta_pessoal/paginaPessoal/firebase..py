import firebase_admin
from firebase_admin import credentials, firestore
import os

# Configuração do Firebase (use suas variáveis de ambiente ou coloque diretamente)
firebase_config = {
    "apiKey": "AIzaSyDtY6oA_lzypny__HKwm_5UgQ8tgoKiyxk",
    "authDomain": "curriculo-74e65.firebaseapp.com",
    "projectId": "curriculo-74e65",
    "storageBucket": "curriculo-74e65.firebasestorage.app",
    "messagingSenderId": "688101883159",
    "appId": "1:688101883159:web:edcb8daf858137bb598b52",
    "measurementId": "G-GXSCXVXJPV"
}

# Inicializar o Firebase
cred = credentials.Certificate("serviceAccountKey.json")  # Você precisa baixar este arquivo do Firebase Console
firebase_admin.initialize_app(cred)

db = firestore.client()

# Dados em português (exemplo)
original_data = {
    "Github": "ViniciusBPessoa",
    "description": "Sou estudante de Ciências da Computação na Universidade Federal Rural de Pernambuco (UFRPE), atualmente no sétimo período. Minha paixão pela inteligência artificial orientou a escolha das disciplinas opcionais ao longo do curso. Estou em busca da minha primeira experiência profissional, onde posso aplicar os conhecimentos adquiridos e continuar a aprender.",
    "knowledge": "Conhecimentos",
    "knowledge-description": "Graduação em Ciências da Computação na Universidade Federal Rural de Pernambuco (UFRPE) Para mais informações sobre linguagens e frameworks, visite meu GitHub:",
    "name": "Vinicius Bezerra",
    "presentation": "Olá, eu sou o"
}

# Tradução para inglês (você pode usar uma API de tradução ou fazer manualmente)
translated_data = {
    "Github": "ViniciusBPessoa",  # Mantém igual
    "description": "I am a Computer Science student at the Federal Rural University of Pernambuco (UFRPE), currently in my seventh semester. My passion for artificial intelligence guided my choice of optional courses throughout the program. I am seeking my first professional experience where I can apply the knowledge I've acquired and continue learning.",
    "knowledge": "Knowledge",
    "knowledge-description": "Bachelor's degree in Computer Science at the Federal Rural University of Pernambuco (UFRPE). For more information about languages and frameworks, visit my GitHub:",
    "name": "Vinicius Bezerra",  # Mantém igual
    "presentation": "Hello, I'm"
}

def add_english_version():
    # Referência para a coleção (substitua "collection_name" pelo nome real da sua coleção)
    collection_ref = db.collection("collection_name")
    
    # Adiciona o documento em inglês
    doc_ref = collection_ref.add(translated_data)
    
    print(f"Documento em inglês adicionado com ID: {doc_ref.id}")

if __name__ == "__main__":
    add_english_version()