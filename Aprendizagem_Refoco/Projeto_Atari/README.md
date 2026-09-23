# Projeto Atari: DQN e PPO no Space Invaders

Projeto da disciplina de **Aprendizagem por Reforço**. Treina agentes para jogar **Space Invaders** do Atari (`ALE/SpaceInvaders-v5`, via Gymnasium) de duas formas: com uma implementação própria de **DQN** em PyTorch e com o **PPO** do Stable-Baselines3, cujos hiperparâmetros são ajustados com o Optuna.

## Como funciona

### DQN (implementação própria)

- **Pré-processamento dos frames** (`wrappers/atari_wrappers.py`): o jogo começa com FIRE, o agente repete a ação e pega o máximo entre frames (`MaxAndSkipEnv`), as imagens são redimensionadas para 84×84 em escala de cinza, os valores são normalizados e os últimos frames são empilhados.
- **Rede Q** (`modelos/dqn_models.py`): rede convolucional `DQNNet`, além de uma `MLP` genérica.
- **Treino** (`DQN_aux/DQN_aux.py`): buffer de experiências (replay buffer), escolha de ação ε-greedy e cálculo da perda com uma *target network*.
- **Vídeos** (`video/video_play.py`): grava episódios do agente jogando com a rede treinada.

### PPO (Stable-Baselines3)

- O `main_PPO.ipynb` treina o PPO com `make_atari_env` e `VecFrameStack`.
- Os hiperparâmetros (como `n_steps` e `gamma`) são buscados com o **Optuna**, numa faixa de 50% a 150% dos valores originais. Os estudos ficam salvos em `stud_PPO2.db` (SQLite).

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `main.py` | script de treino do DQN (salva os pesos e atualiza a target network periodicamente) |
| `main.ipynb` | treino do DQN passo a passo (1,2 milhão de passos) |
| `main AD_INFINITUN.ipynb` | versão do DQN com treino mais longo (3 milhões de passos) |
| `main_PPO.ipynb` | PPO com Stable-Baselines3 + otimização com Optuna |
| `opa.ipynb` | leitura dos logs do TensorBoard para gerar gráficos |
| `models/` | modelos salvos durante o treino |
| `dqn-atari/` | vídeo de um episódio do agente |

## Como executar

```bash
pip install torch gymnasium[atari] ale-py stable-baselines3 optuna tensorboard tensorflow opencv-python matplotlib numpy pygame
python main.py
```

Ou abra os notebooks e execute as células em ordem.

## Tecnologias

Python · PyTorch · Gymnasium (ALE) · Stable-Baselines3 · Optuna · TensorBoard · OpenCV
