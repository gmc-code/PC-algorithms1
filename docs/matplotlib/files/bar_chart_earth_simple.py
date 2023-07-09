import matplotlib.pyplot as plt


def plot_bar_chart(data, labels, title, xlabel, ylabel):
    # Plot the bar chart with the given data, labels, and formatting options
    plt.bar(labels, data)
    # X and Y labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # Add a title to the plot
    plt.title(title)
    # Show plot
    plt.show()


def earth_elements():
    # Data to plot
    data = [47, 28, 8, 5, 12]
    # Labels for each wedge of the pie chart
    labels = ['O', 'Si', 'Al', 'Fe', 'Others']
    # Title for plot
    title = "Earth's Crust barchart"
    # X axis label
    xlabel = "Element"
    # Y axis label
    ylabel = "Percentage of crust (%)"
    # Call the function to plot the data with given data, labels, title axis labels
    plot_bar_chart(data, labels, title, xlabel, ylabel)


if __name__ == '__main__':
    earth_elements()
