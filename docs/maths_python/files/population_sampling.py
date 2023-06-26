"""population variation
"""

import numpy as np
import matplotlib.pyplot as plt

# Set the population parameters
population_size = 10000
population_mean = 50
population_std = 10

# Generate the population
population = np.random.normal(loc=population_mean, scale=population_std, size=population_size)

# Set the sample parameters
sample_size = 100
number_of_samples = 20

# Generate the samples
samples = np.random.choice(population, size=(number_of_samples, sample_size))

# Calculate the sample means and proportions
sample_means = samples.mean(axis=1)
sample_proportions = (samples > population_mean).mean(axis=1)

# Plot the sample means and proportions
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].hist(sample_means)
ax[0].set_title('Sample Means')
ax[1].hist(sample_proportions)
ax[1].set_title('Sample Proportions')
# Save the figure as a PNG image
plt.savefig('sample_means_and_proportions10.png', dpi=600)

# plt.show()
