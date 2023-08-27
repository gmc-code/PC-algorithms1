=======================
Polygon construction
=======================

| VC2M9SP03: level 9: Design, test and refine algorithms involving a sequence of steps and decisions based on geometric constructions and theorems; discuss and evaluate refinements

* developing an algorithm for an animation of a geometric construction, or a visual proof, evaluating the algorithm using test cases

| See: https://mathigon.org/task/geometric-constructions-regular-polygons

----

Equilateral triangle
---------------------

| Here is one (there are others) algorithm to construct an equilateral triangle:

- Input: a line segment AB with length L
- Step 1: Draw a circle C1 with center A and radius L
- Step 2: Draw a circle C2 with center B and radius L
- Step 3: Find the point C where C1 and C2 intersect
- Step 4: Draw a line segment AC
- Step 5: Draw a line segment BC
- Step 6: Triangle ABC is equilateral with side length L


| Here is a diagram which illustrates the equilateral triangle construction.

.. image:: images/equilateral_triangle_construction.png
    :width: 400
    :align: center

| Here is the python to draw the equilateral triangle construction.

.. literalinclude:: files/equilateral_triangle_construction.py
    :linenos:


| This python saves the equilateral triangle construction as a gif file.

.. image:: gifs/construct_equilateral_triangle.gif
    :width: 400
    :align: center

.. literalinclude:: files/equilateral_triangle_construction_as_gif.py
    :linenos:


----

Hexagon construction
---------------------

| Here is an algorithm to construct a regular hexagon:

- Input: a radius for the circle.
- Step 1: Draw a circle with given radius.
- Step 2: From the left side of the circle draw another circle.
- Step 3: Form where these 2 circles intersect, draw another circle.
- Step 4: Repeat in an anitclockwise direction until 6 circles have been drawn over the original circle.
- Step 5: Mark teh intersection points and connect them.


| Here is a diagram which illustrates the hexagon construction.

.. image:: images/hexagon_construction.png
    :width: 400
    :align: center


| This python saves the hexagon construction as a gif file.

.. image:: gifs/hexagon_construction.gif
    :width: 400
    :align: center

.. literalinclude:: files/hexagon_construction_as_gif.py
    :linenos:





