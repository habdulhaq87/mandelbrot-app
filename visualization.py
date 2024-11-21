import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(width, height, max_iter, x_min, x_max, y_min, y_max):
    """
    Generate the Mandelbrot set image.
    
    Parameters:
    - width: int, image width in pixels.
    - height: int, image height in pixels.
    - max_iter: int, maximum number of iterations to determine divergence.
    - x_min, x_max: float, range of the real axis.
    - y_min, y_max: float, range of the imaginary axis.

    Returns:
    - mask: 2D numpy array of iteration counts for each point.
    """
    # Create a grid of complex numbers
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C, dtype=complex)
    mask = np.zeros(C.shape, dtype=int)

    # Perform iterations with early escape optimization
    for i in range(max_iter):
        not_diverged = np.abs(Z) <= 2
        Z[not_diverged] = Z[not_diverged]**2 + C[not_diverged]
        mask[not_diverged] += 1

    # Normalize the mask for better visualization
    mask = (mask / max_iter * 255).astype(np.uint8)
    return mask

def plot_mandelbrot(mask, cmap='hot', x_range=(-2, 1), y_range=(-1.5, 1.5)):
    """
    Plot the Mandelbrot set using matplotlib.
    
    Parameters:
    - mask: 2D numpy array, Mandelbrot set data.
    - cmap: str, colormap for the visualization.
    - x_range: tuple of floats, range of the real axis.
    - y_range: tuple of floats, range of the imaginary axis.
    
    Returns:
    - fig: Matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    extent = [x_range[0], x_range[1], y_range[0], y_range[1]]
    ax.imshow(mask, cmap=cmap, extent=extent, interpolation="nearest")
    ax.set_title("Mandelbrot Set", fontsize=18, weight="bold")
    ax.set_xlabel("Real Axis", fontsize=14)
    ax.set_ylabel("Imaginary Axis", fontsize=14)
    ax.tick_params(axis='both', labelsize=12)
    ax.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.5)
    return fig
