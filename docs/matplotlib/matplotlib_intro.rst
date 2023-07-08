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

Some code comments
-----------------------

::

    plt.figure(figsize=(7, 8), dpi=100)
    
| This line of code that creates a new Figure object and returns it.
| A Figure object is the top-level container for all plot elements. It represents the entire window in the user interface, including the plotting area, axes, labels, titles, and legends. A Figure object can contain multiple Axes objects, which are the individual plots within the figure.  
| `figsize=(7, 8)` is a keyword argument that specifies the size of the figure in inches. In this case, it specifies that the figure should be 7 inches wide and 8 inches tall.
| `dpi=100` is a keyword argument that specifies the resolution of the figure in dots per inch. In this case, it specifies that the figure should have a resolution of 100 dots per inch.

::

    plt.plot(x, y, "bo-", label=label)
    
| This line calls the `plot` function from the `pyplot` module to plot a line graph of the data stored in variables named `x` and `y`. 
| `x` and `y` are the first two arguments passed to the plot method. They are arrays of data that specify the x-coordinates and y-coordinates of the data points to plot. In this case, they are variables that contain the x and y values calculated earlier in the code.
| `"bo-"` is the third argument passed to the plot method. It is a format string that specifies how to format the data points. In this case, it specifies that the data points should be plotted as blue circles connected by solid lines. The first character, "b", specifies the color of the data points (blue). The second character, "o", specifies the marker style for the data points (circle). The third character, "-", specifies the line style for connecting the data points (solid).
| `label=label` It specifies the label for this data series in the legend. In this case, it is a variable that contains the label string specified earlier in the code.


