def mandelbrot_explanation():
    """
    Returns a string explaining the Mandelbrot set.
    """
    return """
    ## About the Mandelbrot Set
    
    The Mandelbrot set is a set of complex numbers for which a simple iterative formula does not diverge to infinity. 
    It is defined as follows:
    
    $$ Z_{n+1} = Z_n^2 + C $$
    
    Where:
    - \( Z \) is a complex number.
    - \( C \) is a constant complex number.

    Starting with \( Z_0 = 0 \), we iterate the formula and check whether the magnitude of \( Z_n \) stays bounded (less than 2). 
    If \( |Z_n| \geq 2 \), the sequence diverges, and the corresponding point does not belong to the Mandelbrot set.
    
    ### Visualizing the Mandelbrot Set
    The Mandelbrot set forms a fractal—a self-similar pattern at all scales. The boundary of the set contains infinite complexity and beauty, making it one of the most famous examples of a fractal in mathematics.
    
    ### Key Facts
    - **Inventor**: Benoit B. Mandelbrot, a mathematician who studied fractals and chaos theory.
    - **Discovered**: 1980s, with the advent of computer graphics.
    - **Applications**: Art, computer graphics, modeling natural phenomena, and chaos theory.

    To learn more, visit [Wikipedia](https://en.wikipedia.org/wiki/Mandelbrot_set).
    """
