# models/drn.py
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models
from .modules import GlobalAttention

class DRN(nn.Module):
    """Density Regression Network - accepts single-channel weight map"""
    def __init__(self, pretrained=True):
        super().__init__()
        vgg = models.vgg16_bn(pretrained=pretrained).features
        # modify first conv to receive 1 channel
        first = vgg[0]
        if isinstance(first, nn.Conv2d):
            new_first = nn.Conv2d(1, first.out_channels,
                                  kernel_size=first.kernel_size,
                                  stride=first.stride,
                                  padding=first.padding)
            with torch.no_grad():
                # init: sum original rgb weights to approximate
                new_first.weight[:] = first.weight.sum(dim=1, keepdim=True)
                if first.bias is not None:
                    new_first.bias[:] = first.bias
            vgg[0] = new_first
        self.vgg = vgg
        self.global_att = GlobalAttention(512)
        self.out_conv = nn.Sequential(
            nn.Conv2d(512, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 1, kernel_size=1)
        )

    def forward(self, weight):
        x = weight
        for layer in self.vgg:
            x = layer(x)
        x = self.global_att(x)
        density = self.out_conv(x)
        return density
