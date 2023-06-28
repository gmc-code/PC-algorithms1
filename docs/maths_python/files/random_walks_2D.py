"""Simulates a 2D random walk
"""
from pathlib import Path
import random
import matplotlib.pyplot as plt

currfile_dir = Path(__file__).parent


def random_walk(n):
    """
    Simulates a 2D random walk of `n` steps.
    Returns the final coordinates after the walk.
    """
    x, y = 0, 0
    for _ in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


def simulate_walks(walk_lengths, number_of_walks, dist_to_home):
    """
    Simulates multiple 2D random walks for each walk length in `walk_lengths`.
    Calculates the percentage of walks that end within `dist_to_home` blocks of the origin for each walk length.
    Returns a list of percentages for each walk length.
    """
    percentages = []
    for walkn in walk_lengths:
        close_to_home = 0
        for _ in range(number_of_walks):
            walk = random_walk(walkn)
            if abs(walk[0]) + abs(walk[1]) <= dist_to_home:
                close_to_home += 1
        percentages.append(int(100 * close_to_home / number_of_walks))
    return percentages


def plot_results(y, x):
    """
    Plots the percentage of walks that end within 4 blocks of the origin for each walk length.
    `y` is a list of walk lengths and `x` is a list of percentages.
    """
    plt.plot(y, x)
    plt.title("Random walks 2D")
    plt.xlabel("Walk Length")
    plt.ylabel("Percentage of Walks Within 4 Blocks of Origin")
    plt.axhline(y=50, color="gray", linestyle="--")
    plt.xticks(range(0, max(walk_lengths) + 1, 2))
    plt.grid(axis="x")
    save_plot(plt, "random_walks_2D.png")
    plt.show()


def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


number_of_walks = 1000
walk_lengths = range(30)
dist_to_home = 4
percentages = simulate_walks(walk_lengths, number_of_walks, dist_to_home)
plot_results(walk_lengths, percentages)
