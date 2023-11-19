import pygame
import os
import sys

diretorio_modelos = os.path.dirname(os.path.abspath(__file__))  # Para executar sempre (Carrega a devida localização)
sys.path.append(diretorio_modelos)

from arquivos import gerenciador_arquivos


pygame.init()

largura, altura = 1366, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Modelador')

gerenciador_modelo = gerenciador_arquivos.Gerenciador_Modelo()
gerenciador_modelo.carregar_malha("piramide")

executando = True
while executando:

    tela.fill((0,0,0))

    # Verificação de eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_r:
                gerenciador_modelo.carregar_malha(gerenciador_modelo.nome_malha_atual)

            if evento.key == pygame.K_t:
                print("Hallo, world")
            
            if evento.key == pygame.K_SPACE:
                gerenciador_modelo.exibir_malha()

            if evento.key == pygame.K_ESCAPE:
                executando = False


    # Atualiza a tela
    pygame.display.update()

# Finaliza o Pygame
pygame.quit()
