import random
import matplotlib.pyplot as plt
from pathlib import Path

currfile_dir = Path(__file__).parent


def is_derangement(permutation):
    """
    Checks if a permutation is a derangement, which means that no element appears in its original position.

    Args:
        permutation (list): A list of integers representing a permutation of n elements from 0 to n-1.

    Returns:
        bool: True if the permutation is a derangement, False otherwise.
    """
    # Loop over the permutation
    for i in range(len(permutation)):
        # If any element is in its original position, return False
        if permutation[i] == i:
            return False
    # If no element is in its original position, return True
    return True


def random_permutation(n):
    """
    Generates a random permutation of n elements from 0 to n-1.

    Args:
        n (int): The number of elements in the permutation.

    Returns:
        list: A list of integers representing a random permutation of n elements from 0 to n-1.
    """
    # Create a list of n elements from 0 to n-1
    elements = list(range(n))
    # Shuffle the list randomly
    random.shuffle(elements)
    # Return the shuffled list
    return elements


def derangement_simulation(n):
    """
    Simulates n rounds of generating a random permutation of n elements and checking if it is a derangement.
    Returns the proportion of derangements out of n permutations.

    Args:
        n (int): The number of elements in the permutation and the number of rounds to simulate.

    Returns:
        float: The proportion of derangements out of n permutations.
    """
    # Initialize a variable to count the number of derangements
    derangements = 0
    # Loop over n rounds
    for i in range(n):
        # Generate a random permutation of n elements
        permutation = random_permutation(n)
        # Check if the permutation is a derangement and update the count
        if is_derangement(permutation):
            derangements += 1

    # Calculate and return the proportion of derangements
    proportion = derangements / n
    return proportion


def repeat_simulation(m, n, filename):
    """
    Repeats the simulation m times with n elements and plots the histogram of the proportions of derangements.

    Args:
        m (int): The number of times to repeat the simulation.
        n (int): The number of elements in the permutation.
        filename (str): The filename to save the plot as.
    """
    # Initialize a list to store the proportions of derangements
    proportions = []
    # Initialize a variable to store the sum of the proportions
    total = 0
    # Loop over m times
    for i in range(m):
        # Call the simulation function with n elements and append the result to the list
        proportion = derangement_simulation(n)
        proportions.append(proportion)
        # Add the proportion to the total
        total += proportion

    # Plot the histogram of the proportions with bins and labels
    plt.hist(proportions, bins=20)
    plt.xlabel("Proportion of derangements")
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {m} simulations with {n} elements")

    # Calculate and print the overall probability by dividing the total by m
    probability = total / m

    # Put the overall probability in a text box on the top right of the plot
    plt.text(
        0.95,
        0.95,
        f"Overall probability: {probability:.4f}",
        horizontalalignment="right",
        verticalalignment="top",
        transform=plt.gca().transAxes,
    )

    # Show the plot
    save_plot(plt, filename)
    plt.show()


def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory.

    Args:
        plot (matplotlib.pyplot): The plot to save.
        filename (str): The filename to save the plot as.
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


repeat_simulation(1000, 100, "derangement_100.png")
