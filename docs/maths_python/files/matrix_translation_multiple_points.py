import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import to_rgba, LinearSegmentedColormap
from pathlib import Path

currfile_dir = Path(__file__).parent

def plot_translation(points, point_names, translation, filename):
    """
    Plots the translation of a list of points by a given translation vector.

    Args:
        points (List[np.ndarray]): A list of points, where each point is represented as a numpy array of shape (2,).
        point_names (List[str]): A list of point names, where each name corresponds to a point in the `points` list.
        translation (np.ndarray): The translation vector as a numpy array of shape (2,).
        filename (str): The filename to save the plot as.

    Returns:
        None
    """
    colors = ['blue', 'green', 'orange', 'purple', 'brown']
    light_colors = ['lightblue', 'lightgreen', 'moccasin', 'thistle', 'burlywood']
    intermediate_colors = [LinearSegmentedColormap.from_list('', [to_rgba(colors[i]), to_rgba(light_colors[i])])(0.7) for i in range(len(colors))]

    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))

    for i, (point, point_name) in enumerate(zip(points, point_names)):
        transformed_point = point + translation
        plt.scatter(point[0], point[1], color=colors[i % len(colors)], label=f'{point_name}')
        plt.scatter(transformed_point[0], transformed_point[1], color=intermediate_colors[i % len(intermediate_colors)], label=f'{point_name}$^\prime$')
        plt.arrow(point[0], point[1], transformed_point[0]-point[0]-0.5, transformed_point[1]-point[1]-0.5, head_width=0.5, head_length=0.5, overhang=1)
        plt.annotate(f'{point_name}: ({point[0]}, {point[1]})', (point[0]+0.1, point[1]-0.5))
        plt.text(transformed_point[0]+0.1, transformed_point[1]+0.2, f'{point_name}$^\prime$: ({transformed_point[0]}, {transformed_point[1]})')

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.legend(loc='lower right')
    plt.title(f'Translation by ({translation[0]}, {translation[1]})')
    plt.grid(True)
    save_plot(plt, filename)
    plt.show()

def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)

points = [np.array([1, 3]), np.array([2, 2]), np.array([3, 1])]
point_names = ['A', 'B', 'C']
translation = np.array([3, 4])
plot_translation(points, point_names, translation, "matrix_translation_multiple_points.png")
