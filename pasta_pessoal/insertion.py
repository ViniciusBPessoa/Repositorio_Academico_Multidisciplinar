import random

n = int(input("Digite a quantidade de números: "))

lista = [random.randint(0, 1000) for _ in range(n)]
lista2 = []

def sort_list(lista):
    for numero in lista:
        if len(lista2) == 0:
            lista2.append(numero)
        else:
            if numero < lista2[0]:
                lista2.insert(0, numero)
            elif numero > lista2[-1]:
                lista2.append(numero)
            else:
                for i in range(len(lista2)):
                    if numero < lista2[i]:
                        lista2.insert(i, numero)
                        break

sort_list(lista)
print("Lista original:", lista)
print("Lista ordenada:", lista2)