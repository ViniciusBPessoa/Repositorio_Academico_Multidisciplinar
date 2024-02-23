def loader_malha(gerenciador_modelo, gerenciador_camera, modelo, normal_Hxy, resolu, Z_buffer): # carrega a malha
    verificador = gerenciador_modelo.carregar_malha(modelo)
    if verificador != -1:
        z_bff = gerenciador_modelo.projecao_malha(gerenciador_camera.get_Matrix_mudanca(), gerenciador_camera.camera_atual["C"], gerenciador_camera.camera_atual["d"], normal_Hxy, resolu, Z_buffer)
    return verificador, z_bff

def loader_normal_Hxy(gerenciador_camera): # carrega os valores para rasteirização (perspectiva)
    return [gerenciador_camera.camera_atual["Hx"][0], gerenciador_camera.camera_atual["Hy"][0]]

