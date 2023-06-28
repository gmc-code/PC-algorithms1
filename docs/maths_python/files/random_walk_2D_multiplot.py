import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
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

def plot_walks(walks):
    """
    Plot the paths of multiple 2D random walks.

    Parameters:
    walks (list): A list of lists of (x, y) coordinates visited during each walk.
    """
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    max_coord = 0
    for i, coords in enumerate(walks):
        color = colors[i % len(colors)]
        x_coords = [x for x, y in coords]
        y_coords = [y for x, y in coords]
        plt.plot(x_coords, y_coords, color=color, label=f'Walk {i+1}')
        start_color = to_rgba(color)
        end_color = to_rgba(color)
        plt.scatter(x_coords[0], y_coords[0], color=start_color[:3] + (0.3,))
        plt.scatter(x_coords[-1], y_coords[-1], color=end_color[:3] + (0.7,), label=f'End {i+1}')
        max_coord = max(max_coord, max(map(abs, x_coords)), max(map(abs, y_coords)))
    
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
    plt.title(f'Random Walks ({len(coords)-1} steps)')
    plt.subplots_adjust(right=0.7)
    
    save_plot(plt, f'random_walks_2D_multi_{len(coords)-1}_steps')
    
    plt.show()


def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


# Example usage:
walks = [random_walk(20) for _ in range(4)]
plot_walks(walks)
walks = [random_walk(50) for _ in range(6)]
plot_walks(walks)
walks = [random_walk(1000) for _ in range(6)]
plot_walks(walks)