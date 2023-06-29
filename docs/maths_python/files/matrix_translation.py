import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from pathlib import Path

currfile_dir = Path(__file__).parent


def plot_translation(point, translation, filename):
    """
    Plots the translation of a point by a given translation vector.

    Args:
        point (np.ndarray): The coordinates of the original point as a numpy array of shape (2,).
        translation (np.ndarray): The translation vector as a numpy array of shape (2,).
        filename (str): The filename to save the plot as.

    Returns:
        None
    """
    transformed_point = point + translation

    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))

    plt.scatter(point[0], point[1], color="blue", label="A Original Point")
    plt.scatter(
        transformed_point[0],
        transformed_point[1],
        color="red",
        label="A$^\prime$ Translated Point",
    )
    plt.arrow(
        point[0],
        point[1],
        transformed_point[0] - point[0] - 0.5,
        transformed_point[1] - point[1] - 0.5,
        head_width=0.5,
        head_length=0.5,
        overhang=1,
    )
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.legend(loc="lower right")
    plt.annotate(r"A" + f"({point[0]}, {point[1]})", (point[0] + 0.1, point[1] - 0.5))
    plt.text(
        transformed_point[0] + 0.1,
        transformed_point[1] + 0.2,
        r"A$^\prime$" + f"({transformed_point[0]}, {transformed_point[1]})",
    )
    plt.title(f"Translation by ({translation[0]}, {translation[1]})")
    plt.grid(True)
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


point = np.array([1, 2])
translation = np.array([3, 4])
plot_translation(point, translation, "matrix_translation.png")
