with open('texto.txt') as arquivo:        
    linhas = arquivo.readlines()
    lista_palavas = []
    for linha in linhas:
        palavras = linha.split()
        for palavra in palavras:
            lista_palavas.append(palavra)

    

#resultado 01

n_letras = 0
for palavra in lista_palavas:
    for letra in palavra:
        n_letras += len(palavra)

print(f"O numero total de letras é: {n_letras}")

#resultado 02

n_palavras = 0
for palavra in lista_palavas:
    n_palavras += 1

print(f"O numero total de palavras é: {n_palavras}")


#resultado 03

lista_palavra_chamada = []
for palavra in lista_palavas:
    if palavra not in lista_palavra_chamada:
        lista_palavra_chamada.append(palavra)

for palavra in lista_palavra_chamada:
    print(f"A palavra {palavra}, aparece {lista_palavas.count(palavra)} vezes.")

