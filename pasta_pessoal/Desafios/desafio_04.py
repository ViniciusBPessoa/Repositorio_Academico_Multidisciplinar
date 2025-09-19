
numero = 0
numero_real = 0.0
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
    except:
        print("Valor inválido. Tente novamente.")
        continue
    break

while True:
    try:
        numero_real = float(input("Digite um número real: "))
    except:
        print("Valor inválido. Tente novamente.")
        continue
    break

print(f"O número inteiro digitado foi: {numero}")
print(f"O número real digitado foi: {numero_real}")