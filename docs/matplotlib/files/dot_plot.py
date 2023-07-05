import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

currfile_dir = Path(__file__).parent


def dot_plot(data, title):
    """
    Create a dot plot of the given data with the specified title.

    Parameters:
    data (array-like): The data to plot.
    title (str): The title of the plot.

    Returns:
    None
    """
    # get counts of each value
    values, counts = np.unique(data, return_counts=True)
    # Set formatting parameters based on data
    data_range = max(values)-min(values)
    width = 1 + data_range/2 if data_range<30 else 15
    height = 1.2 + max(counts)/3 if data_range<30 else 2 + max(counts)/4
    marker_size = 10 if data_range<50 else np.ceil(30/(data_range//10))
    # Create dot plot with appropriate format
    fig, ax = plt.subplots(figsize=(width, height))

    # The x-coordinates are [value] * count, which is a list of count copies of value. The y-coordinates are list(range(count)), which is a list of integers from 0 to count-1.
    for value, count in zip(values, counts):
        ax.plot(
            [value] * count,
            list(range(count)),
            marker="o",
            color="tab:blue",
            ms=marker_size,
            linestyle="",
        )   
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)  
    ax.yaxis.set_visible(False)
    ax.set_ylim(-1, max(counts))
    ax.set_xticks(range(min(values), max(values) + 1))
    # Adjust bottom margin to leave 1 cm of space for x labels
    cms = 0.5 * 1/2.54 # inches per cm
    plt.subplots_adjust(bottom=cms)
    # Add a title
    title_str = title.title()
    plt.title(f"{title_str}", fontdict={"fontname": "Arial", "fontsize": 12})
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    filepath = currfile_dir / (f"{title}.png")
    plt.savefig(filepath, dpi=600)
    # Show plot
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
    s = np.random.normal(mu, sigma, n)
    s = np.clip(s, min, max)  # clip values outside the range [min, max]
    s = s.astype(int)  # convert to integers
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


# Call the main function if this file is run as a script
if __name__ == "__main__":
    data = [1, 2, 3, 2, 0, 1, 0, 2, 5, 3, 2, 1, 2, 0, 2, 0, 1, 3, 2, 1]
    title = "pets_per_household"
    dot_plot(data, title)

    data = [2, 0, 3, 2, 1, 0, 2, 3, 4, 2, 2, 1, 0, 1, 3, 2, 1, 0, 0, 0, 2, 2, 3, 3]
    title = "vehicles_per_household"
    dot_plot(data, title)

    data = random_data(1, 6, 20)
    title = "Random_distribution"
    dot_plot(data, title)
    
    data = norm_sample_data(5, 45, 25, 3, 50)
    title = "Normal_distribution"
    dot_plot(data, title)
