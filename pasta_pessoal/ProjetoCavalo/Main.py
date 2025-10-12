import matplotlib.pyplot as plt

def main():
    temperaturas = []
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", 
             "agosto", "setembro", "outubro", "novembro", "dezembro"]

    print("Por favor, insira a temperatura média para cada mês do ano:")
    for mes in meses:
        while True:
            try:
                temp = float(input(f"Temperatura média de {mes}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    # 1. Média anual
    media_anual = sum(temperaturas) / len(temperaturas)
    print(f"\nTemperatura média anual: {media_anual:.2f}°C")

    # 2. Mês mais quente e mais frio
    mes_mais_quente_idx = temperaturas.index(max(temperaturas))
    mes_mais_quente = meses[mes_mais_quente_idx]
    temp_mais_quente = temperaturas[mes_mais_quente_idx]
    print(f"Mês mais quente: {mes_mais_quente} com {temp_mais_quente:.2f}°C")

    mes_mais_frio_idx = temperaturas.index(min(temperaturas))
    mes_mais_frio = meses[mes_mais_frio_idx]
    temp_mais_frio = temperaturas[mes_mais_frio_idx]
    print(f"Mês mais frio: {mes_mais_frio} com {temp_mais_frio:.2f}°C")

    # 3. Meses acima da média
    meses_acima_media = [meses[i] for i, temp in enumerate(temperaturas) if temp > media_anual]
    if meses_acima_media:
        print(f"Meses com temperatura acima da média anual: {', '.join(meses_acima_media)}")
    else:
        print("Nenhum mês teve temperatura acima da média anual.")