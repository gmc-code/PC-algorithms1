import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def calculate_boxplot_stats(data):
    """
    Calculate box plot statistics for a given dataset.

    This function takes an array of data as input and returns the interquartile range (IQR),
    lower whisker length, and upper whisker length as a tuple.

    Args:
        data (array-like): An array of data to calculate box plot statistics for.

    Returns:
        tuple: A tuple containing the IQR, lower whisker length, and upper whisker length.
    """
    # Calculate the first and third quartiles
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    # Calculate the interquartile range (IQR)
    iqr = q3 - q1
    # Calculate the lower and upper bounds for outliers
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    # Calculate the adjacent values
    adjacent_lower = np.min(data[data >= lower_bound])
    adjacent_upper = np.max(data[data <= upper_bound])
    # Calculate the length of the whiskers
    lower_whisker_length = q1 - adjacent_lower
    upper_whisker_length = adjacent_upper - q3
    return iqr, lower_whisker_length, upper_whisker_length


def multi_box_plot():
    # Set the random seed for reproducibility
    np.random.seed(0)

    # Define the properties of each distribution
    distributions = [
        {
            'data': np.random.gamma(shape=1, scale=1.5, size=100),
            'hist_title': 'Positively Skewed Histogram',
            'box_title': 'Positively Skewed Box Plot'
        },
        {
            'data': 10 - np.random.gamma(shape=1, scale=1.5, size=100),
            'hist_title': 'Negatively Skewed Histogram',
            'box_title': 'Negatively Skewed Box Plot'
        },
        {
            'data': np.random.normal(loc=5.0, scale=1.5, size=100),
            'hist_title': 'Symmetric Histogram',
            'box_title': 'Symmetric Box Plot'
        }
    ]

    # Filter the data for each distribution
    for dist in distributions:
        dist['data'] = dist['data'][(dist['data'] >= 0) & (dist['data'] <= 10)]

    # Create figure with 3x2 subplots
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(6, 8))
    fig.subplots_adjust(hspace=0.35)
    # Add title to figure
    fig.suptitle('Comparison of Skewed and Symmetric Data', y=0.96)

    # Create histogram and box plot for each distribution
    for i, dist in enumerate(distributions):
        axs[i, 0].hist(dist['data'], bins=10, range=(0, 10))
        axs[i, 0].set_title(dist['hist_title'])
        axs[i, 1].set_title(dist['box_title'])
        axs[i, 1].boxplot(dist['data'], vert=False)
        axs[i, 1].set_xlim([0, 10])

        # Calculate the interquartile range (IQR) and whisker lengths
        iqr, lower_whisker_length, upper_whisker_length = calculate_boxplot_stats(dist['data'])
        # Add text labels for box plot statistics
        axs[i, 1].text(1, 1.4, f'IQR: {iqr:.2f}')
        axs[i, 1].text(1, 1.3, f'Lower whisker length: {lower_whisker_length:.2f}')
        axs[i, 1].text(1, 1.2, f'Upper whisker length: {upper_whisker_length:.2f}')
        
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent
    # Replace spaces in title with underscores to create filename for saving figure
    title = "Skewed and Symmetric Data"
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
    multi_box_plot()
