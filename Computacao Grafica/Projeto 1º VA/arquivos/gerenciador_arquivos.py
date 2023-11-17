def carregar_arquivo_modelo(nome_modelo="default"):
    with open(f"/modelos/{nome_modelo}.txt", "r") as modelo:
        linhas = modelo.readline
    return linhas

print(carregar_arquivo_modelo("casa"))
