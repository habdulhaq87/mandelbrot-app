import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(width, height, max_iter, x_min, x_max, y_min, y_max):
    """
    Generate the Mandelbrot set image.
    """
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C, dtype=complex)
    mask = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        not_diverged = np.abs(Z) <= 2
        Z[not_diverged] = Z[not_diverged]**2 + C[not_diverged]
        mask[not_diverged] += 1
        
    return mask

def plot_mandelbrot(mask, cmap='hot'):
    """
    Plot the Mandelbrot set.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(mask, cmap=cmap, extent=[-2, 2, -2, 2])
    ax.set_title("Mandelbrot Set", fontsize=16)
    ax.set_xlabel("Real Axis", fontsize=12)
    ax.set_ylabel("Imaginary Axis", fontsize=12)
    ax.tick_params(axis='both', which='major', labelsize=10)
    return fig
