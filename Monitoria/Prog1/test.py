#Questão 3

pessoas_sexo = ["M", "F", "F", "M", "M", "F", "F", "M", "F", "M"]
pessoas_altura = [1.75, 1.60, 1.68, 1.80, 1.72, 1.55, 1.62, 1.78, 1.58, 1.74]

print(f"maior: {max(pessoas_altura)} menor: {min(pessoas_altura)}")

contador = 0

for pessoa in pessoas_sexo:
    if pessoa == "M":
        contador += 1
print(f"Numero de homens: {contador}")

pessoa_mais = max(pessoas_altura)
indice_pessoa_mais = pessoas_altura.index(pessoa_mais)
print(f"sexo pessso mais alta: {pessoas_sexo[indice_pessoa_mais]}")

auturas_mulheres = []

for p in range(len(pessoas_sexo)):
    if pessoas_sexo[p] == "F":
        auturas_mulheres.append(pessoas_altura[p])
    
print(f"Media altura mulheres: {sum(auturas_mulheres)/len(auturas_mulheres):.3f}")