import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import to_rgba, LinearSegmentedColormap
from pathlib import Path

currfile_dir = Path(__file__).parent


def plot_transformation(points, point_names, matrix_reflection, filename):
    """
    Plots the reflection of a list of points about the x-axis or y-axis.

    Args:
        points (List[np.ndarray]): A list of points, where each point is represented as a numpy array of shape (2,).
        point_names (List[str]): A list of point names, where each name corresponds to a point in the `points` list.
        matrix_reflection (np.ndarray): The reflection matrix to use for reflecting the points. Must be a numpy array of shape (2, 2).
        filename (str): The filename to save the plot as.

    Returns:
        None
    """
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
        transformed_point = matrix_reflection.dot(point)
        plt.annotate(
            f"{point_name} ({point[0]}, {point[1]})",
            (point[0] + 0.2, point[1] + 0.2),
        )
        plt.text(
            transformed_point[0] + 0.2,
            transformed_point[1] + 0.2,
            f"{point_name}$^\prime$ ({transformed_point[0]}, {transformed_point[1]})",
        )
        plt.scatter(
            point[0], point[1], color=colors[i % len(colors)], label=f"{point_name}"
        )
        plt.scatter(
            transformed_point[0],
            transformed_point[1],
            color=intermediate_colors[i % len(intermediate_colors)],
            label=f"{point_name}$^\prime$",
        )     
        # Shorten the arrows
        dx = transformed_point[0] - point[0]
        dy = transformed_point[1] - point[1]
        # dx -= np.sign(dx) * 0.8
        # dy -= np.sign(dy) * 0.8
        # Reduce the line length by 0.8
        if dx == 0:
            dy -= np.sign(dy) * 0.8
        elif dy == 0:
            dx -= np.sign(dx) * 0.8
        else:   
            gradient = abs(dy / dx)
            dx -= np.sign(dx) * 0.8 / np.sqrt(1 + gradient**2)
            dy -= np.sign(dy) * 0.8 * gradient / np.sqrt(1 + gradient**2)


        plt.arrow(
            point[0],point[1],dx,dy,head_width=0.5,head_length=0.5,overhang=1,
            color=colors[i % len(colors)],
        )
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.legend(bbox_to_anchor=(1.05, 0.5), loc="upper left")
    plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))
    plt.subplots_adjust(right=0.8)

    title_str = f"Transformation by {np.array2string(matrix_reflection, separator=', ', prefix='[', suffix=']', max_line_width=np.inf)}".replace("\n", "")
    plt.title(title_str)
    # Change grid lines to be dotted except for the grid lines going through the origin
    ax.grid(True, which="both", linestyle="--")
    # Make the axis lines grey instead of black
    ax.axhline(y=0, color="grey")
    ax.axvline(x=0, color="grey")
    save_plot(plt, filename)
    # plt.show()


def save_plot(plot, filename):
    "    Saves the given plot to a file with the given filename within the curr directory"
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


points = [np.array([4, 6]), np.array([-2, -4])]  # , np.array([-2, -2]), np.array([-3, 2])
point_names = ["A", "B"]  # , "C", "D"
# Define reflection matrices for reflecting about x-axis and y-axis
matrix_reflection_x = np.array([[1, 0], [0, -1]])
matrix_reflection_y = np.array([[-1, 0], [0, 1]])
matrix_reflection_yisx = np.array([[0, 1], [1, 0]])
matrix_reflection_yisnegx = np.array([[0, -1], [-1, 0]])
matrix_rotation_90clock = np.array([[0, 1], [-1, 0]])
matrix_rotation_180clock = np.array([[-1, 0], [0, -1]])
matrix_rotation_270clock = np.array([[0, -1], [1, 0]])
matrix_dilation_05 = np.array([[0.5, 0], [0, 0.5]])
matrix_dilation_15 = np.array([[1.5, 0], [0, 1.5]])
plot_transformation(points, point_names, matrix_reflection_x,"matrix_reflection_x.png")
plot_transformation(points, point_names, matrix_reflection_y,"matrix_reflection_y.png")
plot_transformation(points, point_names, matrix_reflection_yisx,"matrix_reflection_y=x.png")
plot_transformation(points, point_names, matrix_reflection_yisnegx,"matrix_reflection_y=-x.png")
plot_transformation(points, point_names, matrix_rotation_90clock,"matrix_rotation_90clock.png")
plot_transformation(points, point_names, matrix_rotation_180clock,"matrix_rotation_180clock.png")
plot_transformation(points, point_names, matrix_rotation_270clock,"matrix_rotation_270clock.png")
plot_transformation(points, point_names, matrix_dilation_05,"matrix_dilation_05.png")
plot_transformation(points, point_names, matrix_dilation_15,"matrix_dilation_15.png")