import matplotlib.pyplot as plt


def plot_pie_chart(data, labels, title):
    # Plot the pie chart with the given data, labels, and formatting options
    plt.pie(data, labels=labels)
    # Set the aspect ratio of the plot to be equal
    plt.axis('equal')
    # Add a title to the plot
    plt.title(title, y=1.08, size=18)
    # Show plot
    plt.show()


def earth_elements():
    # Data to plot
    data = [47, 28, 8, 5, 12]
    # Labels for each wedge of the pie chart
    labels = ['O Oxygen', 'Si Silicon', 'Al Aluminium', 'Fe Iron', 'Others']
    # Title for plot and filename for saving figure
    title = "Earth's Crust"
    # Call the function to plot the data with given data, labels, title and full_labels
    plot_pie_chart(data, labels, title)


if __name__ == '__main__':
    earth_elements()
