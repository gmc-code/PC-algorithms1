=======================
Geomteric patterns
=======================


| VCMNA254: Design and implement mathematical algorithms using a simple general purpose programming language

* constructing geometric patterns such as a honeycomb, using dynamic geometry functionality

| The python turtle module can be used to generate patetrns of shapes.

----

Turtle basics
----------------

See: https://pc-python.readthedocs.io/en/latest/turtle/turtle_drawing.html

----

Square patterns
--------------------

| A grid of squares

.. image:: images/squares.png
    :scale: 33 %
    :align: center

| Squares rotated 45 degrees.

.. image:: images/squares_at_45.png
    :scale: 33 %
    :align: center

|  
|  Python code for both examples, where the initial angle can be set to 0 or 45 degrees.

.. literalinclude:: files/square_grid.py
    :linenos:

----

Hexagon patterns
--------------------

| Aligned touching hexagons creating diamond gaps.

.. image:: images/hexagon_diamonds.png
    :scale: 33 %
    :align: center

|  
|  Python code:

.. literalinclude:: files/hexagon_diamonds.py
    :linenos:
  
----

| Staggered hexagons creating a tessalation with no overlap.

.. image:: images/hexagon_tessalation.png
    :scale: 33 %
    :align: center

|  
|  Python code:

.. literalinclude:: files/hexagon_tessalation.py
    :linenos:

----

| Overlapping hexagons. The overlap_factor can be varied from 0.5 for tiangles to 1.0 for hexagons with triangular gaps.

.. grid:: 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::  

        hexagons_overlap_.5
        ^^^

        .. figure:: images/hexagons_overlap_.5.png
            :width: 300
            :alt: hexagons_overlap_.5
            :figclass: align-center

    .. grid-item-card::

        hexagons_overlap_.67
        ^^^

        .. figure:: images/hexagons_overlap_.67.png
            :width: 300
            :alt: hexagons_overlap_.67
            :figclass: align-center

.. grid:: 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::  

        hexagons_overlap_.75
        ^^^

        .. figure:: images/hexagons_overlap_.75.png
            :width: 300
            :alt: hexagons_overlap_.75
            :figclass: align-center

    .. grid-item-card::

        hexagons_overlap_1
        ^^^

        .. figure:: images/hexagons_overlap_1.png
            :width: 300
            :alt: hexagons_overlap_1
            :figclass: align-center

|  
|  Python code:

.. literalinclude:: files/hexagons_overlap.py
   :linenos:


