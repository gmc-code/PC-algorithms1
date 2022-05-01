==========================
Selection
==========================

| Selection is one of the three basic control structures.
| Selection provides alternatives or branching using ``if`` ... ``elif`` ... ``else``)

----


If, else
----------------------------

| ``if`` is used with a condition that results in ``True`` or ``False``.
| When the condition is True, the code indented below the ``if`` statement is executed.
| If all conditions are ``False``, ``else:`` can be used to execute other code.

.. code-block:: python

   score = 65
   cut_off_score = 60
   if score >= cut_off_score:
      print("Suitable standard.")
   else:
      print("Do a retest.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

   BEGIN
      score <- 65
      cut_off_score <- 60
      IF score >= cut_off_score THEN
         OUTPUT "Suitable standard."
      ELSE
         OUTPUT "Do a retest."
      ENDIF
   END

----
.. admonition:: Tasks

   #. In the code above, is the condition in the if statement True or False?
   #. Give a value for ``score`` in the code above such that the output is ``"Do a retest."``.
   #. Assuming scores can only be integers from and including 0 to 100, how many different scores would result in the output of ``"Do a retest."``?
   #. Assuming scores can only be integers from and including 0 to 100, how many different scores would result in the output of ``"Suitable standard."``?

----

If, elif, else
----------------------------

| Alternatives can be provided using ``elif`` with a condition.
| Note that there must be a colon, ``:``, at the end of each ``if``, ``elif`` and ``else`` statement.

.. code-block:: python

   scoreA = 88
   scoreB = 85
   if scoreA > scoreB:
      print("A won.")
   elif scoreB > scoreA:
      print("B won.")
   else:
      print("A drew with B.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

   BEGIN
      scoreA <- 88
      scoreB <- 85
      IF scoreA > scoreB THEN
         OUTPUT "A won."
      ELSEIF scoreB > scoreA THEN
         OUTPUT "B won."
      ELSE
         OUTPUT "A drew with B."
      ENDIF
   END

----

.. admonition:: Tasks

   #. In the code above, is the condition in the if statement True or False?
   #. GIve a value for ``scoreB`` in the code above such that the output is ``"B won."``.
   #. Give a value for ``scoreB`` in the code above such that the output is ``"A drew with B."``.

----

.. admonition:: Tasks

   #. Write python code for the following pseudocode for travelling to school.

      .. code-block::

         BEGIN
            IF it is raining THEN
               OUTPUT "Catch the bus."
            ELSE
               OUTPUT "Ride the bike."
            ENDIF
         END

----

And, or, not
----------------------------

| The ``and`` keyword is a logical operator used to combine conditional statements.
| The return value will be **True** if **all** of the statements are **True**.
| ``if is_raining and is_cold`` returns True if **both** are True.
| If will return **False** if **any** of the statements are **False**.
| ``if is_raining and is_cold`` returns False if **either** are False.

.. code-block:: python

   is_raining = True
   is_cold = True
   print("Good Morning.")
   if is_raining and is_cold:
      print("Bring Umbrella and jacket.")
   else:
      print("Umbrella and jacket are optional.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

   BEGIN
      is_raining <- TRUE
      is_cold <- TRUE
      OUTPUT "Good Morning."
      IF is_raining AND is_cold THEN
         OUTPUT "Bring Umbrella and jacket."
      ELSE
         OUTPUT "Umbrella and jacket are optional."
      ENDIF
   END

----

.. admonition:: Tasks

   #. In the code above, is the condition in the if statement True or False?
   #. What is the expected output from the code above?
   #. Would changing ``is_raining`` to ``False`` result in a change in the output?
   #. Would changing ``is_raining`` to ``False`` and ``is_cold`` to ``False`` result in a change from the original output?

----

| The ``or`` keyword is a logical operator used to combine conditional statements.
| The return value will be **True** if **one** is **True**.
| ``if is_raining or is_cold`` returns True if **either** is True.
| If will return **False** if **all** of the statements are **False**.
| ``if is_raining or is_cold`` returns False if **both** are False.

.. code-block:: python

   is_raining = False
   is_cold = False
   print("Good Morning.")
   if is_raining or is_cold:
      print("Bring Umbrella or jacket or both.")
   else:
      print("Wear a sun hat.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

   BEGIN
      is_raining <- FALSE
      is_cold <- FALSE
      OUTPUT "Good Morning."
      IF is_raining OR is_cold THEN
         OUTPUT "Bring Umbrella or jacket or both."
      ELSE
         OUTPUT "Wear a sun hat."
      ENDIF
   END

----

.. admonition:: Tasks

   #. In the code above, is the condition in the if statement True or False?
   #. What is the expected output from the code above?
   #. Would changing ``is_raining`` to ``True`` result in a change in the output?
   #. Would changing ``is_raining`` to ``True`` and ``is_cold`` to ``True`` result in a change from the original output?

----

| The ``not`` keyword is a logical operator.
| It changes True to False, and False to True.

.. code-block:: python

   is_raining = True
   is_cold = False
   print("Good Morning.")
   if is_raining and is_cold:
      print("Bring Umbrella and jacket.")
   elif is_raining and not(is_cold):
      print("Bring Umbrella.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

   BEGIN
      is_raining <- TRUE
      is_cold <- FALSE
      OUTPUT "Good Morning."
      IF is_raining AND is_cold THEN
         OUTPUT "Bring Umbrella AND jacket."
      ELSEIF is_raining AND NOT (is_cold) THEN
         OUTPUT "Bring Umbrella."
      ENDIF
   END

----

.. admonition:: Tasks

   #. In the code above, is the condition in the if statement True or False?
   #. What is the expected output from the code above?
   #. What change would be needed in the variable assignments to result in the output being ``"Bring Umbrella AND jacket."``?

----

.. admonition:: Tasks

   #. Write python code for the following pseudocode on preparing for the weather.

      .. code-block::

         BEGIN
            is_raining <- False
            is_cold <- False
            OUTPUT "Good Morning."
            IF is_raining AND is_cold THEN
               OUTPUT "Bring Umbrella and jacket."
            ELSEIF is_raining AND NOT(is_cold) THEN
               OUTPUT "Bring Umbrella."
            ELSEIF NOT(is_raining) AND is_cold THEN
               OUTPUT "Bring Jacket."
            ELSE
               OUTPUT "Wear a sun hat."
            ENDIF
         END


----

Nested if
----------------------------

| Nesting is the inclusion of other ``if`` statements within ``if`` statements.
| Both the ``if`` and the ``elif`` below have a nested ``if`` and ``else`` that are used when their condition is true. 

.. code-block:: python

   scoreA = 120
   scoreB = 55
   if scoreA > scoreB:
      if scoreA - scoreB > 60:
         print("A won easily.")
      else:
         print("A won.")
   elif scoreB > scoreA:
      if scoreB - scoreA > 60:
         print("B won easily.")
      else:
         print("B won.")
   else:
      print("A drew with B.")


| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

   BEGIN
      scoreA <- 120
      scoreB <- 55
      IF scoreA > scoreB THEN
         IF scoreA - scoreB > 60 THEN
               OUTPUT "A won easily."
         ELSE
               OUTPUT "A won."
         ENDIF
      ELSEIF scoreB > scoreA THEN
         IF scoreB - scoreA > 60 THEN
               OUTPUT "B won easily."
         ELSE
               OUTPUT "B won."
         ENDIF
      ELSE
         OUTPUT "A drew with B."
      ENDIF
   END

----

.. admonition:: Tasks

   #. Using python code, add the variables ``teamA`` and ``teamB`` and set team names for them. Modify the code to scroll the team name instead of 'A' or 'B'. Hint: To join text use a plus symbol. e.g (myteam + " my text")
   #. Using pseudocode, modify the code to scroll the winning margins. Use ``str(number)`` to convert numbers to text for joining with other text. e.g "A won easily by 65".





