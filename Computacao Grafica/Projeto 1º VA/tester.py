VA1 = 6
VA2 = 6
Fianl = 3

def metodo_j(va1, va2,final):
    auxiliar = va1 + va2
    auxiliar /= 2
    auxiliar += final
    return auxiliar/2

def Metodo_FODA(va1, va2,final):
    auxiliar = va1 + va2
    auxiliar /= 4
    auxiliar += final/2
    return auxiliar

print(f"Resultados iguais {metodo_j(VA1, VA2, Fianl)}, {Metodo_FODA(VA1, VA2, Fianl)}")