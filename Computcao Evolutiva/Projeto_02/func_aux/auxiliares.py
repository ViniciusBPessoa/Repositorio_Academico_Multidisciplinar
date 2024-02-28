import numpy as np

from copy import deepcopy
import random
import torch
import torch.nn as nn

import pickle


def escolhe_acao(rede_neural, imagem):
    estado_array = np.array(imagem)
    estado_tensor = torch.tensor(estado_array, dtype=torch.float32)
    estado_tensor = estado_tensor.unsqueeze(0)
    saida = rede_neural(estado_tensor)
    _, acao = torch.max(saida, dim=1)
    acao = int(acao.item())
    # Retorna a ação escolhida
    return acao

# Exemplo de função de seleção de pais (se você deseja implementá-la)
def seleciona_pais(geracao_atual, n_selecionados):
    parents = sorted(geracao_atual, key=lambda x: x[1], reverse=True)[:n_selecionados]
    return [rede for rede, _ in parents] # retorna lista ordenada porém só as redes

def computacao_evolutiva_mutador_Cpais(n_geracao, pais, lr):
    nextgen = n_geracao - len(pais)
    nextgenindividuals = []
    for x in range(nextgen): 
        index = x % (len(pais) - 1) # 
        nextgenindividuals.append(aplica_mutacao(pais[index], lr))
        
    return nextgenindividuals + pais
        

def computacao_evolutiva_mutador_Spais(n_geracao, pais, lr):
    nextgenindividuals = []
    for x in range(n_geracao): 
        index = x % (len(pais) - 1) # 
        nextgenindividuals.append(aplica_mutacao(pais[index], lr))
    
    return nextgenindividuals

def aplica_mutacao(rede_neural, learning_rate):
    rede_mutada = deepcopy(rede_neural)
    for nome_parametro, parametro in rede_mutada.named_parameters():
        if 'weight' in nome_parametro:  # Apenas aplicar mutação aos pesos
            with torch.no_grad():
                parametro += learning_rate * torch.randn_like(parametro)
    return rede_mutada

def salvar_dados(dados, nome_arquivo):
    """Salva os dados em um arquivo usando pickle."""
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(dados, arquivo)
    print(f'Dados salvos em {nome_arquivo}.')

def recarregar_dados(nome_arquivo):
    """Recarrega os dados de um arquivo usando pickle."""
    with open(nome_arquivo, 'rb') as arquivo:
        dados = pickle.load(arquivo)
    print(f'Dados recarregados de {nome_arquivo}.')
    return dados

def calcular_media(lista):
    """Calcula a média de uma lista."""
    if not lista:
        return 0  # Retorna 0 se a lista estiver vazia para evitar divisão por zero
    return sum(lista) / len(lista)