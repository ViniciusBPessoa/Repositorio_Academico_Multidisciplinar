import mpmath
import time
import multiprocessing as mp

def buscar_sequencia(pi_str, sequencia, inicio, fim, resultado, progresso, total_processos):
    """Busca a sequência em um intervalo específico de dígitos de π."""
    tam_seq = len(sequencia)

    for i in range(inicio, fim - tam_seq + 1):
        if pi_str[i:i + tam_seq] == sequencia:
            resultado.value = i + 1  # Armazena a posição (1-based)
            return

    with progresso.get_lock():
        progresso.value += 1
        print(f"Progresso: {progresso.value}/{total_processos} processos concluídos", end="\r")

def encontrar_sequencia_pi_paralelo(sequencia, casas_decimais=10_000_000, num_processos=4):
    """Procura a primeira ocorrência de uma sequência nos dígitos de π usando paralelismo."""
    if len(sequencia) > casas_decimais:
        print("Erro: A sequência é maior que o número de casas decimais especificado.")
        return

    mpmath.mp.dps = casas_decimais + 2  # Ajusta a precisão (+2 para incluir '3.')
    pi_str = str(mpmath.mp.pi)[2:]  # Remove '3.'

    print(f"Buscando a sequência {sequencia} nos primeiros {casas_decimais} dígitos de π usando {num_processos} processos...\n")
    
    inicio = time.time()

    tamanho_parte = casas_decimais // num_processos
    processos = []
    resultado = mp.Value('i', -1)  # Armazena o resultado encontrado (-1 se não encontrado)
    progresso = mp.Value('i', 0)  # Conta quantos processos já terminaram

    for i in range(num_processos):
        inicio_parte = i * tamanho_parte
        fim_parte = min((i + 1) * tamanho_parte + len(sequencia) - 1, casas_decimais)

        processo = mp.Process(target=buscar_sequencia, args=(pi_str, sequencia, inicio_parte, fim_parte, resultado, progresso, num_processos))
        processos.append(processo)
        processo.start()

    for processo in processos:
        processo.join()
    
    if resultado.value != -1:
        print(f"\nA sequência {sequencia} aparece pela primeira vez na posição {resultado.value}.")
    else:
        print(f"\nA sequência {sequencia} não foi encontrada nas primeiras {casas_decimais} casas decimais de π.")

    print(f"Tempo de execução: {time.time() - inicio:.2f} segundos.")

# Exemplo de uso
encontrar_sequencia_pi_paralelo("40028922", casas_decimais=10_000_000, num_processos=4)
