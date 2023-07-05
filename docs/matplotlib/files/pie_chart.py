import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def plot_pie_chart(data, labels, title):
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent
    # Set the style for the plot
    # plt.style.use('seaborn-v0_8-whitegrid')
    # Create a list of values to determine how far each wedge of the pie chart should be offset from the center
    explode = [0 if x > 8 else 0.3 for x in data]
    # Define the colors to use for the pie chart
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    # Plot the pie chart with the given data, labels, and formatting options
    wedges, texts, autotexts = plt.pie(data, labels=labels, autopct='%1.1f%%', explode=explode, pctdistance=0.8, colors=colors)
    # Set the font size and weight for the data labels
    plt.setp(autotexts, size=8, weight="bold")
    # Set the aspect ratio of the plot to be equal
    plt.axis('equal')
    # Add some space around the plot
    plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1)
    # Add a title to the plot. The y parameter determines the vertical position of the title relative to the top of the axes. In this case, setting it to 1.08 which means that the title will be placed slightly above its default position.
    plt.title(title, y=1.08)
    filename = title.replace(" ","_")
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    filepath = currfile_dir / (f"{filename}.png")
    plt.savefig(filepath, dpi=600)
    # Show plot
    plt.show()

def main():
    # Data to plot
    data = [47, 28, 8, 5, 12]
    labels = ['O', 'Si', 'Al', 'Fe', 'rest']
    title = "Elements in the Earth's Crust"
    # Call the function to plot the data
    plot_pie_chart(data, labels, title)

if __name__ == '__main__':
    main()
