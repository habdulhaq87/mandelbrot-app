import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(width, height, max_iter, x_min, x_max, y_min, y_max):
    """Generate the Mandelbrot set image."""
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C, dtype=complex)
    mask = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        Z = Z**2 + C
        mask += (np.abs(Z) < 2)
        
    return mask

def plot_mandelbrot(mask, cmap='hot'):
    """Plot the Mandelbrot set."""
    fig, ax = plt.subplots()
    ax.imshow(mask, cmap=cmap, extent=[-2, 2, -2, 2])
    ax.set_title("Mandelbrot Set")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    return fig

# Streamlit interface
st.title("Mandelbrot Set Visualization")

# Sidebar for inputs
st.sidebar.header("Visualization Settings")
width = st.sidebar.slider("Width (pixels)", 400, 1200, 800)
height = st.sidebar.slider("Height (pixels)", 400, 1200, 800)
max_iter = st.sidebar.slider("Max Iterations", 50, 1000, 200)
x_min, x_max = st.sidebar.slider("X-axis Range", -3.0, 3.0, (-2.0, 1.0))
y_min, y_max = st.sidebar.slider("Y-axis Range", -3.0, 3.0, (-1.5, 1.5))
cmap = st.sidebar.selectbox("Color Map", ["hot", "plasma", "viridis", "magma"])

# Generate and display the Mandelbrot set
st.sidebar.text("Generating...")
mask = mandelbrot_set(width, height, max_iter, x_min, x_max, y_min, y_max)
fig = plot_mandelbrot(mask, cmap=cmap)
st.pyplot(fig)
