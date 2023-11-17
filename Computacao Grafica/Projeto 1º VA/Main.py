import pygame
import os
import sys

diretorio_modelos = os.path.dirname(os.path.abspath(__file__))  # Para executar sempre (Carrega a devida localização)
sys.path.append(diretorio_modelos)

from arquivos import gerenciador_arquivos


pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Modelador')

gerenciador_modelo = gerenciador_arquivos.GerenciadorModelo()
gerenciador_modelo.carregar_malha()

executando = True
while executando:

    tela.fill((0,0,0))

    # Verificação de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                print("Hallo, world")


    # Atualiza a tela
    pygame.display.update()

# Finaliza o Pygame
pygame.quit()
