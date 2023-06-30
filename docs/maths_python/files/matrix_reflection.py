import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import to_rgba, LinearSegmentedColormap
from pathlib import Path

currfile_dir = Path(__file__).parent


def plot_reflection(points, point_names, axis, filename):
    """
    Plots the reflection of a list of points about the x-axis or y-axis.

    Args:
        points (List[np.ndarray]): A list of points, where each point is represented as a numpy array of shape (2,).
        point_names (List[str]): A list of point names, where each name corresponds to a point in the `points` list.
        axis (str): The axis to reflect the points about. Must be either 'x' or 'y'.
        filename (str): The filename to save the plot as.

    Returns:
        None
    """
    if axis not in ["x", "y"]:
        raise ValueError("Invalid axis. Must be either 'x' or 'y'.")
    colors = ["blue", "green", "brown", "purple", "orange"]
    light_colors = ["lightblue", "lightgreen", "burlywood", "thistle", "moccasin"]
    intermediate_colors = [
        LinearSegmentedColormap.from_list(
            "", [to_rgba(colors[i]), to_rgba(light_colors[i])]
        )(0.7)
        for i in range(len(colors))
    ]
    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticks(np.arange(-10, 10, 1))
    ax.set_yticks(np.arange(-10, 10, 1))
    for i, (point, point_name) in enumerate(zip(points, point_names)):
        if axis == "x":
            reflected_point = np.array([point[0], -point[1]])
            plt.annotate(
                f"{point_name}: ({point[0]}, {point[1]})",
                (point[0] + 0.2, point[1] + 0.2),
            )
            plt.text(
                reflected_point[0] + 0.2,
                reflected_point[1] + 0.2,
                f"{point_name}$^\prime$: ({reflected_point[0]}, {reflected_point[1]})",
            )
        else:
            reflected_point = np.array([-point[0], point[1]])
            plt.annotate(
                f"{point_name}: ({point[0]}, {point[1]})",
                (point[0] + 0.2, point[1] + 0.2),
            )
            plt.text(
                reflected_point[0] + 0.2,
                reflected_point[1] + 0.2,
                f"{point_name}$^\prime$: ({reflected_point[0]}, {reflected_point[1]})",
            )
        plt.scatter(
            point[0], point[1], color=colors[i % len(colors)], label=f"{point_name}"
        )
        plt.scatter(
            reflected_point[0],
            reflected_point[1],
            color=intermediate_colors[i % len(intermediate_colors)],
            label=f"{point_name}$^\prime$",
        )
        # Shorten the arrows
        dx = reflected_point[0] - point[0]
        dy = reflected_point[1] - point[1]
        dx -= np.sign(dx) * 0.8
        dy -= np.sign(dy) * 0.8

        plt.arrow(
            point[0],
            point[1],
            dx,
            dy,
            head_width=0.5,
            head_length=0.5,
            overhang=1,
            color=colors[i % len(colors)],
        )
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.legend(bbox_to_anchor=(1.05, 0.5), loc="upper left")
    plt.title(f"Reflection about the {axis}-axis")
    plt.subplots_adjust(right=0.8)
    # Change grid lines to be dotted except for the grid lines going through the origin
    ax.grid(True, which="both", linestyle="--")
    # Make the axis lines grey instead of black
    ax.axhline(y=0, color="grey")
    ax.axvline(x=0, color="grey")
    save_plot(plt, filename)
    plt.show()


def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


points = [np.array([5, 2]), np.array([-4, -6])]
point_names = ["A", "B"]
plot_reflection(points, point_names, "x", "matrix_reflection_x.png")
plot_reflection(points, point_names, "y", "matrix_reflection_y.png")
