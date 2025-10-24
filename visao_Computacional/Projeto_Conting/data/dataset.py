# data/dataset.py
import os
import torch
from torch.utils.data import Dataset
import cv2
import numpy as np
from utils.density import generate_density_map

class CrowdDataset(Dataset):
    """
    Espera:
      root/
        images/
          img1.jpg
          img2.jpg
        annots/
          img1.npy   -> Nx2 array: [[x,y],[x,y],...]
          img2.npy
    Para produção: adapte para ShanghaiTech, UCF-QNRF, etc.
    """
    def __init__(self, root, img_size=(384,384), transform=None, sigma=4, downsample=32):
        self.root = root
        self.img_dir = os.path.join(root, "images")
        self.ann_dir = os.path.join(root, "annots")
        self.images = sorted(os.listdir(self.img_dir))
        self.img_size = img_size
        self.transform = transform
        self.sigma = sigma
        self.downsample = downsample

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        name = self.images[idx]
        img_path = os.path.join(self.img_dir, name)
        annot_path = os.path.join(self.ann_dir, os.path.splitext(name)[0] + ".npy")
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        H0, W0 = img.shape[:2]

        # simple center-crop / resize to img_size
        img_resized = cv2.resize(img, (self.img_size[1], self.img_size[0]))
        img_t = img_resized.astype(np.float32) / 255.0
        img_t = (img_t - 0.5) / 0.5  # normalize to approx [-1,1]
        img_t = np.transpose(img_t, (2,0,1))  # C,H,W

        # load points
        if os.path.exists(annot_path):
            pts = np.load(annot_path)  # Nx2: (x,y) relative to original image size
            # scale points to resized image
            scale_x = self.img_size[1] / float(W0)
            scale_y = self.img_size[0] / float(H0)
            pts = np.array([[p[0]*scale_x, p[1]*scale_y] for p in pts])
        else:
            pts = np.zeros((0,2))

        # generate density map at original resized size
        den = generate_density_map((self.img_size[0], self.img_size[1]), pts, sigma=self.sigma)
        # optionally downsample density to match network output resolution (e.g., 1/32)
        if self.downsample is not None and self.downsample > 1:
            h_ds = self.img_size[0] // self.downsample
            w_ds = self.img_size[1] // self.downsample
            den_ds = cv2.resize(den, (w_ds, h_ds), interpolation=cv2.INTER_LINEAR)
            # scale sum to keep count consistent
            den_ds = den_ds * ( (den.sum() + 1e-8) / (den_ds.sum() + 1e-8) )
        else:
            den_ds = den

        # build a simple weight GT: prob_map = normalized density, att_map = gaussian blurred binary mask
        prob_map = den / (den.max() + 1e-8)
        # att_map: create binary around points
        att_map = np.zeros_like(prob_map, dtype=np.float32)
        for (x,y) in pts:
            xi = int(round(x)); yi = int(round(y))
            if 0 <= yi < att_map.shape[0] and 0 <= xi < att_map.shape[1]:
                att_map[max(0, yi-2):min(att_map.shape[0], yi+3),
                        max(0, xi-2):min(att_map.shape[1], xi+3)] = 1.0
        # blur att_map lightly
        att_map = cv2.GaussianBlur(att_map, (7,7), 2)
        weight_gt = np.minimum(prob_map, att_map)

        sample = {
            'img': torch.from_numpy(img_t).float(),
            'gt_density': torch.from_numpy(den_ds[np.newaxis, ...]).float(),
            'gt_weight': torch.from_numpy(weight_gt[np.newaxis, ...]).float(),
            'gt_count': torch.tensor([float(len(pts))], dtype=torch.float32)
        }
        return sample
