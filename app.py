import streamlit as st
import numpy as np
import plotly.graph_objects as go

@st.cache_data
def mandelbrot_3d(x_min, x_max, y_min, y_max, z_min, z_max, res, max_iter):
    """Generate the Mandelbrot set in 3D."""
    # Generate 3D grid
    x = np.linspace(x_min, x_max, res)
    y = np.linspace(y_min, y_max, res)
    z = np.linspace(z_min, z_max, res)
    X, Y, Z = np.meshgrid(x, y, z)
    
    # Flatten grid for vectorized operations
    C = X.flatten() + 1j * (Y.flatten() + Z.flatten() * 1j)
    Z = np.zeros_like(C, dtype=complex)
    iterations = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask]**2 + C[mask]
        iterations[mask] += 1

    # Reshape iterations to 3D and normalize
    iterations = iterations.reshape((res, res, res))
    iterations = iterations / max_iter  # Normalize for better visualization
    return X, Y, Z, iterations

# Streamlit interface
st.title("Optimized 3D Mandelbrot Set Visualization")

# Sidebar controls
st.sidebar.header("3D Visualization Settings")
x_min, x_max = st.sidebar.slider("X-axis Range", -2.0, 2.0, (-1.5, 1.5))
y_min, y_max = st.sidebar.slider("Y-axis Range", -2.0, 2.0, (-1.5, 1.5))
z_min, z_max = st.sidebar.slider("Z-axis Range", -2.0, 2.0, (-1.0, 1.0))
res = st.sidebar.slider("Resolution", 10, 100, 50)
max_iter = st.sidebar.slider("Max Iterations", 10, 200, 50)

st.sidebar.text("Generating Mandelbrot set...")
# Generate the Mandelbrot set
X, Y, Z, iterations = mandelbrot_3d(x_min, x_max, y_min, y_max, z_min, z_max, res, max_iter)

# Flatten grid data for visualization
X_flat = X.flatten()
Y_flat = Y.flatten()
Z_flat = Z.flatten()
iterations_flat = iterations.flatten()

# Create a 3D volume rendering
fig = go.Figure(
    data=go.Volume(
        x=X_flat,
        y=Y_flat,
        z=Z_flat,
        value=iterations_flat,
        isomin=0.0,
        isomax=1.0,
        opacity=0.1,  # Adjust for better visualization
        surface_count=20,
        colorscale="Viridis",
    )
)

# Update layout
fig.update_layout(
    scene=dict(
        xaxis_title="Re",
        yaxis_title="Im",
        zaxis_title="3rd Dimension",
    ),
    title="Interactive 3D Mandelbrot Set",
    margin=dict(l=0, r=0, b=0, t=40),
)

# Display the figure
st.plotly_chart(fig, use_container_width=True)
