====================================================
Matplotlib pie chart
====================================================

| Matplotlib can be used to draw a pie chart.
| By default, the plotting of the first wedge starts from the x-axis and moves counterclockwise.
| The size of each wedge is determined by comparing the value with all the other values, by using this formula: the value divided by the sum of all values: x/sum(x)
| See: https://www.w3schools.com/python/matplotlib_pie_charts.asp
| See: https://matplotlib.org/stable/gallery/pie_and_polar_charts/index.html

----

.. image:: images/Elements_in_the_Earth's_Crust.png
    :width: 600
    :align: center

----

Python code
-------------

| The python code is below.
| The code is commented to indicate what each part is doing.

.. literalinclude:: files/pie_chart_earth.py
    :linenos:
