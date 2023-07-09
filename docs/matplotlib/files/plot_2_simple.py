import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph(title, equations, min_x, max_x):
    """Plots line graphs of given equations.

    Args:
        title (str): The title of the graph.
        equations (list of str): A list of strings representing the equations to be plotted.
        min_x (int): The minimum value of x to plot.
        max_x (int): The maximum value of x to plot.
        
    Returns:
        None
    """
    # Size the Graph
    fig = plt.figure(figsize=(5,5), dpi=100)
    # Define the range of x values
    x = np.linspace(min_x, max_x, 100)
    # plot each equation
    for equation in equations:
        # Calculate the corresponding y values
        y = eval(equation)
        # Plot the line graph
        plt.plot(x, y)
    # Add x, y axis lines through the origin
    plt.axhline(0, color="gray", linestyle="-")
    plt.axvline(0, color="gray", linestyle="-")
    # Add a title (specify font parameters with fontdict)
    plt.title(title, fontdict={"fontname": "Lucida Sans", "fontsize": 16})
    # Show plot
    plt.show()


def main():
    plot_line_graph("Multiple lines", ["2 * x - 2", "-3 * x + 3", "(x-1)**2", "0.4*(x-1)**3"], -1, 3)


if __name__ == '__main__':
    main()
