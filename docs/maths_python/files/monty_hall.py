import random
import matplotlib.pyplot as plt
from pathlib import Path

currfile_dir = Path(__file__).parent


def monty_hall():
    """
    Simulates one round of the Monty Hall problem and returns True if switching wins the car, False otherwise.

    Returns:
        bool: The outcome of switching.
    """
    # Create a list of three doors, one with a car and two with goats
    doors = ["car", "goat", "goat"]
    # Shuffle the list randomly
    random.shuffle(doors)
    # Choose a door at random as the initial choice
    choice = random.randint(0, 2)
    # Find the index of the door with the car
    car = doors.index("car")
    # Find the index of a door with a goat that is not the initial choice
    goat = random.choice([i for i in range(3) if i != choice and i != car])
    # Switch to the other door that is not the initial choice or the revealed goat
    switch = 3 - choice - goat
    # Return True if switching wins the car, False otherwise
    return switch == car


def monty_hall_simulation(n, filename):
    """
    Simulates n rounds of the Monty Hall problem and plots the outcomes of switching against the number of rounds.

    Args:
        n (int): The number of rounds to simulate.
        filename (str): The filename to save the plot as.
    """
    # Initialize a list to store the outcomes of switching
    switch_outcomes = []
    # Initialize a variable to count the number of wins by switching
    switch_wins = 0
    # Loop over n rounds
    for i in range(n):
        # Simulate one round and get the outcome
        outcome = monty_hall()
        # Update the number of wins by switching
        switch_wins += outcome
        # Append the proportion of wins by switching so far to the list
        switch_outcomes.append(switch_wins / (i + 1))
    # Call the plot function with the list of outcomes and n
    plot_outcomes(switch_outcomes, n, filename)


def plot_outcomes(switch_outcomes, n, filename):
    """
    Plots the outcomes of switching against the number of rounds and saves the plot to a file.

    Args:
        switch_outcomes (list): The list of outcomes of switching.
        n (int): The number of rounds.
        filename (str): The filename to save the plot as.
    """
    # Plot the list of outcomes against the number of rounds
    plt.plot(range(1, n + 1), switch_outcomes)
    # Add labels and title
    plt.xlabel("Number of rounds")
    plt.ylabel("Proportion of wins by switching")
    plt.title("Monty Hall Simulation")
    plt.ylim(0, 1)
    # Add a horizontal line, grey dashed at 0.67
    plt.axhline(0.67, color="grey", linestyle="--")
    # Save and show the plot
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


monty_hall_simulation(200, "monty_hall_200.png")
