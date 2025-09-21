"""
least_squares.py

This script demonstrates the concept of the least squares component
by performing a simple linear regression calculation from scratch.

It calculates the line of best fit by minimizing the sum of squared errors
between observed data and the model's predictions.
"""

import numpy as np

def calculate_least_squares(x_data, y_data):
    """
    Calculates the slope (m) and y-intercept (b) of the least squares
    regression line.

    Args:
        x_data (np.array): The independent variable data.
        y_data (np.array): The dependent variable (observed) data.

    Returns:
        tuple: A tuple containing the slope (m) and y-intercept (b).
    """
    # Number of data points
    n = len(x_data)

    # Calculate the means of x and y
    mean_x = np.mean(x_data)
    mean_y = np.mean(y_data)

    # Calculate the numerator and denominator for the slope (m)
    # Numerator: sum of (x_i - mean_x) * (y_i - mean_y)
    # Denominator: sum of (x_i - mean_x)^2
    numerator = np.sum((x_data - mean_x) * (y_data - mean_y))
    denominator = np.sum((x_data - mean_x)**2)

    # Handle the case where the denominator is zero (no variance in x)
    if denominator == 0:
        print("Warning: Denominator is zero. Cannot calculate slope.")
        return 0, mean_y

    # Calculate the slope and y-intercept
    m = numerator / denominator
    b = mean_y - m * mean_x

    return m, b

def calculate_sum_of_squared_errors(x_data, y_data, m, b):
    """
    Calculates the sum of squared errors (SSE) for a given regression line.
    This is the least squares component.

    Args:
        x_data (np.array): The independent variable data.
        y_data (np.array): The dependent variable (observed) data.
        m (float): The slope of the regression line.
        b (float): The y-intercept of the regression line.

    Returns:
        float: The sum of squared errors (SSE).
    """
    # Calculate predicted y values
    y_predicted = m * x_data + b

    # Calculate the residuals (errors)
    residuals = y_data - y_predicted

    # Calculate the sum of the squared residuals
    sse = np.sum(residuals**2)

    return sse

if __name__ == "__main__":
    # Sample data for house prices (same as the previous example)
    # x_data: House size in square feet (in thousands for easier calculation)
    # y_data: House price (in thousands of dollars)
    x_data = np.array([1000, 1200, 1500, 1700, 2000])
    y_data = np.array([250, 280, 350, 380, 450])

    print("--- Least Squares Regression Example ---")
    print("Observed Data:")
    print(f"Sizes (sq ft): {x_data}")
    print(f"Prices ($):    {y_data}")
    print("-" * 35)

    # Calculate the slope and y-intercept
    slope, intercept = calculate_least_squares(x_data, y_data)
    
    # Calculate the sum of squared errors for our model
    sse = calculate_sum_of_squared_errors(x_data, y_data, slope, intercept)

    # Print the results
    print(f"Calculated Slope (m): {slope:.2f} (price increase per sq ft)")
    print(f"Calculated Y-Intercept (b): {intercept:.2f} (base price in $)")
    print(f"The equation for the line of best fit is: y = {slope:.2f}x + {intercept:.2f}")
    print("-" * 35)
    print(f"Sum of Squared Errors (SSE): {sse:.2f}")
    print("This value represents the 'least squares component'—the goodness of fit.")
    print("A smaller SSE indicates a better fit of the line to the data.")
