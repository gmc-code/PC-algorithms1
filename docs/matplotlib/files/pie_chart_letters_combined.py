import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path


def plot_pie_chart(data, labels, full_labels, title):
    # Define the colors to use for the pie chart
    colors = colors=[plt.cm.tab20(i) for i in range(20)]  # plt.cm.rainbow(np.linspace(0, 1, 20))
    # Create a figure object with a size of 10 by 10 inches
    plt.figure(figsize=(8, 8))   
    # Plot the pie chart with the given data, labels, and formatting options
    wedges, texts, autotexts = plt.pie(data, labels=labels, autopct=lambda pct: f"{pct:.1f}%" if pct >= 2 else f"{pct:.2f}%", pctdistance=1.1, labeldistance=1.22, startangle = 270, colors=colors, radius=1.5)
    # Set the font size and color for the data
    plt.setp(texts, size=14, color='k')
    # Set the font size and color for the data labels
    plt.setp(autotexts, size=10, color='k')
    # Set the aspect ratio of the plot to be equal
    plt.axis('equal')
    # Add some space around the plot
    plt.subplots_adjust(left=0.1, right=0.70, top=0.85, bottom=0.1)
    # Add a title to the plot
    plt.title(title, y=1.08, size=18)
    # Add a legend to the plot using the given full_labels and colors from the pie chart
    plt.legend(wedges, full_labels, title="Elements", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))
    # Adjust the label for the last wedge by using the last text object in texts
    last_text = texts[-1]
        # Get the current position of the last text object
    x, y = last_text.get_position()
    # Add a small amount to the x and y coordinates
    x += 0.4
    y += 0.0
    # Set the new position of the last text object
    last_text.set_position((x,y))
    last_text.set_size(12) # Set the font size to 10
    # Get the directory of the current file
    currfile_dir = Path(__file__).parent
    # Replace spaces in title with underscores to create filename for saving figure
    filename = title.replace(" ", "_")
    # build the image file path
    filepath = currfile_dir / (f"{filename}.png")
    # Save figure (dpi 300 is good when saving so graph has high resolution)
    plt.savefig(filepath, dpi=600)
    # Show plot
    plt.show()


def letters_usage_sorted():
    currfile_dir = Path(__file__).parent# Replace spaces in title with underscores to create filename for saving figure
    filepath = currfile_dir / 'letter_frequency.csv'
    # Read data from csv file into pandas dataframe.
    data = pd.read_csv(filepath)
    # Sort data by frequency column in descending order.
    data.sort_values(by='frequency', ascending=False, inplace=True)
    # Extract letters and frequency values from dataframe.
    letters = data['letter']
    values = data['frequency'] * 100
    # Initialize lists to store filtered letters and values.
    filtered_letters = []
    filtered_values = []
    other_letters = []
    other_value = 0
    # Iterate over letters and values.
    for letter, value in zip(letters, values):
            if value > 2:
                filtered_letters.append(letter)
                filtered_values.append(value)
            else:
                other_letters.append(letter)
                other_value += value
    # Join the other letters and add the other wedge to the filtered data.
    other_label = "".join(other_letters)
    filtered_letters.append(other_label)
    filtered_values.append(other_value)
    # Data to plot.
    data = filtered_values
    # Labels for each wedge of the pie chart.
    labels = filtered_letters
    # Full labels for legend.
    full_labels = filtered_letters
    # Title for plot and filename for saving figure.
    title = "Letter frequency sorted"
    # Call the function to plot the data with given data, labels, title and full_labels.
    plot_pie_chart(data, labels, full_labels, title)


if __name__ == '__main__':
    letters_usage_sorted()
