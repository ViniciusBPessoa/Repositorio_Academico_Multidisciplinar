import pickle

# Dicionário de exemplo
meu_dicionario = {'a': 1, 'b': 2, 'c': 3}

# Salvar o dicionário em um arquivo
with open('meu_dicionario.pkl', 'wb') as arquivo:
    pickle.dump(meu_dicionario, arquivo)

# Carregar o dicionário do arquivo
with open('meu_dicionario.pkl', 'rb') as arquivo:
    dicionario_carregado = pickle.load(arquivo)

# Verificar se o dicionário foi carregado corretamente
print(dicionario_carregado)