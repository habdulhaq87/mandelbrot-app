import streamlit as st
from explains import mandelbrot_explanation
from visualization import mandelbrot_set, plot_mandelbrot

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

# Tabs for navigation
tab1, tab2 = st.tabs(["Visualization", "Explain"])

# Visualization Tab
with tab1:
    st.header("Visualization")
    st.sidebar.header("🎨 Visualization Settings")
    
    # Sidebar controls for visualization
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
    with st.spinner("Generating Mandelbrot set..."):
        mask = mandelbrot_set(width, height, max_iter, x_min, x_max, y_min, y_max)
        fig = plot_mandelbrot(mask, cmap=cmap)
        st.pyplot(fig)

# Explain Tab
with tab2:
    st.header("Explain")
    st.write(mandelbrot_explanation())

# Footer
st.markdown("---")
st.markdown(
    """
    Created with ❤️ using [Streamlit](https://streamlit.io) and [Matplotlib](https://matplotlib.org).  
    Explore more about the Mandelbrot set [here](https://en.wikipedia.org/wiki/Mandelbrot_set).
    """
)
