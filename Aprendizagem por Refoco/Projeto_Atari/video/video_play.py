# Baseada na minha versão (Pablo)
import gymnasium as gym

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
