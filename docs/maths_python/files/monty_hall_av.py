import random
import matplotlib.pyplot as plt
from pathlib import Path
import statistics  # Import the statistics module to use the mean function
import webcolors  # Import the webcolors module
import colorsys  # Import the colorsys module


currfile_dir = Path(__file__).parent


def monty_hall():
    """
    Simulates one round of the Monty Hall problem and returns True if switching wins the car, False otherwise.

    Returns:
        bool: The outcome of switching.
    """
    # Create a list of three doors, one with a car and two with goats
    doors = ["car", "goat", "goat"]
    # Shuffle the list randomly
    random.shuffle(doors)
    # Choose a door at random as the initial choice
    choice = random.randint(0, 2)
    # Find the index of the door with the car
    car = doors.index("car")
    # Find the index of a door with a goat that is not the initial choice
    goat = random.choice([i for i in range(3) if i != choice and i != car])
    # Switch to the other door that is not the initial choice or the revealed goat
    switch = 3 - choice - goat
    # Return True if switching wins the car, False otherwise
    return switch == car


def monty_hall_simulation(n):
    """
    Simulates n rounds of the Monty Hall problem and returns a list of outcomes of switching.

    Args:
        n (int): The number of rounds to simulate.

    Returns:
        list: The list of outcomes of switching.
    """
    # Initialize a list to store the outcomes of switching
    switch_outcomes = []
    # Initialize a variable to count the number of wins by switching
    switch_wins = 0
    # Loop over n rounds
    for i in range(n):
        # Simulate one round and get the outcome
        outcome = monty_hall()
        # Update the number of wins by switching
        switch_wins += outcome
        # Append the proportion of wins by switching so far to the list
        switch_outcomes.append(switch_wins / (i + 1))
    # Return the list of outcomes
    return switch_outcomes


def lighten_color_name(color_name, factor):
    """
    Takes a color name and a factor between 0 and 1 and returns a lighter color in RGB format.

    Args:
        color_name (str): The name of the color, such as 'red', 'blue', etc.
        factor (float): The factor by which to increase the value component of the color. Should be between 0 and 1.

    Returns:
        tuple: The lighter color in RGB format as a tuple of three numbers between 0 and 1.
    """
    # Convert the color name to a hex string using the webcolors module
    hex_color = webcolors.name_to_hex(color_name)
    # Convert the hex string to a tuple of RGB values using the webcolors module
    rgb_color = webcolors.hex_to_rgb_percent(hex_color)
    # Convert the RGB values to floats between 0 and 1
    rgb_color = tuple(float(x.strip("%")) / 100 for x in rgb_color)
    # Convert the RGB color to HSV format using the colorsys module
    h, s, v = colorsys.rgb_to_hsv(*rgb_color)
    # Increase the value component by the factor, but make sure it does not exceed 1
    v = min(v + factor, 1)
    # Convert the HSV color back to RGB format using the colorsys module
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    # Return the lighter color as a tuple
    return (r, g, b)


def new_colors():
    # Define a list of color names to use for each simulation
    color_names = [
        "red",
        "orange",
        "plum",
        "green",
        "blue",
        "indigo",
        "violet",
        "pink",
        "brown",
        "skyblue",
        "lightgreen",
        "peachpuff",
        "yellow",
    ]
    # Define a list of factors to use for each color name
    factors = [0.1, 0.2, 0.1, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.4]
    new_colors = []
    for i in range(len(color_names)):
        new_light_color = lighten_color_name(color_names[i], factors[i])
        new_colors.append(new_light_color)
    return new_colors


def plot_outcomes(switch_outcomes, color, rounds, label, linewidth=1, linestyle="-"):
    """
    Plots the outcomes of switching against the first 200 rounds using the given color, label, linewidth and linestyle.

    Args:
        switch_outcomes (list): The list of outcomes of switching.
        color (str): The color to use for the plot.
        rounds (int): The number of trials in the sim
        label (str): The label to use for the plot.
        linewidth (int): The linewidth to use for the plot. Default is 1.
        linestyle (str): The linestyle to use for the plot. Default is '-'.
    """
    # Plot the list of outcomes against the rounds using the given color, label, linewidth and linestyle
    plt.plot(
        range(1, rounds + 1),
        switch_outcomes[:rounds],
        color=color,
        label=label,
        linewidth=linewidth,
        linestyle=linestyle,
    )


def save_plot(plot, filename):
    """
    Saves the given plot to a file with the given filename within the curr directory.

    Args:
        plot (matplotlib.pyplot): The plot to save.
        filename (str): The filename to save the plot as.
    """
    filepath = currfile_dir / filename
    plot.savefig(filepath, dpi=600)


def main(sims, rounds):
    """
    Runs sims simulations of the Monty Hall problem with rounds rounds each and plots them on one figure.
    """
    # Define a list of colors to use for each simulation
    colors = new_colors()
    # Initialize an empty list to store the data from each simulation
    data = []
    # Loop over sims simulations with different number of rounds and store the data in the list
    for i in range(sims):
        data.append(
            monty_hall_simulation(rounds)
        )  # Use append method instead of indexing and pass rounds as argument
    # Initialize an empty list to store the averages from each simulation
    average = []
    # Loop over sims simulations again and calculate and plot each data set with a different color and label
    for i in range(sims):
        # Plot each data set with a different color and label
        color = colors[i]
        # Use the lighten_color function with a factor of 0.2
        plot_outcomes(data[i], color, rounds, f"Simulation {i + 1}")
    # Plot the overall average with grey color and label and double linewidth
    average = [statistics.mean(data[i][k] for i in range(sims)) for k in range(rounds)]
    plot_outcomes(average, "black", rounds, "Overall average", 4, ":")
    # Add labels and title
    plt.xlabel("Number of rounds")
    plt.ylabel("Proportion of wins by switching")
    plt.title("Monty Hall Simulation")
    # plt.xscale("log")
    plt.ylim(0, 1)
    # Add a horizontal line, grey dashed at 0.67
    plt.axhline(0.67, color="grey", linestyle="--")
    # Add a legend in the lower right corner
    plt.legend(loc="lower right")
    # Save and show the plot
    save_plot(plt, "monty_hall_av.png")  # Add a closing parenthesis here
    plt.show()


# Call the main function if this file is run as a script
if __name__ == "__main__":
    main(8, 100)  # Pass the number of simulations and rounds as arguments
