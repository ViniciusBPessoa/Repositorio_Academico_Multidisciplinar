import pygame

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Modelador')

executando = True
while executando:

    tela.fill((0,0,0))

    # Verificação de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Atualiza a tela
    pygame.display.update()

# Finaliza o Pygame
pygame.quit()
