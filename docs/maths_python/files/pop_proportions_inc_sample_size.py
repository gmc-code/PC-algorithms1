"""histograms increasing the number of samples
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

currfile_dir = Path(__file__).parent

# Set the population parameters
population = ['blue'] * 100 + ['red'] * 400

# Set the sample parameters
sample_size_list = [10, 20, 40, 100]
number_of_samples = 20

def inc_sample_size_proportions(sample_size_list,number_of_samples):
    fig, ax = plt.subplots(1, 4, figsize=(15, 5), sharex=True)
    # Generate the samples
    for i in range(len(sample_size_list)):
        samples = [np.random.choice(population, size=sample_size_list[i], replace=False) for _ in range(number_of_samples)]
        # Calculate the sample proportions
        sample_proportions = [np.mean(sample == 'blue') for sample in samples]
        # Plot the sample proportions
        
        ax[i].hist(sample_proportions)
        ax[i].set_title('Sample Proportions: size ' + str(sample_size_list[i]))
    # Add a title to the figure
    fig.suptitle('Proportion of Blue Balls')
    # Save the figure as a PNG image
    filepath = currfile_dir / ('sample_proportions_inc_size.png')
    plt.savefig(filepath, dpi=600)
    plt.show()

inc_sample_size_proportions(sample_size_list,number_of_samples)

