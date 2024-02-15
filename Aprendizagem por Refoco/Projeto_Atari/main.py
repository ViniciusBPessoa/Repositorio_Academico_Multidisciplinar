import pygame
import sys
from os import path, getcwd

from os import path
sys.path.append( path.dirname( path.dirname( path.abspath("__main__") ) ) )


import time
from datetime import datetime
import collections

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


import matplotlib.pyplot as plt
from modelos import dqn_models
from wrappers.atari_wrappers import *

import gymnasium as gym

inicio = time.time()

# verifica a disponibilidade da GPU
if torch.cuda.is_available():
    is_gpu = torch.device("cuda")
else:
    is_gpu = torch.device("cpu")

torch.set_default_device(is_gpu) # instanciando onde a rede neural deve rodar 
from DQN_aux.DQN_aux import *

# Baseada na minha versão (Pablo)
def record_video_q_neuralnet(env_name, qnet, episodes=3, folder='videos/', prefix='rl-video', epsilon=0.0):
    """
    Grava um vídeo a partir de uma política epsilon-greedy definida pela 'qtable' e pelo valor de 'epsilon'.
    - env_name: A string do ambiente cadastrada no gymnasium ou uma instância da classe. Ao final, o ambiente é fechado (função `close()`).
    - qnet: A rede neural que representa a função Q.
    - episodes: Número de episódios completos que serão executados.
    - prefiz: Prefixo do nome dos arquivos de vídeo.
    - folder: Pasta onde os arquivos de vídeo serão salvos.
    - epsilon: Valor do parâmetro da política "epsilon-greedy" usada para escolher as ações.
    """
    if isinstance(env_name, str):
        env = gym.make(env_name, render_mode="rgb_array")
    else:
        env = env_name
    rec_env = gym.wrappers.RecordVideo(env, folder, episode_trigger=lambda i : True, name_prefix=prefix)
    num_steps = 0
    for epi in range(episodes):
        state, _ = rec_env.reset()
        num_steps += 1
        epi_reward = 0.0
        done = False
        while not done:
            action = choose_action(qnet, env, state, epsilon)
            state, r, termi, trunc, _ = rec_env.step(action)
            done = termi or trunc
            num_steps += 1
            epi_reward += r
        print(f"Episode {epi}: {num_steps} steps / return {epi_reward:.2f}")
    rec_env.close()
    env.close()

def DQN_TRAIN(env, env_name, gamma, qnet, qnet_lr, target_qnet, target_update_freq, replay_size, batch_size, epsilon_f, epsilon_decay_period, NUM_STAPS):

    """
    Treina um agente utilizando o algoritmo Deep Q-Network (DQN) em um ambiente de aprendizado por reforço.

    Args:
        env: O ambiente de aprendizado por reforço. Pode ser uma instância da classe do ambiente ou uma string 
            que representa o nome do ambiente registrado no Gym.
        env_name (str): O nome do ambiente (usado para fins de logging e salvamento).
        gamma (float): O fator de desconto para recompensas futuras.
        qnet (torch.nn.Module): A rede neural que representa a função Q.
        qnet_lr (float): A taxa de aprendizado para o otimizador Adam utilizado para treinar a rede neural.
        target_qnet (torch.nn.Module): A rede neural que representa a função Q-alvo.
        target_update_freq (int): A frequência com que os pesos da rede alvo são atualizados.
        replay_size (int): O tamanho do buffer de experiência usado para amostragem durante o treinamento.
        batch_size (int): O tamanho do lote usado para atualizar os pesos da rede neural.
        epsilon_f (float): O valor inicial de epsilon para a política epsilon-greedy.
        epsilon_decay_period (int): O período de decaimento para o valor de epsilon.
        NUM_STAPS (int): O número total de passos de treinamento a serem executados.
    """

    # Cria o otimizador, que vai fazer o ajuste dos pesos da 'qnet',
    # Usa uma técnica de gradiente descendente de destaque, chamada ADAM
    optimizer = optim.Adam(qnet.parameters(), lr=qnet_lr)

    # Para o logging de dados, para serem exibidos no tensorboard
    writer = SummaryWriter(comment="-" + env_name)

    buffer = DQNExperienceBuffer(replay_size)

    start_time_str = datetime.now().strftime("%Y-%m-%d,%H-%M-%S")
    episode_reward_list = []
    step = 0
    epsilon = 1.0

    state, _ = env.reset()
    episode_reward = 0.0
    episode_start_step = 0
    episode_start_time = time.time()

    while True:
        step += 1

        # Decaimento linear do epsilon
        epsilon = max(epsilon_f, 1.0 - step / epsilon_decay_period)

        action = choose_action(qnet, env, state, epsilon)

        # Faz um passo / Aplica uma ação no ambiente
        new_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        episode_reward += reward

        # Adiciona no buffer
        buffer.append(state, action, reward, terminated, new_state)
        state = new_state

        if done:
            episode_reward_list.append(episode_reward)
            speed = (step - episode_start_step) / (time.time() - episode_start_time + 0.00001)

            state, _ = env.reset()
            episode_reward = 0.0
            episode_start_step = step
            episode_start_time = time.time()

            # Abaixo, faz vários loggings de dados
            mean_reward = np.mean(episode_reward_list[-100:])
            print(f"{step}: finished {len(episode_reward_list)} episodes, mean reward {mean_reward:.3f}, eps {epsilon:.2f}, speed {speed:.2f} steps/s")
            writer.add_scalar("epsilon", epsilon, step)
            writer.add_scalar("epi_reward_100", mean_reward, step)
            writer.add_scalar("epi_reward", episode_reward, step)

            # Testa se "resolveu" o ambiente
            if step > NUM_STAPS:
                print(f"Solved in {step} steps with mean reward {mean_reward:.3f}")
                filename = env_name + "-" + start_time_str + ".dat"
                torch.save(qnet.state_dict(), filename)
                print(f"Model saved as {filename}")
                break

        if len(buffer) < replay_size:
            continue

        # Faz a 'tgt_net' receber os mesmos valores de pesos da 'qnet', na frequência indicada
        if step % target_update_freq == 0:
            target_qnet.load_state_dict(qnet.state_dict())

        # Escolhendo amostras aleatórios do buffer e faz uma atualização dos pesos da rede
        optimizer.zero_grad()
        batch = buffer.sample(batch_size)
        loss_t = calc_loss(batch, qnet, target_qnet, gamma)
        loss_t.backward()
        optimizer.step()

    writer.close()

    # Veja outros em: https://gymnasium.farama.org/environments/atari/
# Se mudar o jogo, lembre-se de alterar também o GOAL_REWARD abaixo!
ATARI_ENV_NAME = "ALE/SpaceInvaders-v5"

# Recompensa alvo; no Pong, esta é a diferença de pontos do player para a "cpu", sendo +21.0 o máximo e -21.0 o mínimo
# Tente com algum valor negativo (e.g. -15.0) para um treinamento mais rápido, ou algum valor positivo (+15.0) para ver o agent ganhar da "cpu"
NUM_STAPS = 1000 #0.0

# Parâmetros do DQN
GAMMA = 0.99
BATCH_SIZE = 32
REPLAY_SIZE = 20_000
LEARNING_RATE = 1e-4
SYNC_TARGET_FRAMES = 1_500

EPSILON_DECAY_PERIOD = 100_000
EPSILON_FINAL = 0.02

env2 = gym.make(ATARI_ENV_NAME)

# Aplica os wrappers do DQN para ambientes Atari
env2a = MaxAndSkipEnv(env2)
env2b = FireResetEnv(env2a)
env2c = ProcessFrame84(env2b)
env2d = ImageToPyTorch(env2c)
env2e = BufferWrapper(env2d, 4)
env2f = ScaledFloatFrame(env2e)

# Cria as redes neurais
qnet2 = dqn_models.DQNNet(env2f.observation_space.shape, env2f.action_space.n)
qtarget2 = dqn_models.DQNNet(env2f.observation_space.shape, env2f.action_space.n)

DQN_TRAIN(
    env = env2f,
    env_name = ATARI_ENV_NAME,
    gamma = GAMMA,
    qnet = qnet2,
    qnet_lr = LEARNING_RATE,
    target_qnet = qtarget2,
    target_update_freq = SYNC_TARGET_FRAMES,
    replay_size = REPLAY_SIZE,
    batch_size = BATCH_SIZE,
    epsilon_f = EPSILON_FINAL,
    epsilon_decay_period = EPSILON_DECAY_PERIOD,
    NUM_STAPS = NUM_STAPS)

print(f"Fim da função: {time.time() - inicio:0.2f}")
