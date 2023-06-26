"""histograms that show that by increasing the number of samples, the better the samples means fit a normal distibution
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

currfile_dir = Path(__file__).parent

# Set the population parameters
population_size = 10000
population_mean = 50
population_std = 10

# Generate the population
population = np.random.normal(loc=population_mean, scale=population_std, size=population_size)

# Set the sample parameters
sample_size_list = [10, 100, 1000]
number_of_samples = 100



def output_sample_means(sample_size_list,number_of_samples):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5), sharex=True)
    # Generate the samples
    for i in range(len(sample_size_list)):
        samples = np.random.choice(population, size=(number_of_samples, sample_size_list[i]))
        # Calculate the sample means and proportions
        sample_means = samples.mean(axis=1)
        # Plot the sample means and proportions
        
        ax[i].hist(sample_means)
        ax[i].set_title('Sample Means: size ' + str(sample_size_list[i]))
    # Plot the population histogram
    # ax[3].hist(population)
    # ax[3].set_title('Population')

    # Save the figure as a PNG image
    filepath = currfile_dir / ('sample_means_inc_size.png')
    plt.savefig(filepath, dpi=600)
    plt.show()

output_sample_means(sample_size_list,number_of_samples)

