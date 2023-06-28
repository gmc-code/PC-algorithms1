import matplotlib.pyplot as plt
import random
from pathlib import Path
import math

currfile_dir = Path(__file__).parent


def levy_flight(n, levy, min_jump, max_jump):
    """
    Simulate a 2D Lévy flight of `n` steps.

    Parameters:
    n (int): The total number of steps
    levy (int): The number of steps before a Lévy jump.

    Returns:
    list: The list of (x, y) coordinates visitedt.
    """
    x, y = 0, 0
    coords = [(x, y)]
    for i in range(n):
        if i % levy == 0:
            r = random.randrange(min_jump, max_jump)
            theta = random.uniform(0, 2 * math.pi)
            dx, dy = int(r * math.cos(theta)), int(r * math.sin(theta))
        else:
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
        coords.append((x, y))
    return coords


def plot_walk(coords, levy):
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
    if max_coord > 100:
        max_coord = max_coord + (-max_coord % 50)
        ticks = range(-max_coord, max_coord + 1, 50)
    elif max_coord > 60:
        max_coord = max_coord + (-max_coord % 20)
        ticks = range(-max_coord, max_coord + 1, 20)
    elif max_coord > 30:
        max_coord = max_coord + (-max_coord % 10)
        ticks = range(-max_coord, max_coord + 1, 10)
    elif max_coord > 16:
        max_coord = max_coord + (-max_coord % 5)
        ticks = range(-max_coord, max_coord + 1, 5)
    elif max_coord > 8:
        max_coord = max_coord + (-max_coord % 2)
        ticks = range(-max_coord, max_coord + 1, 2)
    else:
        ticks = range(-int(max_coord), int(max_coord) + 1)
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.xlim(-max_coord, max_coord)
    plt.ylim(-max_coord, max_coord)
    plt.legend(loc="center left", bbox_to_anchor=(1.05, 0.5))
    plt.title(f"Random Walk ({len(coords)-1} steps)")
    plt.subplots_adjust(right=0.7)
    save_plot(plt, f"random_walk_Levy_every_{levy}_of_{len(coords)-1}")
    plt.show()


def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


# Example usage:
levy = 100
steps = 1000
min_jump = 10
max_jump = 20
coords = levy_flight(steps, levy, min_jump, max_jump)
plot_walk(coords, levy)
