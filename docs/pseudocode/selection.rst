==========================
Selection
==========================

| Selection is one of the three basic control structures:
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
   while True:
      if score >= cut_off_score:
         print("Suitable standard.")
      else:
         print("Do a retest.")

| The equivalent pseudocode is:

.. code-block::

   BEGIN
      score <- 65
      cut_off_score <- 60
      WHILE TRUE
      IF score >= cut_off_score THEN
         OUTPUT "Suitable standard."
      ELSE
         OUTPUT "Do a retest."
      ENDIF
      ENDWHILE
   END

----

If, elif, else
----------------------------

| ``if`` is used with a condition that results in ``True`` or ``False``.
| When the condition is True, the code indented below the ``if`` statement is executed.
| Alternatives can be provided using ``elif`` with a condition.
| If all conditions are ``False``, ``else:`` can be used to execute other code.
| Note that there must be a colon, ``:``, at the end of each ``if``, ``elif`` and ``else`` statement.

.. code-block:: python

   scoreA = 88
   scoreB = 85
   while True:
      if scoreA > scoreB:
         print("A won")
      elif scoreB > scoreA:
         print("B won")
      else:
         print("A drew with B")

| The equivalent pseudocode is:

.. code-block::

   BEGIN
      scoreA <- 88
      scoreB <- 85
      WHILE TRUE
         IF scoreA > scoreB THEN
            OUTPUT "A won"
         ELSEIF scoreB > scoreA THEN
            OUTPUT "B won"
         ELSE
            OUTPUT "A drew with B"
         ENDIF
      ENDWHILE
   END


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

   #. Write python code for the following pseudocode on preparing for the weather.

      .. code-block::

         BEGIN
            is_raining <- False
            is_cold <- False
            OUTPUT "Good Morning."
            IF is_raining and is_cold THEN
               OUTPUT "Bring Umbrella and jacket."
            ELSEIF is_raining and not(is_cold) THEN
               OUTPUT "Bring Umbrella."
            ELSEIF not(is_raining) and is_cold THEN
               OUTPUT "Bring Jacket."
            ELSE
               OUTPUT "Wear a sun hat."
            ENDIF
         END



    #. Add the variables ``teamA`` and ``teamB`` and assign team names for them. Modify the code to scroll the team name instead of 'A' or 'B'. Write both the python code and pseudocode.

----

Nested if 
----------------------------

| Nesting is the inclusion of other ``if`` statements have within ``if`` statements.
| Both the ``if`` and the ``elif`` have a nested ``if`` and ``else`` that are used when their condition is true. 

.. code-block:: python


    scoreA = 120
    scoreB = 55
    while True:
        if scoreA > scoreB:
            if scoreA - scoreB > 60:
                display.scroll("A won easily")
            else:
                display.scroll("A won")
        elif scoreB > scoreA:
            if scoreB - scoreA > 60:
                display.scroll("B won easily")
            else:
                display.scroll("B won")
        else:
            display.scroll("A drew with B")


----

.. admonition:: Tasks

    #. Add the variables ``teamA`` and ``teamB`` and set team names for them. Modify the code to scroll the team name instead of 'A' or 'B'. Hint: To join text use a plus symbol. e.g (myteam + " my text")
    #. Modify the code to scroll the winning margins. Use ``str(number)`` to convert numbers to text for joining with other text. Add the variables ``teamAwinby`` and ``teamBwinby``. Calculate those variables using the scoreA and scoreB. e.g ``teamAwinby = scoreA - scoreB``. Replace "A won easily" with code to output "A won easily by 65". Do similar replacements for the other scrolling text.


----

.. admonition:: Tasks

    #. Write pseudocode for ``num = 2``.
    #. Write pseudocode for ``print(a * 2)``.
    #. Write pseudocode for:

    .. code-block:: python
    
        a = 5
        b = 6
        print(a * b)

    #. Write python for this pseudocode::
    
      BEGIN
         INPUT a number between 1 and 10
         Multiply by 3 
         Add 18
         Multiply by 3
         OUTPUT all the digits but 1
      END


