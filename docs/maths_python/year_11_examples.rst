=======================
year_11_examples
=======================

Grades
------------------------------

| The code below uses selection to return a grade from a percentage score.

.. code-block:: python

    score = float(input("Enter the percentage score: "))
    if score >=93:
        print("A+")
    elif score >=85:
        print("A")
    elif score >=80:
        print("B+")
    elif score >=75:
        print("B")
    elif score >=68:
        print("C+")
    elif score >=60:
        print("C")
    elif score >=55:
        print("D+")
    elif score >=50:
        print("D")
    elif score >=40:
        print("NP")
    else: 
        print("UG")


| Pseudocode:

input score
if score >=93 then
    print "A+"
elif score >=85 then
    print "A"
elif score >=80 then
    print "B+"
elif score >=75 then
    print "B"
elif score >=68 then
    print "C+"
elif score >=60 then
    print "C"
elif score >=55 then
    print "D+"
elif score >=50 then
    print "D"
elif score >=40 then
    print "NP"
else: 
    print "UG"

----


