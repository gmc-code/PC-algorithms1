from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph(title, equations, labels):
    """Plots line graphs of given equations and labels them.

    Args:
        title (str): The title of the graph.
        equations (list of str): A list of strings representing the equations to be plotted.
        labels (list of str): A list of strings representing the labels for each equation.

    Returns:
        None
    """
    # Define the range of x values
    x = np.linspace(-1, 5, 100)
    # Resize the Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
    fig = plt.figure(figsize=(8, 8), dpi=100)
    # Adjust subplot parameters to make room for the legend
    fig.subplots_adjust(right=0.75)
    # set initial y_min and y_max that will be used for y ticks
    y_min = 0
    y_max = 0
    for i, (equation, label) in enumerate(zip(equations, labels)):
        # Calculate the corresponding y values
        y = eval(equation)
        # since y is an array, need to do min(y) first before combining with y_min
        y_min = int(min(min(y), y_min))
        y_max = int(max(max(y), y_max))
        # use default colours C0, C1...C9
        color = f'C{i}'
        # Plot the line graph
        plt.plot(x, y, label=label, color=color)
        # Create a lambda function from the equation string to allow use of variable xi
        f = eval("lambda x: " + equation)
        # Label each point on the graph for x = -1 to 5 as integers
        for j in range(-1, 6):
            xi = j
            yi = f(xi)
            plt.plot(xi, yi, "o", color=color)
            # test to see if value is an integer so y coordinates can avoid using decimals
            if int(yi) == yi:
                plt.text(xi+0.1, yi-0.25, f"({xi}, {int(yi)})", fontsize=10)
            else:
                plt.text(xi+0.1, yi-0.25, f"({xi}, {yi:.2f})", fontsize=10)
    # Calculate the corresponding y values for both lines
    y1 = eval(equations[0])
    y2 = eval(equations[1])            
    # Fill the area between the two lines
    plt.fill_between(x, y1, y2, where=(y1 > y2), interpolate=True, color='green', alpha=0.2, label="Line above")
    plt.fill_between(x, y1, y2, where=(y1 <= y2), interpolate=True, color='red', alpha=0.2, label="Curve above")
    # Add a x, y axis lines through the origin
    plt.axhline(0, color="gray", linestyle="-")
    plt.axvline(0, color="gray", linestyle="-")
    # Add a title (specify font parameters with fontdict)
    plt.title(title, fontdict={"fontname": "Lucida Sans", "fontsize": 24})
    # X and Y labels
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    # specify X axis Tickmarks (will resize graph)
    plt.xticks(np.arange(-1, 6))
    # Set y-axis tick marks to be every 1
    plt.yticks(range(y_min, y_max+1))
    # Place legend outside plot at top right, making extra room for it
    plt.legend(title="Lines", loc='center left', bbox_to_anchor=(1.05, 0.5))
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
    plot_line_graph("Straight line and parabola", ["2 * x + 1", "(x-1)**2"], ["y = 2x + 1", r"y = (x-1)$^2$"])


if __name__ == '__main__':
    main()
