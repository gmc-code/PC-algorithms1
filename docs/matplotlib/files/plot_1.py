from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph(title, equation, label):
    """Plots a line graph of a given equation and labels it.

    Args:
        title (str): The title of the graph.
        equation (str): A string representing the equation to be plotted.
        label (str): A string representing the label for the equation.

    Returns:
        None
    """
    # Define the range of x values
    x = np.arange(-1, 6)
    # Calculate the corresponding y values as a np array using the x values.
    y = eval(equation)
    # set size and resolution
    plt.figure(figsize=(7, 8), dpi=100)
    # Plot the line graph
    plt.plot(x, y, "bo-", label=label)
    # Add a x, y axis black solid lines through the origin
    plt.axhline(0, color="k", linestyle="-")
    plt.axvline(0, color="k", linestyle="-")
    # add a grid, grey as dots
    plt.grid(True, color='grey', linestyle=':')
    # Add a title (specify font parameters with fontdict)
    plt.title(title, fontdict={"fontname": "Lucida Sans", "fontsize": 24})
    # X and Y labels
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    # specify X, Y axis Tickmarks (will resize graph)
    plt.xticks(list(x))
    # Set y-axis tick marks to be every 1 instead of 2
    y_min = int(min(y))
    y_max = int(max(y))
    plt.yticks(range(y_min, y_max+1))
    # Set the aspect ratio of the axes to be equal
    plt.gca().set_aspect('equal')
    # Label each point on the graph
    for i in range(len(x)):
        plt.text(x[i]+0.1, y[i]-0.25, f"({x[i]}, {y[i]})", fontsize=10)
    # Place legend outside plot at top right, making extra room for it
    plt.legend(title="Line", loc='center left', bbox_to_anchor=(1.00, 0.5))
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent
    # Replace spaces in title with underscores to create filename for saving figure
    filename = title.replace(" ", "_")
    # build the image file path
    filepath = currfile_dir / (f"{filename}.png")
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    plt.savefig(filepath, dpi=600)
    # Show plot
    plt.show()


def main():
    plot_line_graph("Straight line", "2 * x + 1", "y = 2x + 1")


if __name__ == '__main__':
    main()
