import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



def dot_plot(data, title):
    """
    Create a dot plot of the given data with the specified title.

    Parameters:
    data (array-like): The data to plot.
    title (str): The title of the plot.

    Returns:
    None
    """
    # Get the unique values in the data and their counts
    values, counts = np.unique(data, return_counts=True)
    # Set formatting parameters based on the range of the data
    data_range = max(values)-min(values)
    width = 1 + data_range/2 if data_range<30 else 15
    height = 1.2 + max(counts)/3 if data_range<30 else 2 + max(counts)/4
    marker_size = 10 if data_range<50 else np.ceil(30/(data_range//10))
    # Create a new figure with the specified size
    plt.figure(figsize=(width, height))
    # Plot the data as a series of dots, with one dot for each count of each value
    for value, count in zip(values, counts):
        plt.plot(
            [value] * count,
            list(range(count)),
            marker="o",
            color="tab:blue",
            ms=marker_size,
            linestyle="",
        )
    # Get the current Axes object
    ax = plt.gca()
    # Hide the top, right, and left spines of the plot
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    # Hide the y-axis
    ax.yaxis.set_visible(False)
    # Set the y-axis limits to include all of the data points
    ax.set_ylim(-1, max(counts))
    # Set the x tick locations to be at integer values from the minimum to the maximum value in the data
    ax.set_xticks(range(min(values), max(values) + 1))
    # Adjust the bottom margin of the plot to leave space for the x tick labels
    cms = 0.5 * 1/2.54 # inches per cm
    plt.subplots_adjust(bottom=cms)
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


def dot_pets():
    data = [1, 2, 3, 2, 0, 1, 0, 2, 5, 3, 2, 1, 2, 0, 2, 0, 1, 3, 2, 1]
    title = "pets per household"
    dot_plot(data, title)


def dot_vehicles():
    data = [2, 0, 3, 2, 1, 0, 2, 3, 4, 2, 2, 1, 0, 1, 3, 2, 1, 0, 0, 0, 2, 2, 3, 3]
    title = "vehicles per household"
    dot_plot(data, title)


def dot_random():
    data = random_data(1, 6, 20)
    title = "Random distribution"
    dot_plot(data, title)


def dot_normal():   
    data = norm_sample_data(5, 45, 25, 3, 50)
    title = "Normal distribution"
    dot_plot(data, title)


# Call the main function if this file is run as a script
if __name__ == "__main__":
    dot_pets()
    dot_vehicles()
    dot_random()
    dot_normal()