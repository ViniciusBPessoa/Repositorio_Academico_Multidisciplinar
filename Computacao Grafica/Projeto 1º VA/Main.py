import os
import sys
import webbrowser
from time import sleep

# Inicio da brincadeira
import pygame

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from arquivos import gerenciador_arquivos # gerencia as malhas e as cameras
from arquivos.auxiliares.aux_main import loader_malha, loader_normal_Hxy

def plota_obj(janela, pontos, cor_ponto, faces, estado = 3):
    for ponto in pontos:
        pygame.draw.rect(janela, cor_ponto, (ponto[0], ponto[1], 1, 1))

    if estado == 3 or estado == 2:

        for face in faces:
            for aresta in face:
                for ponto in aresta:
                    pygame.draw.rect(janela, cor_ponto, (ponto[0], ponto[1], 1, 1))

pygame.init()

resolu = [1366, 720] # define a largura e altura da tela respectivamente
tela = pygame.display.set_mode((resolu[0], resolu[1]))
pygame.display.set_caption('3D Objects')

# carrega a camera (sera a mesma todo o projeto)
gerenciador_camera = gerenciador_arquivos.Gerenciador_camera()
gerenciador_camera.carregar_camera("camera01")
normal_Hxy = loader_normal_Hxy(gerenciador_camera)

# Carregador de malha apenas instancia a classe
gerenciador_modelo = gerenciador_arquivos.Gerenciador_Modelo() 

estado_plot = 3
loader_malha(gerenciador_modelo, gerenciador_camera, "triangulo", normal_Hxy, resolu)

executando = True
while executando:
    tela.fill((0,0,0)) # limpa a tela para o loop

    # Verificação de eventos
    for evento in pygame.event.get(): # encerra no X
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.KEYDOWN: # tecla apertada
            if evento.key == pygame.K_r:
                loader_malha(gerenciador_modelo, gerenciador_camera, gerenciador_modelo.nome_malha_atual, normal_Hxy, resolu)

            if evento.key == pygame.K_t:
                while True:
                    verificador = input("Qual o nome do arquivo da malha (T = retornar): ")
                    if verificador != "T":
                        verificador = loader_malha(gerenciador_modelo, gerenciador_camera, verificador, normal_Hxy, resolu)
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
            
            if evento.key == pygame.K_1:
                estado_plot = 1
            if evento.key == pygame.K_2:
                estado_plot = 2
            if evento.key == pygame.K_3:
                estado_plot = 3
            
            if evento.key == pygame.K_7:
                webbrowser.open("https://www.youtube.com/watch?v=VBJvDgBZEi4")

    plota_obj(tela, gerenciador_modelo.malha_perspectiva, (255,255,255), gerenciador_modelo.rasteiros, estado_plot)

    # Atualiza a tela
    pygame.display.update()

# Finaliza o codigo
pygame.quit()
