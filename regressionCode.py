
import numpy as np
import plotly.graph_objects as go

def convert_text(text):
    text = str(text)
    normal_chars = "0123456789"
    superscript_chars = "⁰¹²³⁴⁵⁶⁷⁸⁹"

    mapping = str.maketrans(normal_chars, superscript_chars)

    converted_text = text.translate(mapping)
    return converted_text

def create_dist(x_mean: float, x_std: float, y_mean: float, y_std: float, num_of_points: int, order: int):
    # Generate your x and y data points
    x = np.random.normal(x_mean, x_std, num_of_points)
    y = .5*(x**3) + x**2 + 100*np.random.normal(y_mean, y_std, num_of_points)

    # Add a column of ones to account for the y intercept constant
    A = np.column_stack((np.ones(x.shape[0]), x))
    for i in range(2, order + 1):
        A = np.column_stack((A, x**i))


    """START OF CALCULATIONS"""

    # Generating x hat for Ax = b
    def generate_x_hat(A: np.array):
        x_hat = np.linalg.pinv(A.T.dot(A)).dot(A.T).dot(y)
        return x_hat

    x_hat = generate_x_hat(A)

    # Calculate error 
    # y - p where p = A(x_hat)
    p = A.dot(x_hat)
    error = y - p

    # Calculate R^2 -- SSR/SST 
    # SSR = sum squared regression (SSR) = sum of errors squared
    # SST = total sum of squares (SST) = (sum of y values of points) - (mean of all y values)
    ## mean of y points
    
    ssr = np.sum(error ** 2)
    sst = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1-(ssr/sst)
    #print(f"ssr: {ssr}")
    #print(f"sst: {sst}")
    #print(f"R^2 ssr/sst: {r_squared}")
    

    """END OF CALCULATIONS"""


    """CREATING PLOTS"""
    # Plotting with Plotly
    fig = go.Figure()

    # Generate x values for the curve
    x_curve = np.linspace(np.min(x), np.max(x), 100)
    y_curve = np.zeros_like(x_curve)  # Initialize y_curve with zeros

    # Add terms for each power of x_curve
    for i in range(order + 1):
        y_curve += x_hat[i] * (x_curve ** i)  
    
    # Create the string equation 
    equation = "y = "
    for i in range(order, -1, -1):
        if i == 0:
            equation += f"{x_hat[i]:.2f}"
        elif i == 1:
            equation += f"{x_hat[i]:.2f}x + "
        else:
            equation += f"{x_hat[i]:.2f}x{convert_text(i)} + "
        if i%3 == 0:
            equation += "<br>"

    # Scatter plot
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Data'))
    # Line of best fit
    fig.add_trace(go.Scatter(x=x_curve, y = y_curve, mode='lines', name=f"{equation}R² = {round(r_squared, 3)}"))

    # Update layout for better visualization
    fig.update_layout(
        title="Interactive Scatter Plot with Line of Best Fit",
        xaxis_title="X-axis",
        yaxis_title="Y-axis"
    )

    return fig