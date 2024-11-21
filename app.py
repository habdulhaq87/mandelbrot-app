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
        not_diverged = np.abs(Z) <= 2
        Z[not_diverged] = Z[not_diverged]**2 + C[not_diverged]
        mask[not_diverged] += 1
        
    return mask

def plot_mandelbrot(mask, cmap='hot'):
    """Plot the Mandelbrot set."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(mask, cmap=cmap, extent=[-2, 2, -2, 2])
    ax.set_title("Mandelbrot Set", fontsize=16)
    ax.set_xlabel("Real Axis", fontsize=12)
    ax.set_ylabel("Imaginary Axis", fontsize=12)
    ax.tick_params(axis='both', which='major', labelsize=10)
    return fig

# Set page configuration
st.set_page_config(
    page_title="Mandelbrot Set Visualization",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Main page title and description
st.title("🌀 Mandelbrot Set Visualization")
st.markdown(
    """
    Explore the fascinating Mandelbrot set, a fractal defined by the behavior of complex numbers.
    Use the sidebar to customize the resolution, iterations, and color map.
    """
)

# Sidebar for inputs
st.sidebar.header("🎨 Visualization Settings")
with st.sidebar.expander("Adjust Parameters"):
    width = st.slider("Width (pixels)", 400, 1200, 800, step=100)
    height = st.slider("Height (pixels)", 400, 1200, 800, step=100)
    max_iter = st.slider("Max Iterations", 50, 1000, 200, step=50)
    cmap = st.selectbox("Color Map", ["hot", "plasma", "viridis", "magma", "cividis"])

with st.sidebar.expander("Adjust Axis Ranges"):
    x_min, x_max = st.slider("X-axis Range", -3.0, 3.0, (-2.0, 1.0))
    y_min, y_max = st.slider("Y-axis Range", -3.0, 3.0, (-1.5, 1.5))

# Generate and display Mandelbrot set
st.write("### Mandelbrot Set Output")
st.write("Use the controls in the sidebar to customize the visualization.")
st.spinner("Generating Mandelbrot set...")
mask = mandelbrot_set(width, height, max_iter, x_min, x_max, y_min, y_max)
fig = plot_mandelbrot(mask, cmap=cmap)
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown(
    """
    Created with ❤️ using [Streamlit](https://streamlit.io) and [Matplotlib](https://matplotlib.org).  
    Explore more about the Mandelbrot set [here](https://en.wikipedia.org/wiki/Mandelbrot_set).
    """
)
