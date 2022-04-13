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
| The range function below, ``range (4)``, can be used to assign values of 0, 1, 2, and 3 to i as the for loop runs.

.. code-block:: python

    for i in range(4):
        print(i)

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

    BEGIN
        FOR i <- 0 TO 3
            OUTPUT i
        NEXT
    END

----

.. code-block:: python

    for i in range(4, 9):
        print(i)

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::
 
    BEGIN
        FOR i <- 4 TO 8
            OUTPUT i
        ENDFOR
    END

| The outer loop: ``for x in range(0,5):`` will execute the loop five times
 substituting ``x`` for consecutive values from ``0`` to ``4`` each time. 
| The inner loop: ``for y in range(0,5):`` will run the loop five times
 substituting ``y`` for consecutive values in the range ``0`` to ``4`` each time.


----

While loops
------------------

| ``while`` loops can do something forever.
| ``while True:`` loops repeat forever, or until the program is stopped.

.. code-block:: python

    while True:
        print("Can't stop me.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

    BEGIN
        WHILE TRUE
            OUTPUT "Can't stop me."
        ENDWHILE
    END

----

| While loops test a condition and only run the indented code in the while block while that condition is True.
| The code below prints the numbers 1 to 9.

.. code-block:: python

    num = 1
    while num < 10:
        print(num)
        num = num + 1

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

    BEGIN
        num <- 1
        WHILE num < 10
            OUTPUT num
            num <- num + 1
        ENDWHILE
    END


----

Practice Questions
--------------------

.. admonition:: Tasks

    1. Display a different image depending on which side microbit is tilted in.


