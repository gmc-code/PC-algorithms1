import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib.patches import Patch


def plot_bar_chart(data, labels, legend_labels, title, xlabel, ylabel):
    # Define the colors to use for the bar chart
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    # Plot the bar chart with the given data, labels, and formatting options
    plt.bar(labels, data, color=colors)
    # Add some space around the plot
    plt.subplots_adjust(left=0.1, right=0.70, top=0.85, bottom=0.1)
    # X and Y labels
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    # Add a title to the plot
    plt.title(title, y=1.08, size=16)
    # Create a list of Patch objects with the same colors as the bars in the bar chart
    legend_elements = [Patch(facecolor=color, label=label) for color, label in zip(colors, legend_labels)]
    # Add a legend to the plot using the given legend_labels and colors from the bar chart
    plt.legend(handles=legend_elements, title="Legend", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))
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


def earth_elements():
    # Data to plot
    data = [47, 28, 8, 5, 12]
    # Labels for each wedge of the pie chart
    labels = ['O', 'Si', 'Al', 'Fe', 'Others']
    # Full labels for legend
    legend_labels = ['Oxygen', 'Silicon', 'Aluminium', 'Iron', 'Others']
    # Title for plot and filename for saving figure
    title = "Elements in the Earth's Crust barchart"
    # X axis label
    xlabel = "Element"
    # Y axis label
    ylabel = "Percentage of crust (%)"
    # Call the function to plot the data with given data, labels, legend_labels, title and axis labels.
    plot_bar_chart(data, labels, legend_labels, title, xlabel, ylabel)


if __name__ == '__main__':
    earth_elements()
