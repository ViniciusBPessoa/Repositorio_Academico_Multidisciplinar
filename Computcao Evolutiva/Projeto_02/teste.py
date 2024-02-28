import torch

# Criar um tensor de exemplo
tensor_exemplo = torch.randn((2, 3))  # Um tensor 2x3 com valores aleatórios da distribuição normal padrão

# Criar um novo tensor com a mesma forma que tensor_exemplo, mas preenchido com valores aleatórios da distribuição normal padrão
tensor_aleatorio = torch.randn_like(tensor_exemplo)

print("Tensor de exemplo:")
print(tensor_exemplo)

print("\nTensor aleatório:")
print(tensor_aleatorio)