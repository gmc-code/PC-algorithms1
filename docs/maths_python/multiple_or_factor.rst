=======================
Multiple or factor
=======================

| VC2M5N10: level 5:  Follow a mathematical algorithm involving branching and repetition (iteration); create and use algorithms involving a sequence of steps and decisions and digital tools to experiment with factors, multiples and divisibility; identify, interpret and describe emerging patterns

* creating algorithms that use multiplication and division facts to determine if a number is a multiple or factor of another number; for example, using a flow chart that determines whether numbers are factors or multiples of other numbers using branching, such as yes/no decisions

----

Pseudocode
------------------------------------------------

| The pseudocode to determine if one number is a factor or multiple of a second number.

| **function** is_multiple_or_factor(a, b)
|     **if** a = 0 **or** b = 0
|         return "Do not use 0 for a or b"
|     **end if**
|     **if** b % a = 0
|         **return** a + " is a factor of " + b
|     **else if** a % b = 0
|         **return** a + " is a multiple of " + b
|     **else**
|         **return** a + " is neither factor nor multiple of " + b
|     **end if**
| **end function**

----

Multiple or factor code
------------------------------------------------

.. literalinclude:: files/multiple_or_factor.py
    :linenos:

