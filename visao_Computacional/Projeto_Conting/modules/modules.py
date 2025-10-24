# models/modules.py
import torch
import torch.nn as nn
import torch.nn.functional as F

def conv3x3(in_c, out_c):
    return nn.Sequential(
        nn.Conv2d(in_c, out_c, kernel_size=3, padding=1, bias=True),
        nn.ReLU(inplace=True)
    )

class LRFEM(nn.Module):
    """Low-Resolution Feature Enhancement Module
       Input: features f1, f2, f3 (shallow -> deeper)
       Output: enhanced versions (f1e, f2e, f3e)
    """
    def __init__(self, c1, c2, c3):
        super().__init__()
        self.conv1 = conv3x3(c1, c1)
        self.conv2 = conv3x3(c2, c2)
        self.conv3 = conv3x3(c3, c3)
        # fusions
        self.fuse12 = conv3x3(c1 + c2, c2)
        self.fuse23 = conv3x3(c2 + c3, c3)

    def forward(self, f1, f2, f3):
        f1a = self.conv1(f1)
        f2a = self.conv2(f2)
        f3a = self.conv3(f3)

        # upsample f3 -> f2
        f3_up = F.interpolate(f3a, size=f2a.shape[2:], mode='bilinear', align_corners=False)
        f2_cat = torch.cat([f2a, f3_up], dim=1)
        f2e = self.fuse12(f2_cat)

        # upsample f2e -> f1
        f2_up = F.interpolate(f2e, size=f1a.shape[2:], mode='bilinear', align_corners=False)
        f1_cat = torch.cat([f1a, f2_up], dim=1)
        # compress to c3 via fuse23 (intencional reusage; shapes chosen to be workable)
        f1e = self.fuse23(f1_cat)

        f3e = f3a
        return f1e, f2e, f3e

class MLFCM(nn.Module):
    """Multi-Layer Feature Compilation Module"""
    def __init__(self, in_channels_list, mid_channels=256):
        super().__init__()
        total_in = sum(in_channels_list)
        self.reduce = nn.Sequential(
            nn.Conv2d(total_in, mid_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(mid_channels, mid_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        self.proj = nn.Conv2d(mid_channels, mid_channels, kernel_size=1)

    def forward(self, feature_list):
        # resize all to the largest spatial resolution
        max_h = max([f.shape[2] for f in feature_list])
        max_w = max([f.shape[3] for f in feature_list])
        ups = [F.interpolate(f, size=(max_h, max_w), mode='bilinear', align_corners=False) for f in feature_list]
        cat = torch.cat(ups, dim=1)
        out = self.reduce(cat)
        out = self.proj(out)
        return out

class GlobalAttention(nn.Module):
    """Non-local / global attention block (lightweight)"""
    def __init__(self, in_channels):
        super().__init__()
        self.q = nn.Conv2d(in_channels, in_channels // 8, kernel_size=1)
        self.k = nn.Conv2d(in_channels, in_channels // 8, kernel_size=1)
        self.v = nn.Conv2d(in_channels, in_channels, kernel_size=1)
        self.gamma = nn.Parameter(torch.zeros(1))

    def forward(self, x):
        B, C, H, W = x.size()
        q = self.q(x).view(B, -1, H*W)          # B x C' x N
        k = self.k(x).view(B, -1, H*W)          # B x C' x N
        v = self.v(x).view(B, -1, H*W)          # B x C x N

        attn = torch.bmm(q.permute(0,2,1), k)   # B x N x N
        attn = F.softmax(attn, dim=-1)
        out = torch.bmm(v, attn.permute(0,2,1)) # B x C x N
        out = out.view(B, C, H, W)
        return self.gamma * out + x
