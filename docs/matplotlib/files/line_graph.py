from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph(title, equation, label):
    # Define the range of x values
    x = np.arange(-1, 6)
    # Calculate the corresponding y values
    y = eval(equation)
    # Resize the Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
    # Adjust subplot parameters to make room for the legend
    fig.subplots_adjust(right=0.7)
    # Plot the line graph
    ax.plot(x, y, "bo-", label=label)
    # Add a x, y axis black solid lines through the origin
    ax.axhline(0, color="k", linestyle="-")
    ax.axvline(0, color="k", linestyle="-")
    # add a grid, grey as dots
    ax.grid(True, color='grey', linestyle=':')
    # Add a title (specify font parameters with fontdict)
    ax.set_title(title, fontdict={"fontname": "Lucida Sans", "fontsize": 24})
    # X and Y labels
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    # specify X, Y axis Tickmarks (will resize graph)
    ax.set_xticks(list(x))
    # Set y-axis tick marks to be every 1 instead of 2
    y_min = int(min(y))
    y_max = int(max(y))
    ax.set_yticks(range(y_min, y_max+1))
    # Set the aspect ratio of the axes to be equal
    ax.set_aspect('equal')
    # Label each point on the graph
    for i in range(len(x)):
        ax.text(x[i]+0.1, y[i]-0.25, f"({x[i]}, {y[i]})", fontsize=12)
    # Place legend outside plot at top right, making extra room for it
    ax.legend(title="Lines", loc='center left', bbox_to_anchor=(1.05, 0.5))
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent
    # Replace spaces in title with underscores to create filename for saving figure
    filename = title.replace(" ", "_") 
    filepath = currfile_dir / (f"{filename}.png")
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    plt.savefig(filepath, dpi=600)
    # Show plot
    plt.show()


def main():
    plot_line_graph("Line Graph", "2 * x + 1", "y = 2x + 1")


if __name__ == '__main__':
    main()
