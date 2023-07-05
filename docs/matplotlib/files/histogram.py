import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def plot_histogram(x, title):
    currfile_dir = Path(__file__).parent
    plt.style.use('_mpl-gallery')

    # plot:
    fig, ax = plt.subplots(figsize=(10, 6))
    # The hist function returns three values: the counts of each bin in the histogram, the edges of the bins, and the patches used to create the histogram.
    counts, _, _ = ax.hist(x, linewidth=0.5, edgecolor="white")
    # set the x and y ticks
    plt.xticks(range(min(x), max(x)+1))
    plt.yticks(range(0, int(max(counts))+1))
    # set the x label
    plt.xlabel(title)
    plt.ylabel('Counts')
    plt.title(title)
    filename = title.replace(" ", "_")
    # adjust the margins of the plot
    plt.subplots_adjust(bottom=0.07, left=0.07, top=0.95)
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    filepath = currfile_dir / (f"{filename}.png")
    plt.savefig(filepath, dpi=600)

    # Show plot
    plt.show()


def main():
    # make data
    x = [10, 8, 12, 11, 12, 18, 13, 11, 12, 11, 12, 12, 13, 14]
    # call the function to plot the data
    title = 'Vending Machine Sales'
    plot_histogram(x, title)


if __name__ == '__main__':
    main()
