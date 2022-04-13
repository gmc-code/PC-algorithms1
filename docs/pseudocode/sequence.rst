==========================
Sequence
==========================

| A sequence is a control structure that consists of a set of instructions like a recipe.
| Every line of code in the sequence is run in the order that it is written.

| The code below prompts the suer to enter their name then prints a greeting.

.. code-block:: python

   name = input("Enter your name?")
   print("Hello, " + name + ". Nice to meet you.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

   BEGIN
      name <- INPUT ("Enter your name?")
      PRINT "Hello, " + name + ". Nice to meet you."
   END

----

.. admonition:: Tasks

   #. Write pseudocode for ``num = 2``.
   #. Write pseudocode for ``print(a * 2)``.
   #. Write pseudocode for this python sequence:

      .. code-block:: python

         a = 5
         b = 6
         print(a * b)

   #. Write python for this pseudocode sequence:

      .. code-block:: 
            
         BEGIN
            INPUT a number between 1 and 10
            Multiply by 3 
            Add 18
            Multiply by 3
            OUTPUT all the digits but 1
         END
