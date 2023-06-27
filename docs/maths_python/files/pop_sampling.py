"""histograms of pop
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

currfile_dir = Path(__file__).parent

# Set the parameters of the trimodal distribution
p1 = 0.174
p2 = 0.505
p3 = 0.321
mu1 = 6
mu2 = 33
mu3 = 64
sigma1 = 8
sigma2 = 15
sigma3 = 15
# Generate a sample population of 10000
population_size = 10000
population = np.random.normal(loc=[mu1, mu2, mu3], scale=[sigma1, sigma2, sigma3], size=(population_size, 3))
weights = np.random.choice([0, 1, 2], size=population_size, p=[p1, p2, p3])
population = population[np.arange(population_size), weights]

# Plot a normalized histogram of the sample population
weights = np.ones_like(population) / float(len(population)) * 100 # Normalize the weights so that they sum to 100

# Set the bin width and generate the bin edges
bin_width = 5
bins = np.arange(0, population.max() + bin_width, bin_width)

# Plot a normalized histogram of the sample population with custom bin colors
weights = np.ones_like(population) / float(len(population)) * 100 # Normalize the weights so that they sum to 100
n_bins = len(bins) - 1
colors = ['#89CFF0', '#90EE90', '#FFB6C1', '#FFCBA4'] * (n_bins // 4)
n, bins, patches = plt.hist(population, bins=bins, weights=weights)
for patch, color in zip(patches, colors):
    patch.set_fc(color)

plt.xlim(left=0) # Set the lower limit of the x-axis to 0
plt.xlim(right=100)
plt.xlabel('Age')
plt.ylabel('Percentage')
plt.title('Histogram of Sample Population')

filepath = currfile_dir / ('population_by_age.png')
plt.savefig(filepath, dpi=600)
plt.show()