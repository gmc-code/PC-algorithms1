==========================
Case
==========================

| Match-case statements are in python from 3.10. 
| Python refers to this as structural pattern matching.
| Match-case statements can be used for what is known as switch-case statements in general use in other languages.
| See: https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
| See: https://www.youtube.com/watch?v=-79HGfWmH_w

----

Match-case
--------------------------

| Multiple cases can be used.
| The simple pattern in python is:

.. code-block::
    
    match subject:
        case <pattern_1>:
            <action_1>
        case <pattern_2>:
            <action_2>

| An example in python is:

.. code-block:: python

    age_flag = False
    match age_flag:
        case True:
            print("Entry permitted")
        case False:
            print("No entry until you reach 13 years of age.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block:: 

    BEGIN
        age_flag <- FALSE
        CASE age_flag:
            TRUE:
                OUTPUT "Entry permitted"
            FALSE:
                OUTPUT "No entry until you reach 13 years of age."
        ENDCASE
    END

----

Alternatives
--------------------------

| Several alternatives can be used in a single pattern using the pipe symbol for or: ``|``.

.. code-block:: python

    grade = "A"
    match grade:
        case  "A+" | "A" | "B+" |  "B" | "C+" | "C":
            print("Acceptable standard.")
        case "D+" | "D" | "NP" | "UG":
            print("Retest required.")

| **Pseudocode**. The equivalent pseudocode is:

.. code-block:: 

    BEGIN
        grade <- "A"
        CASE grade:
            "A+" | "A" | "B+" |  "B" | "C+" | "C":
                OUTPUT "Acceptable standard."
            "D+" | "D" | "NP" | "UG":
                OUTPUT "Retest required."
        ENDCASE
    END


----

Wilcard
--------------------------

| If an exact match is not confirmed, the last case, a wildcard _, if provided, will be used as the matching case.
| However, since an underscore will not work in an f-string, the wildcard can be given another variable name such as ``other``. 

.. code-block:: python

    grade = "A-"
    match grade:
        case  "A+" | "A" | "B+" |  "B" | "C+" | "C":
            print("Acceptable standard.")
        case "D+" | "D" | "NP" | "UG":
            print("Retest required.")
        case other:
            print(f'{other} was entered')

| **Pseudocode**. The equivalent pseudocode is:

.. code-block:: 

    BEGIN
        grade <- "A-"
        CASE grade:
            "A+" | "A" | "B+" |  "B" | "C+" | "C":
                OUTPUT "Acceptable standard."
            "D+" | "D" | "NP" | "UG":
                OUTPUT "Retest required."
            other:
                OUTPUT f'{other} was entered'
        ENDCASE
    END


----

Pseudocode alternatives
--------------------------

| The code for each case can be on hte same line in pseudocde.
| The keywords: OF, OTHERS, can be used.
| The OTHERS clause with its default sequence is optional.
| The general pattern amy be:

.. code-block::

   CASE expression OF
      condition 1 : sequence 1
      condition 2 : sequence 2
      ...
      condition n : sequence n
      OTHERS : default sequence
   ENDCASE


Example:

.. code-block::

    CASE  Title  OF
            Mr   : OUTPUT "Mister"
            Mrs  : OUTPUT "Missus"
            Ms   : OUTPUT "Miss"
            OTHERWISE OUTPUT "Form of address not recognised"
    ENDCASE
