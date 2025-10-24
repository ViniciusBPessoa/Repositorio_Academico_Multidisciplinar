# train.py
import os
import torch
from torch.utils.data import DataLoader
from models.wafnet import WAFNet
from data.dataset import CrowdDataset
from torch.optim import Adam
from tqdm import tqdm

def train_loop(root_data, epochs=10, batch_size=1, lr=1e-5, device='cuda'):
    device = torch.device(device if torch.cuda.is_available() else 'cpu')
    ds = CrowdDataset(root_data, img_size=(384,384), sigma=4, downsample=32)
    loader = DataLoader(ds, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True)

    model = WAFNet(pretrained=True, lambda_w=0.8).to(device)
    optimizer = Adam(model.parameters(), lr=lr)

    for ep in range(epochs):
        model.train()
        total_loss = 0.0
        for batch in tqdm(loader, desc=f"Epoch {ep+1}/{epochs}"):
            img = batch['img'].to(device)           # Bx3xHxW
            gt_den = batch['gt_density'].to(device) # Bx1xh'xw' (downsampled)
            gt_w = batch['gt_weight'].to(device)    # Bx1xHxW (same as weight output)
            optimizer.zero_grad()
            out = model(img, gt_density=gt_den, gt_weight=gt_w)
            loss = out['loss']
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        avg_loss = total_loss / len(loader)
        print(f"Ep {ep+1} - loss: {avg_loss:.4f}")
        # salvar checkpoint simples
        ckpt_path = f"checkpoint_ep{ep+1}.pth"
        torch.save({'model': model.state_dict(), 'optimizer': optimizer.state_dict()}, ckpt_path)
        print("Saved", ckpt_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, required=True, help='root data folder (images/ and annots/)')
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--bs', type=int, default=1)
    parser.add_argument('--lr', type=float, default=1e-5)
    args = parser.parse_args()
    train_loop(args.data, epochs=args.epochs, batch_size=args.bs, lr=args.lr)
