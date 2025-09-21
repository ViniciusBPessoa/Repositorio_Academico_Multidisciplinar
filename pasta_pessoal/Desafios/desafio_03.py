valor1 = 2
valor2 = 10

def separador(valor1 : int, valor2 : int) -> list:
    lista_final = [x for x in range(valor1, valor2 + 1) if x % 2 == 0]
    return lista_final

print(separador(valor1, valor2))