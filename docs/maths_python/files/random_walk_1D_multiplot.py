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


def plot_random_walks_1d(startpos):
    """
    Performs 4 random walks and plots their positions on the same graph using different colors.
    """
    colors = ['b', 'g', 'r', 'c']
    for i in range(4):
        positions = random_walk_1d(startpos)
        plt.plot(positions, color=colors[i], label=f'Walk {i+1}')
    plt.title("Random Walks 1D")
    plt.xlabel("Step")
    plt.ylabel("Position")
    plt.legend()
    save_plot(plt, "random_walk_1D_multi.png")
    plt.show()



def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)



plot_random_walks_1d(3)


