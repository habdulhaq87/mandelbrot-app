import streamlit as st
import numpy as np
import plotly.graph_objects as go

def mandelbrot_3d(x_min, x_max, y_min, y_max, z_min, z_max, res, max_iter):
    """Generate the Mandelbrot set in 3D."""
    x = np.linspace(x_min, x_max, res)
    y = np.linspace(y_min, y_max, res)
    z = np.linspace(z_min, z_max, res)
    X, Y, Z = np.meshgrid(x, y, z)
    
    C = X + 1j * (Y + 1j * Z)
    Z = np.zeros(C.shape, dtype=complex)
    iterations = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask]**2 + C[mask]
        iterations[mask] += 1

    return iterations

# Streamlit interface
st.title("3D Mandelbrot Set Visualization")

# Sidebar controls
st.sidebar.header("3D Visualization Settings")
x_min, x_max = st.sidebar.slider("X-axis Range", -2.0, 2.0, (-1.5, 1.5))
y_min, y_max = st.sidebar.slider("Y-axis Range", -2.0, 2.0, (-1.5, 1.5))
z_min, z_max = st.sidebar.slider("Z-axis Range", -2.0, 2.0, (-1.0, 1.0))
res = st.sidebar.slider("Resolution", 20, 200, 50)
max_iter = st.sidebar.slider("Max Iterations", 10, 200, 50)

st.sidebar.text("Generating...")
# Generate the 3D Mandelbrot set
iterations = mandelbrot_3d(x_min, x_max, y_min, y_max, z_min, z_max, res, max_iter)

# Create a Plotly figure
fig = go.Figure(
    data=[
        go.Volume(
            x=np.repeat(np.linspace(x_min, x_max, res), res * res),
            y=np.tile(np.repeat(np.linspace(y_min, y_max, res), res), res),
            z=np.tile(np.linspace(z_min, z_max, res), res * res),
            value=iterations.flatten(),
            isomin=0,
            isomax=max_iter,
            opacity=0.1,  # Adjust for better visualization
            surface_count=20,
            colorscale="Viridis",
        )
    ]
)

# Customize the layout
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
