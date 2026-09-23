import random
import time

# 🎬 Catálogo com seus filmes/séries
catalogo = {
    "devoradores de estrelas": 10.0,
    "harry potter": 9.9,
    "Interestelar": 9.8,
    "Minecraft": 9.1,
    "hobit": 9.0,
    "bominavel": 9.7,
    "guardiões da galaxia": 9.9,
    "fate saga winx": 9.9,
    "rebelde": 10,
    "witchwatch": 9.9,
    "wandinha": 8.9,
    "jumanji": 10.0,
    "de volta para o futuro": 10,
    "spy family": 8.9,
    "pokemon": 9.5
}


def linha():
    print("=" * 55)


def boas_vindas():
    linha()
    print("🎬🎮  FILMES & SÉRIES - AVALIAÇÕES  🎮🎬")
    linha()
    print(""" █████╗ ██╗   ██╗ █████╗ ██╗     ██╗ █████╗  ██████╗  ██████╗ ███████╗███████╗
██╔══██╗██║   ██║██╔══██╗██║     ██║██╔══██╗██╔════╝ ██╔════╝ ██╔════╝██╔════╝
███████║██║   ██║███████║██║     ██║███████║██║  ███╗██║  ███╗█████╗  ███████╗
██╔══██║╚██╗ ██╔╝██╔══██║██║     ██║██╔══██║██║   ██║██║   ██║██╔══╝  ╚════██║
██║  ██║ ╚████╔╝ ██║  ██║███████╗██║██║  ██║╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝""")
          
    print("Bem-vindo ao seu sistema de avaliações ⭐")
    time.sleep(1)
    mostrar_comandos()


def mostrar_comandos():
    print("📋 COMANDOS:")
    print("[1] Ver lista")
    print("[2] Adicionar")
    print("[3] Remover")
    print("[4] Alterar nota")
    print("[5] Sortear item")
    print("[6] Mostrar comandos")
    print("[0] Sair")
    linha()


def mostrar_lista():
    print("\n🎞️ LISTA:")
    if len(catalogo) == 0:
        print("Lista vazia.")
    else:
        for nome, nota in catalogo.items():
            print(f"• {nome} → ⭐ {nota}")
    linha()


def adicionar():
    print("\n➕ Adicionar item")
    nome = input("Nome: ").strip()

    if nome == "":
        print("⚠️ Nome inválido.")
        linha()
        return

    if nome in catalogo:
        print("⚠️ Já existe.")
        linha()
        return

    try:
        nota = float(input("Nota (0 a 10): "))
        if 0 <= nota <= 10:
            catalogo[nome] = nota
            print("✅ Adicionado com sucesso!")
        else:
            print("⚠️ Nota inválida.")
    except:
        print("⚠️ Digite um número válido.")

    linha()


def remover():
    print("\n🗑️ Remover item")
    nome = input("Nome: ").strip()

    if nome in catalogo:
        del catalogo[nome]
        print("✅ Removido!")
    else:
        print("⚠️ Não encontrado.")

    linha()


def alterar():
    print("\n✏️ Alterar nota")
    nome = input("Nome: ").strip()

    if nome not in catalogo:
        print("⚠️ Não encontrado.")
        linha()
        return

    try:
        nova = float(input("Nova nota (0 a 10): "))
        if 0 <= nova <= 10:
            catalogo[nome] = nova
            print("✅ Atualizado!")
        else:
            print("⚠️ Nota inválida.")
    except:
        print("⚠️ Digite um número válido.")

    linha()


def sortear():
    print("\n🎲 Sorteando...")
    if len(catalogo) == 0:
        print("Lista vazia.")
    else:
        nome = random.choice(list(catalogo.keys()))
        print(f"🎯 {nome} → ⭐ {catalogo[nome]}")
    linha()


def main():
    boas_vindas()

    while True:
        cmd = input("Escolha: ").strip()

        if cmd == "1":
            mostrar_lista()
        elif cmd == "2":
            adicionar()
        elif cmd == "3":
            remover()
        elif cmd == "4":
            alterar()
        elif cmd == "5":
            sortear()
        elif cmd == "6":
            mostrar_comandos()
        elif cmd == "0":
            print("👋 Até mais!")
            break
        else:
            print("⚠️ Comando inválido.")
            linha()


# 🚀 Executar
main()