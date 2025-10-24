# infer.py
import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt
from models.wafnet import WAFNet
from data.dataset import CrowdDataset

def visualize(img_np, weight, density, save_path=None):
    # img_np: HxWx3 (0-255) ; weight density: tensors 1x1xHxW or smaller
    img_v = img_np.copy()
    # upsample weight/density to image size
    weight_np = weight.squeeze().cpu().numpy()
    density_np = density.squeeze().cpu().numpy()
    # normalize for display
    w_vis = (weight_np - weight_np.min()) / (weight_np.max() - weight_np.min() + 1e-8)
    d_vis = (density_np - density_np.min()) / (density_np.max() - density_np.min() + 1e-8)
    w_img = cv2.applyColorMap((w_vis*255).astype(np.uint8), cv2.COLORMAP_JET)
    d_img = cv2.applyColorMap((d_vis*255).astype(np.uint8), cv2.COLORMAP_VIRIDIS)
    h, w = img_v.shape[:2]
    w_img = cv2.resize(w_img, (w, h))
    d_img = cv2.resize(d_img, (w, h))
    blend_w = cv2.addWeighted(img_v, 0.6, w_img, 0.4, 0)
    blend_d = cv2.addWeighted(img_v, 0.6, d_img, 0.4, 0)
    fig, axs = plt.subplots(1,3, figsize=(15,6))
    axs[0].imshow(img_v[...,::-1]); axs[0].set_title("Image"); axs[0].axis('off')
    axs[1].imshow(blend_w[...,::-1]); axs[1].set_title("Weight map"); axs[1].axis('off')
    axs[2].imshow(blend_d[...,::-1]); axs[2].set_title("Density map"); axs[2].axis('off')
    if save_path:
        fig.savefig(save_path)
    plt.show()

def run_inference(img_path, ckpt_path=None, device='cuda'):
    device = torch.device(device if torch.cuda.is_available() else 'cpu')
    model = WAFNet(pretrained=False).to(device)
    if ckpt_path:
        ck = torch.load(ckpt_path, map_location=device)
        model.load_state_dict(ck['model'])
    model.eval()
    # simple single-image dataset wrapper (reuse dataset logic)
    # here expect an image and dummy annotation; for quick demo we'll read & resize
    img = cv2.imread(img_path)
    H, W = img.shape[:2]
    img_res = cv2.resize(img, (384,384))
    img_t = img_res.astype('float32')/255.0
    img_t = (img_t - 0.5)/0.5
    img_t = np.transpose(img_t, (2,0,1))
    img_tensor = torch.from_numpy(img_t).unsqueeze(0).float().to(device)
    with torch.no_grad():
        out = model(img_tensor)
    weight = out['weight']    # Bx1xhxw
    density = out['density']  # Bx1xh2xw2
    # upsample density to weight size for visualization (approx)
    dens_up = torch.nn.functional.interpolate(density, size=weight.shape[2:], mode='bilinear', align_corners=False)
    visualize(img_res, weight[0:1], dens_up[0:1])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', type=str, required=True)
    parser.add_argument('--ckpt', type=str, default=None)
    args = parser.parse_args()
    run_inference(args.img, args.ckpt)
