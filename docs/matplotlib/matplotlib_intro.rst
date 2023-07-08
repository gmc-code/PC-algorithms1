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


``legend_elements = [Patch(facecolor=color, label=label) for color, label in zip(colors, full_labels)]
``

This line of code uses a list comprehension to create a list of `Patch` objects, one for each element in the `colors` and `full_labels` lists. The `zip` function is used to iterate over both lists simultaneously, so that each `color` and `label` pair corresponds to the same element in both lists.

For each pair of `color` and `label`, a new `Patch` object is created with the specified `facecolor` and `label`. The `facecolor` argument sets the color of the patch, while the `label` argument sets the text that will be displayed next to the patch in the legend.

``python
plt.legend(handles=legend_elements, title="Elements", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))
``

This line of code calls the `plt.legend()` function to add a legend to the plot. The `handles` argument is set to the list of `Patch` objects created earlier, which means that each patch in the list will be displayed in the legend along with its corresponding label.

The `title` argument sets the title of the legend to "Elements". The `loc` argument sets the location of the legend within the plot to "upper right", which means that it will be placed in the upper right corner of the plot area. The `bbox_to_anchor` argument specifies where within the plot area (in normalized coordinates) to place the legend. In this case, it is set to `(1, 0, 0.5, 1)`, which means that it will be placed halfway between the right edge of the plot area and its center along the x-axis, and at the top edge of the plot area along the y-axis.
