====================================================
Matplotlib pie chart
====================================================

| Matplotlib can be used to draw a pie chart.

----

.. image:: images/Elements_in_the_Earth's_Crust.png
    :width: 600
    :align: center

----


``import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


These lines import the necessary libraries for the code. `matplotlib.pyplot` is a plotting library that provides functions for creating various types of plots. `numpy` is a library for working with arrays of data. `pathlib` is a library for working with file paths.

``def plot_pie_chart(data, labels, title, full_labels):


This line defines a function named `plot_pie_chart` that takes four arguments: `data`, `labels`, `title`, and `full_labels`. The function will use these arguments to create a pie chart with the given data, labels, and title, and a legend with the given full labels.

``    # Get the directory of the current file
    currfile_dir = Path(__file__).parent


This line uses the `Path` class from the `pathlib` library to get the directory of the current file. This will be used later to save the figure to a file in the same directory as the script.

``    # Create a list of values to determine how far each wedge of the pie chart should be offset from the center
    explode = [0 if x > 8 else 0.3 for x in data]


This line uses a list comprehension to create a list of values that will determine how far each wedge of the pie chart should be offset from the center. The list comprehension iterates over each value in `data` and assigns a value of 0 if the value is greater than 8, or 0.3 otherwise. This means that any wedge representing a value less than or equal to 8 will be offset from the center by 0.3 units.

``    # Define the colors to use for the pie chart
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']


This line defines a list of colors to use for the pie chart. Each color is represented as a string containing a hexadecimal color code.

``    # Plot the pie chart with the given data, labels, and formatting options
    wedges, texts, autotexts = plt.pie(data, labels=labels, autopct=lambda pct: f"{pct:.1f}%", explode=explode, pctdistance=0.8, colors=colors)


This line uses the `plt.pie()` function from the `matplotlib.pyplot` library to create a pie chart with the given data and labels. The function also takes several optional arguments to customize the appearance of the pie chart.

The `autopct` argument specifies how to format the percentage values that are displayed on each wedge of the pie chart. In this case, we're using a lambda function that takes a percentage value as input and returns a formatted string containing the value rounded to one decimal place and followed by a percentage sign.

The `explode` argument specifies how far each wedge should be offset from the center. We're passing in the `explode` list that we created earlier.

The `pctdistance` argument specifies how far from the center of each wedge to place its percentage label. In this case, we're setting it to 0.8 which means that each label will be placed closer to its corresponding wedge than it would be by default.

The `colors` argument specifies what colors to use for each wedge of the pie chart. We're passing in the `colors` list that we defined earlier.

The `plt.pie()` function returns three lists: one containing the wedges of the pie chart, one containing their corresponding text labels, and one containing their corresponding percentage labels. We're assigning these lists to variables named `wedges`, `texts`, and `autotexts`, respectively.

``    # Set the font size for text labels
    plt.setp(texts, size=16)


This line uses the `plt.setp()` function from the `matplotlib.pyplot` library to set properties of multiple artists at once. In this case, we're using it to set properties of all text labels in one go.

The first argument passed into this function is an iterable containing all artists whose properties we want to set (in this case, all text labels). The remaining arguments are pairs of property names and values specifying what properties we want to set and what values we want to set them to.

In this case, we're setting only one property: `'size'`. We're setting it to 16 which means that all text labels will have their font size set to 16 points.

``    # Set the font size and weight for percentage labels
    plt.setp(autotexts, size=12, weight="bold")


This line is similar to the previous one, but it sets properties of the percentage labels instead of the text labels. We're setting two properties: `'size'` and `'weight'`. We're setting `'size'` to 12 which means that all percentage labels will have their font size set to 12 points. We're setting `'weight'` to `'bold'` which means that all percentage labels will be displayed in bold font.

``    # Set the aspect ratio of the plot to be equal
    plt.axis('equal')


This line uses the `plt.axis()` function from the `matplotlib.pyplot` library to set the aspect ratio of the plot. The argument `'equal'` means that the x and y axes will have the same scaling, so that circles will appear as circles and squares will appear as squares.

``    # Add some space around the plot
    plt.subplots_adjust(left=0.1, right=0.70, top=0.85, bottom=0.1)


This line uses the `plt.subplots_adjust()` function from the `matplotlib.pyplot` library to adjust the spacing around the plot. The function takes several optional arguments that specify how much space to leave on each side of the plot.

In this case, we're setting `left`, `right`, `top`, and `bottom` to add some space on all sides of the plot. These values are specified as fractions of the figure width and height, so a value of 0.1 means to leave 10% of the figure width or height as empty space.

``    # Add a title to the plot
    plt.title(title, y=1.08, size=18)


This line uses the `plt.title()` function from the `matplotlib.pyplot` library to add a title to the plot. The first argument is a string containing the text of the title. The function also takes several optional arguments that allow you to customize the appearance and position of the title.

In this case, we're setting two optional arguments: `y` and `size`. The `y` argument specifies how far above or below its default position to place the title. In this case, we're setting it to 1.08 which means that the title will be placed slightly above its default position.

The `size` argument specifies what font size to use for the title text. In this case, we're setting it to 18 which means that the title text will be displayed in a font size of 18 points.

``    # Add a legend to the plot using the given full_labels and colors from pie chart
    plt.legend(wedges, full_labels, title="Elements", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))


This line uses the `plt.legend()` function from the `matplotlib.pyplot` library to add a legend to the plot. The first argument is an iterable containing artists whose labels we want to include in the legend (in this case, all wedges of pie chart). The second argument is an iterable containing strings specifying what label text to use for each artist (in this case, all full labels).

The function also takes several optional arguments that allow you to customize various aspects of legend's appearance and position.

In this case, we're setting four optional arguments: `title`, `loc`, and `bbox_to_anchor`. The `title` argument specifies what text to use for legend's title (in this case `"Elements"`). The `loc` argument specifies where on axes legend should be placed (in this case `"upper right"`). The `bbox_to_anchor` argument specifies where on figure legend should be placed (in this case `(1, 0, 0.5, 1)`).

``    # Replace spaces in title with underscores to create filename for saving figure
    filename = title.replace(" ", "_")


This line uses string method `.replace()` on variable `title` with arguments `" "` and `"_"`. This replaces all spaces in string with underscores and assigns resulting string to variable named `filename`.

``    # Save figure (dpi 300 is good when saving so graph has high resolution)
    filepath = currfile_dir / (f"{filename}.png")
    plt.savefig(filepath, dpi=600)


These lines use Path object method `/` on variable `currfile_dir` with argument `(f"{filename}.png")`. This creates new Path object representing file path with filename equal to value of variable named `filename`. This file path is assigned to variable named `filepath`.

Then it uses function `.savefig()` from matplotlib.pyplot library with arguments `filepath` and keyword argument pair `(dpi=600)`. This saves current figure as image file at location specified by file path with resolution specified by dpi value.

``    # Show plot
    plt


.. literalinclude:: files/pie_chart.py
    :linenos:
