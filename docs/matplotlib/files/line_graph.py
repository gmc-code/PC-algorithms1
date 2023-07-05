from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph():
    # Define the range of x values
    x = np.arange(-1, 6)
    # Calculate the corresponding y values
    y = 2 * x + 1
    # Resize the Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
    plt.figure(figsize=(8, 5), dpi=300)
    # Plot the line graph
    plt.plot(x, y, "b^--", label="y = 2x + 1")
    # Add a title (specify font parameters with fontdict)
    plt.title("Line Graph", fontdict={"fontname": "Lucida Sans", "fontsize": 24})
    # X and Y labels
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    # specify X, Y axis Tickmarks (will resize graph)
    plt.xticks([-1, 0, 1, 2, 3, 4, 5])
    # Add a legend
    plt.legend()
    # Save figure (dpi 300 is good when saving so graph has high resolution)  
    currfile_dir = Path(__file__).parent
    filepath = currfile_dir / ("line_graph.png")
    plt.savefig(filepath, dpi=600)
    # Show plot
    plt.show()


def main():
    plot_line_graph()


if __name__ == '__main__':
    main()
