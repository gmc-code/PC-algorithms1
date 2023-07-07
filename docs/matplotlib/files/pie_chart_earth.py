import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def plot_pie_chart(data, labels, full_labels, title):
    # Create a list of values to determine how far each wedge of the pie chart should be offset from the center
    explode = [0 if x > 8 else 0.3 for x in data]
    # Define the colors to use for the pie chart
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    # Plot the pie chart with the given data, labels, and formatting options
    wedges, texts, autotexts = plt.pie(data, labels=labels, autopct=lambda pct: f"{pct:.0f}%", explode=explode, pctdistance=0.8, colors=colors, startangle = 90)
    # Set the font size  for the data labels
    plt.setp(texts, size=16)
    # Set the font size and weight for the data labels
    plt.setp(autotexts, size=12, weight="bold")
    # Set the aspect ratio of the plot to be equal
    plt.axis('equal')
    # Add some space around the plot
    plt.subplots_adjust(left=0.1, right=0.70, top=0.85, bottom=0.1)
    # Add a title to the plot
    plt.title(title, y=1.08, size=18)
    # Add a legend to the plot using the given full_labels and colors from the pie chart
    plt.legend(wedges, full_labels, title="Elements", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent# Replace spaces in title with underscores to create filename for saving figure
    filename = title.replace(" ", "_")
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    filepath = currfile_dir / (f"{filename}.png")
    plt.savefig(filepath, dpi=600)
    # Show plot
    plt.show()


def earth_elements():
    # Data to plot
    data = [47, 28, 8, 5, 12]
    # Labels for each wedge of the pie chart
    labels = ['O', 'Si', 'Al', 'Fe', 'Others']
    # Full labels for legend
    full_labels = ['O, Oxygen', 'Si, Silicon', 'Al, Aluminium', 'Fe, Iron', 'Others']
    # Title for plot and filename for saving figure
    title = "Elements in the Earth's Crust"
    # Call the function to plot the data with given data, labels, title and full_labels
    plot_pie_chart(data, labels, full_labels, title)



if __name__ == '__main__':
    earth_elements()
