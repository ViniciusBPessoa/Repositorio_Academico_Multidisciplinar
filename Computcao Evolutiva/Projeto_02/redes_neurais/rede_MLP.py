import torch # Todas as redes neurais serão criados utilizando PyTorch
import torch.nn as nn
import torch.optim as optim

class MLP(nn.Module):
    def __init__(self, input_dim, list_hidden_dims, output_dim, final_activ_fn=None):
        super().__init__()
        layers = []
        last_dim = input_dim
        for dim in list_hidden_dims:
            layers.append( nn.Linear(last_dim, dim, bias=True) )
            layers.append( nn.ReLU() )
            last_dim = dim
        layers.append( nn.Linear(last_dim, output_dim, bias=True) )
        if final_activ_fn is not None:
            layers.append( final_activ_fn )
        self.layers = nn.Sequential(*layers)

    def forward(self, x):
        y = x
        for layer in self.layers:
            y = layer(y)
        return y
            