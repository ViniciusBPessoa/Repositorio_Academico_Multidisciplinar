# models/wgn.py
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models
from .modules import LRFEM, MLFCM

class WGN(nn.Module):
    """Weight Map Generation Network"""
    def __init__(self, pretrained=True):
        super().__init__()
        vgg = models.vgg16_bn(pretrained=pretrained).features
        self.vgg = vgg
        # channel sizes after pool1..pool5 for vgg16_bn: 64,128,256,512,512
        self.lrfem = LRFEM(64, 128, 256)
        self.mlfcm = MLFCM([64, 128, 256, 512], mid_channels=256)

        self.att_head = nn.Sequential(
            nn.Conv2d(256, 128, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 1, 1)
        )
        self.prob_head = nn.Sequential(
            nn.Conv2d(256, 128, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 1, 1)
        )

    def forward(self, x):
        # extract feature maps at pool boundaries
        fmaps = []
        cur = x
        pool_idx = [6, 13, 23, 33, 43]
        for i, layer in enumerate(self.vgg):
            cur = layer(cur)
            if i in pool_idx:
                fmaps.append(cur)
        f1, f2, f3, f4, f5 = fmaps  # shapes as VGG outputs

        f1e, f2e, f3e = self.lrfem(f1, f2, f3)
        fused = self.mlfcm([f1e, f2e, f3e, f4])  # BxCxhxw

        att = torch.sigmoid(self.att_head(fused))
        prob = torch.sigmoid(self.prob_head(fused))
        weight = torch.min(att, prob)
        return weight, att, prob
