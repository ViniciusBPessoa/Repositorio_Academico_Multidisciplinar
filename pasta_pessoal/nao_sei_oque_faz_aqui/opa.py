def trianguloRetangulo(base : int):
    return ["*"*x for x in range(1, base + 1)]


for x in trianguloRetangulo(5):
    print(x)
