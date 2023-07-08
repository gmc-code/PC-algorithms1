import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def box_plot_ax(data, xlabel, ax):
    """
    Create a box plot of the given data with the specified title.

    Parameters:
    data (array-like): The data to plot.
    title (str): The title of the plot.
    ax (matplotlib.axes.Axes): The Axes object to draw the box plot on.

    Returns:
    None
    """
    # Plot the data on the specified Axes object
    ax.boxplot(data)
    # Hide the top, right, and left spines of the plot
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    # Set the y-axis limits to include all of the data points
    ax.set_ylim(0, max(data)+ 2)
    # Add a title to the plot with the specified text and formatting
    ax.set_xlabel(f"{xlabel}", fontdict={"fontname": "Arial", "fontsize": 12})


def norm_sample_data(min, max, mu, sigma, n):
    """
    Generate n sample points from a normal distribution with mean mu and standard deviation sigma, clipped to the range [min, max] and converted to integers.

    Parameters:
    min (int): The minimum value of the range to clip the sample data to.
    max (int): The maximum value of the range to clip the sample data to.
    mu (float): The mean of the normal distribution to sample from.
    sigma (float): The standard deviation of the normal distribution to sample from.
    n (int): The number of sample points to generate.

    Returns:
    numpy.ndarray: An array of n integers sampled from a normal distribution with mean mu and standard deviation sigma, clipped to the range [min, max].
    """
    # Generate an array of n random values sampled from a normal distribution with mean mu and standard deviation sigma
    s = np.random.normal(mu, sigma, n)
    # clip values outside the range [min, max]
    s = np.clip(s, min, max)  
    # convert to integers
    s = s.astype(int)  
    return s


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


def box_pets(ax):
    data = [1, 2, 3, 2, 0, 1, 0, 2, 5, 3, 2, 1, 2, 0, 2, 0, 1, 3, 2, 1]
    xlabel = "pets per household"
    box_plot_ax(data, xlabel, ax)


def box_vehicles(ax):
    data = [2, 0, 3, 2, 1, 0, 2, 3, 4, 2, 2, 1, 0, 1, 3, 2, 1, 0, 0, 0, 2, 2, 3, 3]
    xlabel = "vehicles per household"
    box_plot_ax(data, xlabel, ax)


def box_random(ax):
    data = random_data(0, 8, 20)
    xlabel = "Random distribution"
    box_plot_ax(data, xlabel, ax)


def box_normal(ax):   
    # (min, max, mu, sigma, n)
    data = norm_sample_data(0, 8, 4, 1, 20)
    xlabel = "Normal distribution"
    box_plot_ax(data, xlabel, ax)


def multi_box_plot(title):
    fig, axs = plt.subplots(2, 2, sharey=True)

    # create box plots
    box_pets(axs[0, 0])
    box_vehicles(axs[0, 1])
    box_random(axs[1, 0])
    box_normal(axs[1, 1])
    # adjust spacing between subplots
    plt.subplots_adjust(hspace=0.4)
        # add title to figure
    title_str = title.title()
    fig.suptitle(f"{title_str}", fontsize=12)
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



# Call the main function if this file is run as a script
if __name__ == "__main__":
    # create figure and axes
    multi_box_plot("Box plots compared")