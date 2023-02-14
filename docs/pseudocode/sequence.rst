==========================
Sequence
==========================

| Sequence is one of the three basic control structures.
| A sequence is a control structure that consists of a set of instructions like a recipe.
| Every line of code in the sequence is run in the order that it is written.
| Pseudocode typically starts with ``BEGIN`` and ends with ``END``.

| The code below prompts the user to enter their name, then prints a greeting.

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

   #. Write pseudocode for this python sequence:

      .. code-block:: python

         a = 5
         b = 6
         print(a * b)

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            Write pseudocode for the python sequence.

            .. code-block::

               a <- 5
               b <- 6
               OUTPUT (a * b)

----

.. admonition:: Tasks

   #. Write python for this pseudocode sequence below.
      Hint: random.sample(string, k) returns a random list of k characters from the string without replacement.

      .. code-block:: 

         BEGIN
            INPUT a number between 1 and 10
            Multiply by 3 
            Add 18
            Multiply by 3
            OUTPUT all the digits but 1
         END

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            Write python for the pseudocode sequence.

            .. code-block:: python

               import random

               n = int(input("Enter a number between 1 and 10: "))
               n = n * 3
               n = n + 18
               n = n * 3
               n = str(n)
               mixed_digits_list = random.sample(n, len(n) - 1)
               digits_str = "".join(mixed_digits_list)
               print(digits_str)




