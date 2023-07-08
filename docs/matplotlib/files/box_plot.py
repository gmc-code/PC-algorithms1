import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def box_plot(data, title):
    """
    Create a box plot of the given data with the specified title.

    Parameters:
    data (array-like): The data to plot.
    title (str): The title of the plot.

    Returns:
    None
    """
    # Create a new figure with the specified size
    # plt.figure(figsize=(6, 6))
    # Plot the data
    plt.boxplot(data)
    # Get the current Axes object
    ax = plt.gca()
    # Hide the top, right, and left spines of the plot
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    # Set the y-axis limits to include all of the data points
    ax.set_ylim(0, max(data)+ 2)
    # Add a title to the plot with the specified text and formatting
    title_str = title.title()
    ax.set_title(f"{title_str}", fontdict={"fontname": "Arial", "fontsize": 12})
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


def random_data(min, max, n):
    """
    Generate an array of n random integers between min and max, inclusive.
    
    Parameters:
    min (int): The minimum value of the range to generate random integers from.
    max (int): The maximum value of the range to generate random integers from.
    n (int): The number of random integers to generate.
    
    Returns:
    numpy.ndarray: An array of n random integers between min and max, inclusive.
    """
    # create a random number generator without a fixed seed
    rng = np.random.default_rng() 
    # generate an array of n random integers between min and max, inclusive
    data = rng.integers(min, max + 1, size=n)  
    # return the generated data
    return data


def box_random():
    data = random_data(1, 8, 20)
    title = "Random box plot"
    box_plot(data, title)



# Call the main function if this file is run as a script
if __name__ == "__main__":
    box_random()
