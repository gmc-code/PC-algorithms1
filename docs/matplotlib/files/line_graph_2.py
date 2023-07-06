from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph(title, equations, labels):
    # Define the range of x values
    x = np.arange(-1, 6)
    
    # Resize the Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
    fig = plt.figure(figsize=(8, 8), dpi=100)
    # Adjust subplot parameters to make room for the legend
    fig.subplots_adjust(right=0.7)
    
    # Plot the line graphs
    for equation, label in zip(equations, labels):
        # Calculate the corresponding y values
        y = eval(equation)
        plt.plot(x, y, "o-", label=label)
        # Label each point on the graph
        for i in range(len(x)):
            plt.text(x[i]+0.1, y[i]-0.25, f"({x[i]}, {y[i]})", fontsize=12)
    
    # Add a x, y axis lines through the origin
    plt.axhline(0, color="gray", linestyle="--")
    plt.axvline(0, color="gray", linestyle="--")
    
    # Add a title (specify font parameters with fontdict)
    plt.title(title, fontdict={"fontname": "Lucida Sans", "fontsize": 24})
    # X and Y labels
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    # specify X, Y axis Tickmarks (will resize graph)
    plt.xticks(list(x))
    
    # Place legend outside plot at top right, making extra room for it
    plt.legend(title="Lines", loc='center left', bbox_to_anchor=(1.05, 0.5))
    
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
    plot_line_graph("Line Graph 2", ["2 * x + 1", "(x-1)**2"], ["y = 2x + 1", r"y = (x-1)$^2$"])


if __name__ == '__main__':
    main()
