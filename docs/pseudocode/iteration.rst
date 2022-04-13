==========================
Iteration
==========================


| Iteration is a control structure that carries out repetition or looping using ``while`` or ``for``.

----

Loops
-------------

There are two types of loops: 
* ``for`` loops, that keep count of the number of times a block of code is executed
* ``while`` loops which perform an action until a specified condition is no longer true. 

----

For loops
-------------

| A ``for`` loop can be used to do an action a specific number of times.
| The range function below, ``range (1,4)``, can be used to assign values of 1, 2, and 3 to i as the for loop runs.

.. code-block:: python

    for i in range (1,4):
        print(i)

Nested For loops
-----------------

.. code-block:: python

    for x in range(0, 5):
        for y in range(0, 5):
            print(x, y)

| The outer loop: ``for x in range(0,5):`` will execute the loop five times
 substituting ``x`` for consecutive values from ``0`` to ``4`` each time. 
| The inner loop: ``for y in range(0,5):`` will run the loop five times
 substituting ``y`` for consecutive values in the range ``0`` to ``4`` each time.


----

While loops
------------------

| One of the most common things you might want to do with a ``while`` loop is to do something forever. 
| ``while True:`` loops repeat forever, or until the program is stopped.

.. code-block:: python

    while True:
        print("can't stop me ")

----

While looops can test a condition and only do an action while that condition is True?

.. code-block:: python

    while (temperature() < 18):
        display.scroll(Image.SAD)
        sleep(1000)

    display.show(Image.HAPPY)

----

Practice Questions
--------------------

.. admonition:: Tasks

    1. Display a different image depending on which side microbit is tilted in.


