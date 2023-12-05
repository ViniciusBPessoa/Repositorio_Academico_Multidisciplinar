import pyttsx3
import os

def texto_para_voz(texto, velocidade):
    engine = pyttsx3.init()
    engine.setProperty('rate', velocidade)
    engine.say(texto)
    engine.runAndWait()

def ler_arquivo_texto(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
        return texto
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        novo_texto = input("Digite o texto que deseja salvar no arquivo: ")
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(novo_texto)
        return novo_texto

nome_arquivo = 'texto_para_falar.txt'

while True:
    input("Pressione Enter para ler o texto (ou pressione Ctrl+C para sair)...")

    texto = ler_arquivo_texto(nome_arquivo)

    velocidade_desejada = 1000000000  # Ajuste a velocidade conforme necessário
    texto_para_voz(texto, velocidade_desejada)
