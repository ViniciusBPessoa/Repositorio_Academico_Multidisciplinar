# utils/density.py
import numpy as np
import cv2

def generate_density_map(shape, points, sigma=4):
    """
    shape: (H, W)
    points: list of (x, y) or numpy array Nx2 (x:col, y:row)
    sigma: gaussian std
    returns: HxW float32 numpy array
    """
    H, W = shape
    density = np.zeros((H, W), dtype=np.float32)
    if len(points) == 0:
        return density
    ksize = int(6 * sigma + 1)
    if ksize % 2 == 0:
        ksize += 1
    gk = cv2.getGaussianKernel(ksize, sigma)
    gk2d = gk @ gk.T
    khalf = ksize // 2
    for (x, y) in points:
        xi = int(round(x))
        yi = int(round(y))
        if xi < 0 or yi < 0 or xi >= W or yi >= H:
            continue
        x1 = max(0, xi - khalf)
        y1 = max(0, yi - khalf)
        x2 = min(W - 1, xi + khalf)
        y2 = min(H - 1, yi + khalf)

        g_x1 = khalf - (xi - x1)
        g_y1 = khalf - (yi - y1)
        g_x2 = g_x1 + (x2 - x1)
        g_y2 = g_y1 + (y2 - y1)

        density[y1:y2+1, x1:x2+1] += gk2d[g_y1:g_y2+1, g_x1:g_x2+1]
    return density
