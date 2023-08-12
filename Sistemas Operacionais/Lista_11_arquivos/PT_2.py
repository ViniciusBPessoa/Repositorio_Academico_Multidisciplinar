def transcrever_para_lista(texto):
    trans_dict = {"(": "AP", ")": "FP"}
    lista = []

    for char in texto:
        if char in trans_dict:
            lista.append(trans_dict[char])
        else:
            lista.append(char)

    return lista

# Exemplo de uso
# S(B(CCS(IKK)K)K)
entrada = "KBKSKKK"
lista_saida = transcrever_para_lista(entrada)
print(lista_saida)

def format_list(lst):
    return ', '.join(lst)

formatted_lst = format_list(lista_saida)
print(f'[{formatted_lst}]')

