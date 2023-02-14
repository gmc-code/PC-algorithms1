==========================
Selection
==========================

| Selection is one of the three basic control structures.
| Selection provides alternatives or branching using ``if`` ... ``elif`` ... ``else``.

.. list-table:: Python - Pseudocode equivalents
   :widths: 125 250
   :header-rows: 1

   * - Python
     - Pseudocode
   * - =
     - <-
   * - if
     - IF ....THEN
   * - elif 
     - ELSEIF   ....THEN
   * - else 
     - ELSE
   * - "end of if"
     - ENDIF
   * - or 
     - OR 
   * - and 
     - AND 
   * - not 
     - NOT 
   * - True 
     - TRUE 
   * - False 
     - FALSE



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

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            | In the code above, is the condition in the if statement True or False?
            | ``if score >= cut_off_score`` becomes ``if 65 >= 60:``
            | This evaluates to True

         .. tab-item:: Q2

            | Give a value for ``score`` in the code above such that the output is ``"Do a retest."``.
            | "Do a retest." is in the False branch.
            | So the score is below 60. e.g. 59

         .. tab-item:: Q3

            | Assuming scores can only be integers from and including 0 to 100, how many different scores would result in the output of ``"Do a retest."``?
            | Required scores are from 0 to 59. 
            | There are 60 scores.

         .. tab-item:: Q4

            | Assuming scores can only be integers from and including 0 to 100, how many different scores would result in the output of ``"Suitable standard."``?
            | Required scores are from 60 to 100. 
            | There are 41 scores.

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
   #. Give a value for ``scoreB`` in the code above such that the output is ``"B won."``.
   #. Give a value for ``scoreB`` in the code above such that the output is ``"A drew with B."``.

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            | In the code above, is the condition in the if statement True or False?
            | ``scoreA > scoreB`` is True since 88 > 85.

         .. tab-item:: Q2

            | Give a value for ``scoreB`` in the code above such that the output is ``"B won."``.
            | ``scoreB > scoreA`` so scoreB > 88. e.g. scoreB = 89

         .. tab-item:: Q3

            | Give a value for ``scoreB`` in the code above such that the output is ``"A drew with B."``.
            | ``scoreB == scoreA`` so scoreB = 88. e.g. scoreB = 88

----

.. admonition:: Tasks

   #. Write python code for the following pseudocode for travelling to school.

      .. code-block::

         BEGIN
            is_raining <- TRUE
            IF is_raining THEN
               OUTPUT "Catch the bus."
            ELSE
               OUTPUT "Ride the bike."
            ENDIF
         END

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            .. code-block:: python

               is_raining = True
               if is_raining:
                  print("Catch the bus.")
               else:
                  print("Ride the bike.")

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

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            | In the code above, is the condition in the if statement True or False?
            | ``is_raining AND is_cold`` is True since both ``is_raining``and ``is_cold`` are True.

         .. tab-item:: Q2

            | What is the expected output from the code above?
            | "Bring Umbrella and jacket."

         .. tab-item:: Q3

            | Would changing ``is_raining`` to ``False`` result in a change in the output?
            | Yes, since the condition would evaluate to False instead of True.

         .. tab-item:: Q4
            
            | Would changing ``is_raining`` to ``False`` and ``is_cold`` to ``False`` result in a change from the original output?
            | Yes, the out put would be: "Umbrella and jacket are optional."

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

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            | In the code above, is the condition in the if statement True or False?
            | ``is_raining OR is_cold`` is False since both ``is_raining``and ``is_cold`` are False.

         .. tab-item:: Q2

            | What is the expected output from the code above?
            | "Wear a sun hat."

         .. tab-item:: Q3

            | Would changing ``is_raining`` to ``True`` result in a change in the output?
            | Yes, since the condition would evaluate to True instead of False.

         .. tab-item:: Q4
            
            | Would changing ``is_raining`` to ``True`` and ``is_cold`` to ``True`` result in a change from the original output?
            | Yes, the output would be: "Bring Umbrella or jacket or both."

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

   #. In the code above, is the condition in the ELSEIF statement True or False?
   #. What is the expected output from the code above?
   #. What change would be needed in the variable assignments to result in the output being ``"Bring Umbrella AND jacket."``?

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            | In the code above, is the condition in the ELSEIF statement True or False?
            | ``is_raining AND NOT (is_cold)`` is TRUE since both ``is_raining``and ``NOT (is_cold)`` are True.

         .. tab-item:: Q2

            | What is the expected output from the code above?
            | "Bring Umbrella."

         .. tab-item:: Q3

            | What change would be needed in the variable assignments to result in the output being ``"Bring Umbrella AND jacket."``?
            | Change ``is_cold <- FALSE`` to ``is_cold <- TRUE``.
``

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

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            .. code-block:: python

               is_raining = False
               is_cold = False
               print("Good Morning.")
               if is_raining and is_cold:
                  print("Bring Umbrella and jacket.")
               elif is_raining and not(is_cold):
                  print("Bring Umbrella.")
               elif not(is_raining) and is_cold:
                  print("Bring Jacket.")
               else:
                  print("Wear a sun hat.")

----

Nested if
----------------------------

| Nesting is the inclusion of other ``if`` statements within ``if`` statements.
| Both the ``if`` and the ``elif`` below have a nested ``if`` and ``else`` that are used when their condition is true. 

.. code-block:: python

   scoreA = 38
   scoreB = 35
   if scoreA > scoreB:
      if scoreA - scoreB > 14:
         print("A won easily.")
      else:
         print("A won.")
   elif scoreB > scoreA:
      if scoreB - scoreA > 14:
         print("B won easily.")
      else:
         print("B won.")
   else:
      print("A drew with B.")


| **Pseudocode**. The equivalent pseudocode is:

.. code-block::

   BEGIN
      scoreA <-38
      scoreB <- 35
      IF scoreA > scoreB THEN
         IF scoreA - scoreB > 14 THEN
               OUTPUT "A won easily."
         ELSE
               OUTPUT "A won."
         ENDIF
      ELSEIF scoreB > scoreA THEN
         IF scoreB - scoreA > 14 THEN
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

   #. Using python code, add the variables ``teamA`` and ``teamB`` and make up team names for them. Modify the code to print the team name instead of 'A' or 'B'. Hint: To join text use a plus symbol. e.g (myteam + " my text")
   #. Using pseudocode, modify the code to include the changes in Q1, and to print the winning margins. Use ``str(number)`` to convert numbers to text for joining with other text. e.g "The Chiefs won by 3."

   .. dropdown::
      :icon: codescan
      :color: primary
      :class-container: sd-dropdown-container

      .. tab-set::

         .. tab-item:: Q1

            .. code-block:: python

               teamA = "Chiefs"
               teamB = "Eagles"               
               scoreA = 38
               scoreB = 35

               if scoreA > scoreB:
                  if scoreA - scoreB > 14:
                     print("The " + teamA + " won easily.")
                  else:
                     print("The " + teamA + " won.")
               elif scoreB > scoreA:
                  if scoreB - scoreA > 14:
                     print("The " + teamB + " won easily.")
                  else:
                     print("The " + teamB + " won.")
               else:
                  print("The " + teamA + " drew with the " + teamB + ".")

         .. tab-item:: Q1

            .. code-block::

               BEGIN
                  teamA <- "Chiefs"
                  teamB <- "Eagles" 
                  scoreA <-38
                  scoreB <- 35
                  IF scoreA > scoreB THEN
                     margin = str(scoreA - scoreB)
                     IF scoreA - scoreB > 14 THEN
                        OUTPUT ("The " + teamA + " won easily by " + margin + ".")
                     ELSE
                        OUTPUT ("The " + teamA + " won by " + margin + ".")
                     ENDIF
                  ELSEIF scoreB > scoreA THEN
                     margin = str(scoreB - scoreA)
                     IF scoreB - scoreA > 14 THEN
                        OUTPUT ("The " + teamB + " won easily by " + margin + ".")
                     ELSE
                        OUTPUT ("The " + teamB + " won by " + margin + ".")
                     ENDIF
                  ELSE
                     OUTPUT ("The " + teamA + " drew with the " + teamB + ".")
                  ENDIF
               END
