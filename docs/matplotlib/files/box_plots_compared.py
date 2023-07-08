import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


import numpy as np

def calculate_boxplot_stats(data):
    # Calculate the first and third quartiles
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    # Calculate the interquartile range (IQR)
    iqr = q3 - q1
    # Calculate the lower and upper bounds for outliers
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    # Calculate the adjacent values
    adjacent_lower = np.max(data[data >= lower_bound])
    adjacent_upper = np.min(data[data <= upper_bound])
    # Calculate the length of the whiskers
    lower_whisker_length = adjacent_lower - q1
    upper_whisker_length = q3 - adjacent_upper
    return iqr, lower_whisker_length, upper_whisker_length


def multi_box_plot():
    # Set the random seed for reproducibility
    np.random.seed(0)
    # Generate positively skewed data
    pos_skewed_data = np.random.gamma(shape=1, scale=1.5, size=100)
    pos_skewed_data = pos_skewed_data[(pos_skewed_data >= 0) & (pos_skewed_data <= 10)]
    # Generate negatively skewed data
    neg_skewed_data = 10 - np.random.gamma(shape=1, scale=1.5, size=100)
    neg_skewed_data = neg_skewed_data[(neg_skewed_data >= 0) & (neg_skewed_data <= 10)]
    # Generate symmetric data
    symmetric_data = np.random.normal(loc=5.0, scale=1.5, size=100)
    symmetric_data = symmetric_data[(symmetric_data >= 0) & (symmetric_data <= 10)]
    # Create figure with 3x2 subplots
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(8, 12))
    # Add title to figure
    fig.suptitle('Comparison of Skewed and Symmetric Data', y=0.96)

    # Create histogram and box plot for positively skewed data
    axs[0, 0].hist(pos_skewed_data, bins=10, range=(0, 10))
    axs[0, 0].set_title('Positively Skewed Data')
    axs[0, 1].boxplot(pos_skewed_data, vert=False)
    axs[0, 1].set_xlim([0, 10])
    # Calculate the interquartile range (IQR) and whiskr lengths
    iqr, lower_whisker_length, upper_whisker_length = calculate_boxplot_stats(pos_skewed_data)
    # Add text labels for box plot statistics
    axs[0, 1].text(1, 1.4, f'IQR: {iqr:.2f}')
    axs[0, 1].text(1, 1.3, f'Lower whisker length: {lower_whisker_length:.2f}')
    axs[0, 1].text(1, 1.2, f'Upper whisker length: {upper_whisker_length:.2f}')

    # Create histogram and box plot for symmetric data
    axs[1, 0].hist(symmetric_data, bins=10, range=(0, 10))
    axs[1, 0].set_title('Symmetric Data')
    axs[1, 1].boxplot(symmetric_data, vert=False)
    axs[1, 1].set_xlim([0, 10])
    # Calculate the interquartile range (IQR) and whiskr lengths
    iqr, lower_whisker_length, upper_whisker_length = calculate_boxplot_stats(symmetric_data)
    # Add text labels for box plot statistics
    axs[1, 1].text(1, 1.4, f'IQR: {iqr:.2f}')
    axs[1, 1].text(1, 1.3, f'Lower whisker length: {lower_whisker_length:.2f}')
    axs[1, 1].text(1, 1.2, f'Upper whisker length: {upper_whisker_length:.2f}')


    # Create histogram and box plot for negatively skewed data
    axs[2, 0].hist(neg_skewed_data, bins=10, range=(0, 10))
    axs[2, 0].set_title('Negatively Skewed Data')
    axs[2, 1].boxplot(neg_skewed_data, vert=False)
    axs[2, 1].set_xlim([0, 10])
    # Calculate the interquartile range (IQR) and whiskr lengths
    iqr, lower_whisker_length, upper_whisker_length = calculate_boxplot_stats(neg_skewed_data)
    # Add text labels for box plot statistics
    axs[2, 1].text(1, 1.4, f'IQR: {iqr:.2f}')
    axs[2, 1].text(1, 1.3, f'Lower whisker length: {lower_whisker_length:.2f}')
    axs[2, 1].text(1, 1.2, f'Upper whisker length: {upper_whisker_length:.2f}')

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
