import os
import sys
import webbrowser

# Inicio da brincadeira
import pygame

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from arquivos import gerenciador_arquivos # gerencia as malhas e as cameras

pygame.init()

largura, altura = 1366, 720 # define a largura e altura da tela respectivamente
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('3D Objects')

# carrega a camera (sera a mesma todo o projeto)
gerenciador_camera = gerenciador_arquivos.Gerenciador_camera()
gerenciador_camera.carregar_camera("camera01")

# Carregador de malha apenas instancia a classe
gerenciador_modelo = gerenciador_arquivos.Gerenciador_Modelo() 

def loader_malha(gerenciador_modelo, gerenciador_camera, modelo):
    verificador = gerenciador_modelo.carregar_malha(modelo)
    if verificador != -1:
        gerenciador_modelo.projecao_malha(gerenciador_camera.get_Matrix_mudanca(), gerenciador_camera.camera_atual["C"], gerenciador_camera.camera_atual["d"][0])
    return verificador

loader_malha(gerenciador_modelo, gerenciador_camera, "piramide")

executando = True
while executando:
    tela.fill((0,0,0)) # limpa a tela para o loop

    # Verificação de eventos
    for evento in pygame.event.get(): # encerra no X
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.KEYDOWN: # tecla apertada
            if evento.key == pygame.K_r:
                loader_malha(gerenciador_modelo, gerenciador_camera, gerenciador_modelo.nome_malha_atual)

            if evento.key == pygame.K_t:
                while True:
                    verificador = input("Qual o nome do arquivo da malha (T = retornar): ")
                    if verificador != "T":
                        verificador = loader_malha(gerenciador_modelo, gerenciador_camera, verificador)
                        if verificador != -1:
                            break
                        else:
                            print("Arquivo não encontrado")
                            continue
                    else: 
                        break
                
            if evento.key == pygame.K_SPACE:
                gerenciador_modelo.exibir_malha()

            if evento.key == pygame.K_ESCAPE:
                executando = False
            
            if evento.key == pygame.K_7:
                webbrowser.open("https://www.youtube.com/watch?v=VBJvDgBZEi4")

    # Atualiza a tela
    pygame.display.update()

# Finaliza o codigo
pygame.quit()
