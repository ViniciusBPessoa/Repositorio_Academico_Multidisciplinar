import requests

BASE_URL = 'http://localhost:8000'

def criar_usuario():
    """Cria um novo usuário no sistema"""
    print("\n✅ Criando usuário...")
    data = {
        "nome": "Ana Paula",
        "email": "ana.paula@email.com",
        "telefone": "987654321",
        "password": "senhaInicial2025"
    }
    response = requests.post(f"{BASE_URL}/usuario/", json=data)
    print("Status:", response.status_code)
    print("Resposta:", response.json())

def obter_token():
    """Obtém token JWT para autenticação"""
    print("\n🔑 Obtendo token JWT...")
    data = {
        "email": "ana.paula@email.com",
        "password": "senhaInicial2025"
    }
    response = requests.post(f"{BASE_URL}/api/token/", json=data)
    print("Status:", response.status_code)
    print("Resposta:", response.json())
    return response.json().get("access")

def login_com_jwt():
    """Realiza login e exibe tokens JWT (access + refresh)"""
    print("\n🔐 Login com JWT (access + refresh)...")
    data = {
        "email": "ana.paula@email.com",
        "password": "senhaInicial2025"
    }
    response = requests.post(f"{BASE_URL}/api/token/", json=data)
    print("Status:", response.status_code)
    print("Resposta:", response.json())

def obter_user_id_por_email(token, email):
    """Busca o ID do usuário pelo email"""
    print("\n🔍 Buscando ID do usuário por e-mail...")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/usuario/", headers=headers)
    if response.status_code == 200:
        for usuario in response.json():
            if usuario.get("email") == email:
                print(f"✅ Usuário encontrado: {usuario['id']}")
                return usuario["id"]
    print("❌ Usuário não encontrado.")
    return None

def trocar_senha(token, user_id):
    """Altera a senha do usuário autenticado"""
    print("\n🔄 Trocando senha...")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "senha_atual": "senhaInicial2025",
        "nova_senha": "senhaNova2025"
    }
    response = requests.post(f"{BASE_URL}/usuario/{user_id}/trocar-senha/", json=data, headers=headers)
    print("Status:", response.status_code)
    print("Resposta:", response.json())

if __name__ == "_main_":
    criar_usuario()                         # 1. Cria usuário
    token = obter_token()                  # 2. Gera token
    login_com_jwt()                        # 3. Exibe login JWT
    user_id = obter_user_id_por_email(token, "ana.paula@email.com")  # 4. Busca ID
    if user_id:
        trocar_senha(token, user_id)       # 5. Troca senha