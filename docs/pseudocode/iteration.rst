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
| The last line in the pseudocode for a for loop can take two forms: ``ENDFOR`` or ``NEXT variable``.

.. code-block:: python

    for i in range(4):
        print(i)

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

    BEGIN
        FOR i ← 0 TO 3
            OUTPUT i
        NEXT i
    END

----

.. admonition:: Tasks

    1. How many times does the loop run?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                | How many times does the loop run?
                | The code runs 4 times, with i being assigned the values 0, 1, 2, 3 in order.

----

.. code-block:: python

    for i in range(4, 9):
        print(i)

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::
 
    BEGIN
        FOR i ← 4 TO 8
            OUTPUT i
        NEXT i
    END


----

While loops: forever
----------------------

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

While loops: pre-test
----------------------

| While loops test a condition and only run the indented code in the while block while that condition is True.
| If the condition is False, the code in the while block doesn't run.
| The condition is tested **before** the rest of the while loop is run.

| The general pattern is:

.. code-block::

    # pre-test loop
    while <conditional>:
        <statements>

| Example python code:

.. code-block:: python

    num = 1
    while num < 10:
        print(num)
        num = num + 1

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

    BEGIN
        num ← 1
        WHILE num < 10
            OUTPUT num
            num ← num + 1
        ENDWHILE
    END

----

Pseudocode: post-test REPEAT UNTIL
--------------------------------------

| The condition is tested **after** the rest of the while loop is run and so controls the exiting of the loop.
| This guarantees that the while block is run at least once.
| When the test condition is **True**, the loop is exited.

| Example pseudocode:

.. code-block::

    BEGIN
        num ← 1
        REPEAT
            OUTPUT num
            num ← num + 2
        UNTIL num > 9
    END

| There is no direct post-test syntax in python. A ``while True`` loop is run with a break if the condition is met.
| The general pattern is:

.. code-block::

    # post-test loop
    while True:
        <statements>
        if <conditional>:
            break

| The equivalent python code is:

.. code-block:: python

    num = 1
    while True:
        print(num)
        num += 2
        if num > 9:
            break

----

Pseudocode: post-test DO WHILE
-----------------------------------

| The condition is tested **after** the rest of the while loop is run and so controls the exiting of the loop.
| This guarantees that the while block is run at least once.
| When the test condition is **False**, the loop is exited.

| Example pseudocode:

.. code-block::

    BEGIN
        num ← 1
        DO
            OUTPUT num
            num ← num + 2
        WHILE num < 10
    END

| There is no direct post-test syntax in python. A ``while True`` loop is run with a break if the condition is met.
| The general pattern is:

.. code-block::

    # post-test loop
    while True:
        <statements>
        if not <conditional>:
            break

| The equivalent python code is:

.. code-block:: python

    num = 1
    while True:
        print(num)
        num += 2
        if not(num > 9):
            break


----

Practice Questions
--------------------

.. admonition:: Tasks

    #. What is the expected output from the code above?
    #. How many times is the loop below executed?

        .. code-block:: 

            BEGIN
                i = 0
                WHILE (i <= 10)
                    print i
                    i = i + 21
                ENDWHILE
            END

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                | What is the expected output from the code above?
                | 1, 3, 5, 7, 9 on separate lines.

            
            .. tab-item:: Q2

                | How many times is the loop below executed?
                | Once.

            