def transcrever_para_lista(texto):
    trans_dict = {"(": "AP", ")": "FP", "+":"ADD", "-": "SUB", "*":"MUL", "<" : "LT"}
    lista = []

    for char in texto:
        if char in trans_dict:
            lista.append(trans_dict[char])
        else:
            lista.append(char)

    return lista

# Exemplo de uso
# S(B(CCS(IKK)K)K)
entrada = "S(K(SII))(S(S(KS)K)(K(SII)))(S(S(KS)(S(S(KS)(S(S(KS)(S(S(KS)(KI))(S(KK)(K2))))(S(KK)(K<))))(KI)))(S(S(KS)(S(S(KS)(S(S(KS)(S(KK)I))(S(S(KS)(S(S(KS)(KI))(S(KK)(K1))))(S(KK)(K-)))))(S(S(KS)(S(KK)I))(S(S(KS)(S(S(KS)(KI))(S(KK)(K2))))(S(KK)(K-))))))(S(KK)(K+))))"
lista_saida = transcrever_para_lista(entrada)
print(lista_saida)

def format_list(lst):
    return ', '.join(lst)

formatted_lst = format_list(lista_saida)
print(f'[{formatted_lst}]')

