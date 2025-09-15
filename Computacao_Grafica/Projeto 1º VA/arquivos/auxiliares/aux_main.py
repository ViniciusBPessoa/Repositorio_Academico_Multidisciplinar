def loader_malha(gerenciador_modelo, gerenciador_camera, modelo, normal_Hxy, resolu): # carrega a malha
    verificador = gerenciador_modelo.carregar_malha(modelo)
    if verificador != -1:
        gerenciador_modelo.projecao_malha(gerenciador_camera.get_Matrix_mudanca(), gerenciador_camera.camera_atual["C"], normal_Hxy, resolu)
    return verificador

def loader_normal_Hxy(gerenciador_camera): # carrega os valores para rasteirização (perspectiva)
    return [gerenciador_camera.camera_atual["d"][0] / gerenciador_camera.camera_atual["Hx"][0], gerenciador_camera.camera_atual["d"][0] / gerenciador_camera.camera_atual["Hy"][0]]
