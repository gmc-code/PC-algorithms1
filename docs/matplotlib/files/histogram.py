import matplotlib.pyplot as plt
import numpy as np
from statistics import median
from pathlib import Path


def plot_histogram(x, title, median):
    # Create a new figure with the specified size
    plt.figure(figsize=(10, 6))
    # Create a histogram plot of the data in x with the specified bin edges, line width, edge color, and fill color
    counts, _, _ = plt.hist(x, bins=np.arange(min(x), max(x)+2), linewidth=0.5, edgecolor="blue", color="lightblue")
    # set the x and y tick locations and labels for the plot to display integer values along both axes, with an offset of 0.5 units for the x tick locations so hte tick is in the middle of each column
    ticks_offset = 0.5
    plt.xticks(np.arange(min(x), max(x)+1) + ticks_offset, np.arange(min(x), max(x)+1))
    plt.yticks(range(0, int(max(counts))+1))
    # Set the x and y axis title labels
    plt.xlabel(title)
    plt.ylabel('Counts')
    # Set the plot title
    plt.title(title)
    # Add a vertical line at the median value with the specified color and line style
    plt.axvline(median + ticks_offset, color="b", linestyle="--")
    # Add a text annotation at the specified x and y coordinates with the specified text, rotation, color, and font size
    plt.text(median + ticks_offset + 0.1, 2, f"Median = {median:.1f}", rotation=90, color="b", fontsize=16)
    # Adjust the margins of the plot to leave space for the axis labels and title
    plt.subplots_adjust(bottom=0.07, left=0.07, top=0.95)
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent
    # Replace spaces in title with underscores to create filename for saving figure
    filename = title.replace(" ", "_")
    # build the image file path
    filepath = currfile_dir / (f"{filename}.png")
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    plt.savefig(filepath, dpi=600)
    # Show the plot on the screen
    plt.show()


def plot_vending_sales():
    # Create a list of data values
    x = [10, 8, 12, 11, 12, 18, 13, 11, 12, 11, 12, 12, 13, 14]
    # Compute the median of the data values
    mymedian = median(x)
    # Set the title of the plot
    title = 'Vending Machine Sales'
    # Call the function to plot the data with the specified title and median value
    plot_histogram(x, title, mymedian)


if __name__ == '__main__':
    plot_vending_sales()
