"""Simulates a 1D random walk
"""
from pathlib import Path
import random
import matplotlib.pyplot as plt

currfile_dir = Path(__file__).parent


def random_walk_1d(start=3):
    """
    Simulates a 1D random walk starting at position `start`.
    The walk continues until the position is either 0 or 10.
    Returns a list of all positions visited during the walk.
    """
    x = start
    x_positions = [x]
    while x > 0 and x < 10:
        step = random.choice([-1, 1])
        if step == 1:
            x += 1
        else:
            x -= 1
        x_positions.append(x)
    return x_positions


def calculate_random_walk_1d(start_poss, number_of_walks):
    """
    Calculates the percentage of safe walks for each starting position in `start_poss`.
    A walk is considered safe if it ends at position 0.
    Returns a list of percentages for each starting position.
    """
    safe_counts = []
    for start_pos in start_poss:
        safe_count = 0
        for _ in range(number_of_walks):
            walk_x_positions = random_walk_1d(start_pos)
            if walk_x_positions[-1] == 0:
                safe_count += 1
        safe_counts.append(int(100 * safe_count / number_of_walks))
    return safe_counts


def plot_random_walk_1d(y, x):
    """
    Plots the percentage of safe walks for each starting position.
    `y` is a list of starting positions and `x` is a list of percentages.
    """
    plt.plot(y, x, marker="o")
    plt.title("Random walks 1D")
    plt.xlabel("Starting Position")
    plt.ylabel("Percentage of Safe Walks")
    for i in range(0, 110, 10):
        plt.axhline(y=i, color="gray", linestyle=":")
    for i in range(0, max(start_poss) + 2):
        plt.axvline(x=i, color="gray", linestyle=":")
    for i, j in zip(y, x):
        plt.annotate(str(j), xy=(i, j + 2), color="darkblue")
    save_plot(plt, "random_walks_1D.png")
    plt.show()


def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


number_of_walks = 10000
start_poss = range(1, 10)
safe_counts = calculate_random_walk_1d(start_poss, number_of_walks)
plot_random_walk_1d(start_poss, safe_counts)
