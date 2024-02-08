import collections
import numpy as np

import random
import torch
import torch.nn as nn

from torch.utils.tensorboard import SummaryWriter

experiencia = collections.namedtuple('experiência', field_names=['estado', 'acao', 'recompenca', 'done', 'novo_estado'])

class DQNExperienceBuffer:
    def __init__(self, capacidade):
        self.buffer = collections.deque(maxlen=capacidade)

    def append(self, s1, a, r, done, s2):
        experience = experiencia(s1, a, r, done, s2)
        self.buffer.append(experience)

    def sample(self, len_amostra):
        indices = np.random.choice(len(self.buffer), len_amostra, replace=False)

        states, actions, rewards, dones, next_states = zip(*[self.buffer[indice] for indice in indices])
        return np.array(states), np.array(actions), np.array(rewards, dtype=np.float32), np.array(dones, dtype=np.uint8), np.array(next_states)
    
    def __len__(self):
        return len(self.buffer)

# Faz uma escolha epsilon-greedy
def choose_action(qnet, env, state, epsilon):

    """
    Escolhe uma ação de acordo com uma política epsilon-greedy baseada nos valores Q estimados pela rede neural 'qnet'.
    - qnet: A rede neural que representa a função Q.
    - env: O ambiente em que o agente está interagindo.
    - state: O estado atual do ambiente.
    - epsilon: O valor do parâmetro da política "epsilon-greedy" usado para escolher a ação.
    Retorna a ação escolhida pelo agente (aleatoria ou baseada da qnet).
    """

    if random.random() < epsilon:
        acao = env.action_space.sample()
    else:
        state_a = np.array([state], copy=False)
        state_v = torch.tensor(state_a, dtype=torch.float32)
        q_vals_v = qnet(state_v)
        _, act_v = torch.max(q_vals_v, dim=1)
        acao = int(act_v.item())
    return acao

    
def calc_loss(batch, net, tgt_net, gamma):
    """
    Calcula a perda (loss) para uma única amostra de lote (batch) de experiências.
    - batch: Uma tupla contendo estados, ações, recompensas, indicadores de término e próximos estados.
    - net: A rede neural que representa a função Q.
    - tgt_net: A rede neural alvo (target network) usada para calcular os valores de Q futuros.
    - gamma: Fator de desconto para recompensas futuras.
    Retorna a perda calculada usando a função de erro quadrático médio (MSE) entre os valores Q preditos e os valores Q alvo.
    """

    states, actions, rewards, dones, next_states = batch

    states_v = torch.tensor(states, dtype=torch.float32)
    next_states_v = torch.tensor(next_states, dtype=torch.float32)
    actions_v = torch.tensor(actions, dtype=torch.int64)
    rewards_v = torch.tensor(rewards, dtype=torch.float32)
    done_mask = torch.tensor(dones, dtype=torch.bool)

    state_action_values = net(states_v).gather(1, actions_v.unsqueeze(-1)).squeeze(-1)
    next_state_values = tgt_net(next_states_v).max(dim=1)[0]
    next_state_values[done_mask] = 0.0

    target_state_action_values = rewards_v + gamma * next_state_values
    loss = nn.functional.mse_loss(state_action_values, target_state_action_values)
    return loss
