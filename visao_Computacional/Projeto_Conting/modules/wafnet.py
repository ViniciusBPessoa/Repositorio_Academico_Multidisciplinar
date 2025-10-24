# models/wafnet.py
import torch
import torch.nn as nn
from .wgn import WGN
from .drn import DRN

class WAFNet(nn.Module):
    def __init__(self, pretrained=True, lambda_w=0.8):
        super().__init__()
        self.wgn = WGN(pretrained=pretrained)
        self.drn = DRN(pretrained=pretrained)
        self.lambda_w = lambda_w
        self.criterion = nn.MSELoss()

    def forward(self, img, gt_density=None, gt_weight=None):
        # img: Bx3xHxW
        weight, att, prob = self.wgn(img)               # weight: Bx1xhxw
        density = self.drn(weight)                      # density: Bx1xh2xw2 (reduced)
        out = {'weight': weight, 'att': att, 'prob': prob, 'density': density}
        if gt_density is not None and gt_weight is not None:
            # if shapes differ, upsample density to gt or downsample gt_density accordingly outside
            ld = self.criterion(density, gt_density)
            lw = self.criterion(weight, gt_weight)
            loss = ld + self.lambda_w * lw
            out.update({'loss': loss, 'ld': ld, 'lw': lw})
        return out
