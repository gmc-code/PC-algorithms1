import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib.patches import Patch


def plot_bar_chart(data, labels, title, xlabel, ylabel):
    # Plot the bar chart with the given data, labels, and formatting options
    plt.bar(labels, data)
    # X and Y labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # Add a title to the plot
    plt.title(title)
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
    # Title for plot
    title = "Earth's Crust barchart"
    # X axis label
    xlabel = "Element"
    # Y axis label
    ylabel = "Percentage of crust (%)"
    # Call the function to plot the data with given data, labels, title axis labels
    plot_bar_chart(data, labels, title, xlabel, ylabel)


if __name__ == '__main__':
    earth_elements()
