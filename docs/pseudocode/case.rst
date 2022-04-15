==========================
Case
==========================

| Match-case statements are in python from 3.10. Python refers to this as structural pattern matching.
| In other languages they are known as switch-case statements.
| See: https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
| See: https://www.youtube.com/watch?v=-79HGfWmH_w
| If an exact match is not confirmed, the last case, a wildcard _, if provided, will be used as the matching case.


THe general pattern is:

.. code-block::
    
    match subject:
        case <pattern_1>:
            <action_1>
        case <pattern_2>:
            <action_2>
        case <pattern_3>:
            <action_3>
        case _:
            <action_wildcard>


.. code-block:: python

    age_flag = False
    match age_flag:
        case True:
            print("Entry permitted")
        case False:
            print("No entry until you reach 13 years of age.")


| Several alternatives can be used in a single pattern using teh pipe symbol for or: ``\|``

.. code-block:: python

.. code-block:: python

    grade = "A"
    match grade:
        case  "A+" | "A" | "B+" |  "B" | "C+" | "C":
            print("Acceptable standard.")
        case "D+" | "D" | "NP" | "UG":
            print("Retest required.")




A CASE construct indicates a multiway branch based on conditions that are mutually exclusive. 
Four keywords, CASE, OF, OTHERS, and ENDCASE, and conditions are used to indicate the various alternatives. The general form is:

.. code-block::

   CASE expression OF
      condition 1 : sequence 1
      condition 2 : sequence 2
      ...
      condition n : sequence n
      OTHERS:
      default sequence
   ENDCASE

The OTHERS clause with its default sequence is optional. Conditions are normally numbers or characters

indicating the value of "expression", but they can be English statements or some other notation that specifies the condition under which the given sequence is to be performed. A certain sequence may be associated with more than one condition.
Example
        CASE  Title  OF
                Mr      : Print "Mister"
                Mrs     : Print "Missus"
                Miss    : Print "Miss"
                Ms      : Print "Mizz"
                Dr      : Print "Doctor"
        ENDCASE
Example
        CASE  grade  OF
                A       : points = 4
                B       : points = 3
                C       : points = 2
                D       : points = 1
                F       : points = 0
        ENDCASE



CASE Day OF
    1 : OUTPUT "Monday"
    2 : OUTPUT "Tuesday"
    3 : OUTPUT "Wednesday"
    4 : OUTPUT "Thursday"
    5 : OUTPUT "Friday"
    6 : OUTPUT "Saturday"
    7 : OUTPUT "Sunday"
    OTHERWISE OUTPUT "Day invalid"
ENDCASE


