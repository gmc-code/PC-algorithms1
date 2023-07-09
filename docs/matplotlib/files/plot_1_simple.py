from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph(title, equation, min_x, max_x):
    """
    Plots a line graph of the equation y = eval(equation) over the range of x values from min_x to max_x.
    
    Parameters:
    title (str): The title of the graph.
    equation (str): The equation to plot.
    min_x (int): The minimum value of x to plot.
    max_x (int): The maximum value of x to plot.
    
    Returns:
    None
    """
    # Define the range of x values
    x = np.arange(min_x, max_x + 1)
    # Calculate the corresponding y values as a np array using the x values.
    y = eval(equation)
    # set size and resolution
    plt.figure(figsize=(7, 8), dpi=100)
    # Plot the line graph
    plt.plot(x, y)
    # Add a x, y axis black solid lines through the origin
    plt.axhline(0, color="k", linestyle="-")
    plt.axvline(0, color="k", linestyle="-")
    # add a grid, grey as dots
    plt.grid(True, color='grey', linestyle=':')
    # Add a title (specify font parameters with fontdict)
    plt.title(title, fontdict={"fontname": "Lucida Sans", "fontsize": 24})
    # Show plot
    plt.show()


def main():
    plot_line_graph("Linear plot", "x/2 + 1", -2, 4)


if __name__ == '__main__':
    main()
