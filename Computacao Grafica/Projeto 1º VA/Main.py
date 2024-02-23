import os
import sys
import webbrowser

# Inicio da brincadeira
import pygame

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from arquivos.gerenciador_arquivos import *  # gerencia as malhas e as cameras
from arquivos.auxiliares.aux_main import loader_malha, loader_normal_Hxy

def plota_obj(janela, gerenciador_modelo : Gerenciador_Modelo, cor_ponto, estado = 2, Z_buffer = [], is_buffer = True):  # função responsavel por plotar todos os pontos em tela
    
    if is_buffer:
        for linha in range(len(Z_buffer)):
            for coluna in range(len(Z_buffer[0])):
                if Z_buffer[linha][coluna] != -1:
                    pygame.draw.rect(janela, cor_ponto, (linha, coluna, 1, 1))
    else:
        for ponto in gerenciador_modelo.malha_perspectiva: # plota os pontos 
            pygame.draw.rect(janela, cor_ponto, (ponto[0], ponto[1], 1, 1))

        if estado == 3 or estado == 2: # verifica os imputs do usuario

            for face in gerenciador_modelo.rasteiros: # plota as linhas incluindo a linha de devisão dos triangulos
                for aresta in face:
                    for ponto in aresta:
                        pygame.draw.rect(janela, cor_ponto, (ponto[0], ponto[1], 1, 1))
            
            if estado == 3:  # estado de plot total (pontos linhas e conteudo)
                for linha in gerenciador_modelo.preenchimento:
                    if len(linha) != 0:
                        for ponto in linha:
                            pygame.draw.rect(janela, cor_ponto, (ponto[0], ponto[1], 1, 1))

pygame.init() # inicializador do pygame 
quadra =720
resolu = [quadra, quadra] # define a largura e altura da tela respectivamente
tela = pygame.display.set_mode((resolu[0], resolu[1])) # cria a tela
pygame.display.set_caption('3D Objects') # da nome a tela

# carrega a camera (sera a mesma todo o projeto)
gerenciador_camera = Gerenciador_camera()
gerenciador_camera.carregar_camera("camera01", resolucao=resolu)
Z_buffer = gerenciador_camera.Z_buffer
normal_Hxy = loader_normal_Hxy(gerenciador_camera)

is_zbf = True

# Carregador de malha apenas instancia a classe
gerenciador_modelo = Gerenciador_Modelo() 

estado_plot = 2
_, Z_buffer = loader_malha(gerenciador_modelo, gerenciador_camera, "triangulo", normal_Hxy, resolu, Z_buffer)

executando = True # variavel responsavel por manter a tela aberta
while executando: # loop principal
    tela.fill((0,0,0)) # limpa a tela para o loop

    # Verificação de eventos
    for evento in pygame.event.get(): # coleta os eventos EX: inputs 
        if evento.type == pygame.QUIT: # encerra no X
            executando = False
        
        if evento.type == pygame.KEYDOWN: # tecla apertada
            if evento.key == pygame.K_r: # R recarrega a malha
                Z_buffer = gerenciador_camera.carregar_Z_buffer(resolu)
                _, Z_buffer = loader_malha(gerenciador_modelo, gerenciador_camera, gerenciador_modelo.nome_malha_atual, normal_Hxy, resolu, Z_buffer)

            if evento.key == pygame.K_t: # voce pode dijitar no console a nova malha e ela sera devidamante carregada
                while True:
                    verificador = input("Qual o nome do arquivo da malha (T = retornar): ")
                    if verificador != "T":
                        Z_buffer = gerenciador_camera.carregar_Z_buffer(resolu)
                        verificador, Z_buffer = loader_malha(gerenciador_modelo, gerenciador_camera, verificador, normal_Hxy, resolu, Z_buffer)
                        if verificador != -1:
                            break
                        else:
                            print("Arquivo não encontrado")
                            continue
                    else: 
                        break
                
            if evento.key == pygame.K_SPACE: # em caso de espaço todos os valores da malha seram exibidos
                gerenciador_modelo.exibir_malha()

            if evento.key == pygame.K_ESCAPE: # escape fecha o programa
                executando = False
            
            # Area que coleta os valores de uso do programa 1 = apenas pontos, 2 = pontos e linhas(junto a linha de divisão do triangulo), 3 = tudo

            if evento.key == pygame.K_1:
                estado_plot = 1
            if evento.key == pygame.K_2:
                estado_plot = 2
            if evento.key == pygame.K_3:
                estado_plot = 3
            if evento.key == pygame.K_z:
                if is_zbf:
                    is_zbf = False
                else:
                    is_zbf = True
            
            if evento.key == pygame.K_7: # 7 faz coisas
                webbrowser.open("https://www.youtube.com/watch?v=VBJvDgBZEi4")

    gerenciador_camera.Z_buffer = Z_buffer
    plota_obj(tela, gerenciador_modelo, (255,255,255), estado_plot, Z_buffer, is_zbf) # plota todos os valores em tela

    # Atualiza a tela
    pygame.display.update()

# Finaliza o codigo
pygame.quit()
