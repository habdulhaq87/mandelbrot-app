import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mandelbrot_set_3d(width, height, max_iter, x_min, x_max, y_min, y_max):
    """Generate the Mandelbrot set data for a 3D plot."""
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C, dtype=complex)
    mask = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        not_diverged = np.abs(Z) <= 2
        Z[not_diverged] = Z[not_diverged]**2 + C[not_diverged]
        mask[not_diverged] += 1
    
    return X, Y, mask

def plot_mandelbrot_3d(X, Y, Z, cmap='plasma'):
    """Plot the Mandelbrot set in 3D."""
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=cmap, edgecolor='none')
    ax.set_title("3D Mandelbrot Set", fontsize=16)
    ax.set_xlabel("Real Axis", fontsize=12)
    ax.set_ylabel("Imaginary Axis", fontsize=12)
    ax.set_zlabel("Iterations", fontsize=12)
    ax.view_init(elev=30, azim=135)  # Adjust viewing angle
    return fig

# Streamlit page configuration
st.set_page_config(
    page_title="3D Mandelbrot Set Visualization",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Main page title and description
st.title("🌌 3D Mandelbrot Set Visualization")
st.markdown(
    """
    Explore the Mandelbrot set in 3D! The height of the plot represents the number of iterations 
    before divergence for each point in the complex plane. Adjust the settings in the sidebar to customize the view.
    """
)

# Sidebar for input parameters
st.sidebar.header("🎛 Visualization Settings")
with st.sidebar.expander("Adjust Parameters"):
    width = st.slider("Width (pixels)", 100, 1000, 500, step=50)
    height = st.slider("Height (pixels)", 100, 1000, 500, step=50)
    max_iter = st.slider("Max Iterations", 10, 500, 100, step=10)
    cmap = st.selectbox("Color Map", ["viridis", "plasma", "magma", "cividis", "hot"])

with st.sidebar.expander("Adjust Axis Ranges"):
    x_min, x_max = st.slider("X-axis Range", -3.0, 3.0, (-2.0, 1.0))
    y_min, y_max = st.slider("Y-axis Range", -3.0, 3.0, (-1.5, 1.5))

# Generate and display Mandelbrot set
st.write("### Mandelbrot Set in 3D")
st.spinner("Generating Mandelbrot set...")
X, Y, Z = mandelbrot_set_3d(width, height, max_iter, x_min, x_max, y_min, y_max)
fig = plot_mandelbrot_3d(X, Y, Z, cmap=cmap)
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown(
    """
    Created with ❤️ using [Streamlit](https://streamlit.io), [Matplotlib](https://matplotlib.org), 
    and [mpl_toolkits.mplot3d](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html).  
    Learn more about the Mandelbrot set on [Wikipedia](https://en.wikipedia.org/wiki/Mandelbrot_set).
    """
)
