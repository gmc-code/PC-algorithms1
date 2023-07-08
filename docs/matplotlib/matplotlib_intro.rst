====================================================
Matplotlib intro
====================================================

| Matplotlib is a python library for creating static, animated, and interactive visualizations in Python.

| For examples see: https://matplotlib.org/stable/gallery/index.html

----

Installation
--------------

Use ``pip install matplotlib`` from the command line in the terminal.

----

Importing Pyplot
------------------

| Most of the Matplotlib features are in the pyplot submodule.
| By convention, it is imported under the plt alias so that the Pyplot package can be referred to as plt.

.. code-block:: python

    import matplotlib.pyplot as plt

----

-----------------------
Some code comments
-----------------------

Figure
-----------

::

    plt.figure(figsize=(7, 8), dpi=100)
    
| This line of code that creates a new Figure object and returns it.
| A Figure object is the top-level container for all plot elements. It represents the entire window in the user interface, including the plotting area, axes, labels, titles, and legends. A Figure object can contain multiple Axes objects, which are the individual plots within the figure.  
| `figsize=(7, 8)` is a keyword argument that specifies the size of the figure in inches. In this case, it specifies that the figure should be 7 inches wide and 8 inches tall.
| `dpi=100` is a keyword argument that specifies the resolution of the figure in dots per inch. In this case, it specifies that the figure should have a resolution of 100 dots per inch.

----

Plot
----------

::

    plt.plot(x, y, "bo-", label=label)
    
| This line calls the `plot` function from the `pyplot` module to plot a line graph of the data stored in variables named `x` and `y`. 
| `x` and `y` are the first two arguments passed to the plot method. They are arrays of data that specify the x-coordinates and y-coordinates of the data points to plot. In this case, they are variables that contain the x and y values calculated earlier in the code.
| `"bo-"` is the third argument passed to the plot method. It is a format string that specifies how to format the data points. In this case, it specifies that the data points should be plotted as blue circles connected by solid lines. The first character, "b", specifies the color of the data points (blue). The second character, "o", specifies the marker style for the data points (circle). The third character, "-", specifies the line style for connecting the data points (solid).
| `label=label` It specifies the label for this data series in the legend. In this case, it is a variable that contains the label string specified earlier in the code.

----

Patch
-----------

::

    # Create a list of Patch objects with the same colors as the bars in the bar chart
    legend_elements = [Patch(facecolor=color, label=label) for color, label in zip(colors, full_labels)]
    # Add a legend to the plot using the given full_labels and colors from the bar chart
    plt.legend(handles=legend_elements, title="Elements", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))


A `Patch` object is a 2D artist in the `matplotlib` library. It represents a shape with a defined face color and edge color, which can be drawn on a plot. Patches are used to create various shapes, such as rectangles, circles, polygons, and more. In the context of creating a custom legend for a bar chart, `Patch` objects are used to create small colored squares that represent each bar in the chart.

When creating a `Patch` object, you can specify various properties such as the face color, edge color, line style, and more. In the code you provided earlier, `Patch` objects were created with a specified `facecolor` and `label`. The `facecolor` argument sets the color of the patch, while the `label` argument sets the text that will be displayed next to the patch in the legend.

Once you have created a list of `Patch` objects, you can pass that list to the `handles` argument of the `plt.legend()` function to create a custom legend for your plot. Each patch in the list will be displayed in the legend along with its corresponding label.

