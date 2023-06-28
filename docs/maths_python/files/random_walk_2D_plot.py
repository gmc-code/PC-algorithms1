import matplotlib.pyplot as plt
import random
from pathlib import Path

currfile_dir = Path(__file__).parent


def random_walk(n):
    """
    Simulate a 2D random walk of `n` steps.

    Parameters:
    n (int): The number of steps in the random walk.

    Returns:
    list: The list of (x, y) coordinates visited during the walk.
    """
    x, y = 0, 0
    coords = [(x, y)]
    for _ in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
        coords.append((x, y))
    return coords


def plot_walk(coords):
    """
    Plot the path of a 2D random walk.

    Parameters:
    coords (list): The list of (x, y) coordinates visited during the walk.
    """
    x_coords = [x for x, y in coords]
    y_coords = [y for x, y in coords]
    plt.plot(x_coords, y_coords)
    plt.scatter(x_coords[0], y_coords[0], color="green", label="Start")
    plt.scatter(x_coords[-1], y_coords[-1], color="red", label="End")
    
    max_coord = max(max(map(abs, x_coords)), max(map(abs, y_coords)))
    
    if max_coord > 30:
        max_coord = max_coord + (-max_coord % 10)
        ticks = range(-max_coord, max_coord + 1, 10)
        
    elif max_coord > 16:
        max_coord = max_coord + (-max_coord % 5)
        ticks = range(-max_coord, max_coord + 1, 5)
        
    elif max_coord > 8:
        max_coord = max_coord + (-max_coord % 2)
        ticks = range(-max_coord, max_coord + 1, 2)
        
    else:
        ticks = range(-max_coord, max_coord + 1)

    plt.xticks(ticks)
    plt.yticks(ticks)

    plt.xlim(-max_coord, max_coord)
    plt.ylim(-max_coord, max_coord)

    plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))
    plt.title(f"Random Walk ({len(coords)-1} steps)")
    plt.subplots_adjust(right=0.7)
    
    save_plot(plt, f'random_walks_2D_{len(coords)-1}_steps')
    
    plt.show()


def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


# Example usage:
coords = random_walk(10)
plot_walk(coords)
coords = random_walk(50)
plot_walk(coords)
coords = random_walk(100)
plot_walk(coords)
coords = random_walk(1000)
plot_walk(coords)
