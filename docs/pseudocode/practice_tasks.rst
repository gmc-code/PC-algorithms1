==========================
Practice tasks
==========================

| Pseudocode is known as Structured English.
| Pseudocode is a way of writing a program that generalizes it for convertion into a programming language.
| Pseudocode represents the the steps of the program in natural language and mathematical notation.
| Pseudocode describes the logic of the program or algorithm.
| The keywords below are in UPPERCASE, but some users use Titlecase and set font style to **bold**.



----

Club player list based on date of birth
--------------------------------------------

| A cricket club needs to print out a list of all players under 21 for special T20 event. The cut off birth date is **2001-12-31**.
| The **club_player_count** is the number of players in the club.
| The system can access player data using arrays with index, **player_id**, starting at 1.
| The player name is obtained using: **name[player_id]** where player_id is the player id number.
| The player date of birth is obtained using: **date_of_birth[player_id]** where player_id is the player id number.
| Write both the pseudocode and python code that will start at the first record and look through each record,
printing out the name and date of birth of each person who can play in the event.

----

| **Pseudocode**. The pseudocode is:

.. code-block::

    BEGIN
        cutoff_date <- "2001-12-31"
        FOR i <- 1 TO club_player_count
            IF date_of_birth[i] > cutoff_date THEN
                OUTPUT name[i], date_of_birth[i]
            ENDIF
        Next i
    END

----

| Sample player arrays are provided for the python code. Index 0 is empty so that player numbers start at 1.
| ``player_name = ["", "Steve Smithy", "Ricky Pont", "Greg Chaps", "Adam Gill"]``
| ``player_date_of_birth = ["", "2000-05-17", "2001-04-21", "2002-03-12", "2003-06-24"]``

| To compare two dates in python, they need to be date objects.
| See: https://docs.python.org/3/library/datetime.html#datetime-objects

| ``datetime.datetime(2001, 12, 31)`` will make a date object for ``"2001-12-31"``.
| To shorten this import the datetime library using ``from datetime import datetime as dt``.
| This allows ``datetime.datetime(2001, 12, 31)`` to be shortened to ``dt(2001, 12, 31)``.
| See: https://docs.python.org/3/library/datetime.html#datetime.datetime

| To convert a date string to a date object, use ``dt.strptime("2000-05-17", "%Y-%m-%d")``
| See: https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime


.. code-block:: python

    from datetime import datetime as dt


    player_name = ["", "Steve Smithy", "Ricky Pont", "Greg Chaps", "Adam Gill"]
    player_date_of_birth = ["", "2000-05-17", "2001-04-21", "2002-03-12", "2003-06-24"]
    club_player_count = len(player_name) 
    # the actual player count is one less than ``len(player_name)``, but this is needed for the range function.

    cutoff_date = dt(2001, 12, 31)
    for i in range(1, club_player_count):
        player_date = dt.strptime(date_of_birth[i], "%Y-%m-%d")
        if player_date > cutoff_date:
            print(name[i], date_of_birth[i])

----

Complete the pseudocode below for the function countDuplicates.
Test case 1
Input: 10, 10, 12, 13, 13, 13, 14, 15, 15
duplicate_count: 4

function countDuplicates (inputArray)
Begin
    duplicate_count <- 0
    counter <- 1
    array_length <- Len (inputArray)
    While counter < array_length
        If inputArray[counter] = inputArray[counter + 1] then
            duplicate_count <- duplicate_count + 1
        endIf
        counter <- counter + 1
    endwhile
    print duplicate_count
End


------------------------------------------------------------
Before a customer can complete a purchase, there are two important checks that must be
completed. The distance (delivery_distance) that the robot must travel for delivery must be less
than or equal to 2.5 km and the order cannot include any fragile items (fragile <- false). If both of
these conditions are met, the order will be processed as "order valid". If either of these conditions is
not met, then the order will be considered "order invalid".
The following pseudocode is used to check these conditions.

If delivery_distance <= 2.5 and fragile = True
    print("order valid")
Else
    print("order invalid")
EndIf



Name and number
--------------------------------------------

| A government department has been issuing new employees with a sequential employee number for over
70 years.
 The sequential employee numbers are now at just under 100 000 and the department would like to
know who has the smallest number and is still working for the department.
A file has been created of the EmployeeName and the EmployeeNumber sorted on EmployeeName. The plan
is to write a simple program to search this file for the smallest number. The pseudocode has been started.
Fill in the missing lines below to find the employee with the smallest number and to print this employee’s
name and number.



Begin
    LowestEmployeeName <-""
    LowestEmployeeNumber <- 100000
    While Not EndOfFile
        Read EmployeeName, EmployeeNumber
        If EmployeeNumber < LowestEmployeeNumber
            LowestEmployeeName <- EmployeeName
            LowestEmployeeNumber <- EmployeeNumber
        EndIF
    EndWhile
    Print LowestEmployeeName, LowestEmployeeNumber
End

-------------------------------------------------------------------------------


The EasyDel app needs to authenticate credit cards. As part of the authentication, the program implements
the following algorithm to help verify whether a credit card number is correct.
Algorithm
• Read the credit card number into a variable.
• Multiply each of the second, fourth, sixth and eighth digits by 2.
– In each case if the number is greater than 10, subtract 9 from it.
• Add up all the other digits plus the results of the previous step.
• Check the result. If the remainder when the total is divided by 10 is 5, 6 or 7 (found by using the
mod operator) then the card is a fake.
Note: The mod operator only keeps the remainder of the division. For example, 9 mod 2 is 1 because 1 is the
remainder.
Begin
//store each digit as it is entered
//initialise variables
//note that dashes are ignored when characters are read
counter <-  1
Repeat
creditnum[counter] <-  digit
counter <- counter + 1
Until digits fi nished
validcard <- false
creditnumtotal <- 0
For counter <- 1 to len(creditnum) //not all credit cards are 16 digits
If (counter mod 2) = 0 then
//it is one of the every second digit
If (2 * creditnum[counter]) <= 10 then
creditnumtotal <- creditnumtotal + 2 * creditnum[counter]
Else
//subtract the 9 as written in the algorithm
creditnumtotal <- creditnumtotal + (2 * creditnum[counter] – 9)
EndIf
EndIf
EndFor
If creditnumtotal mod 10 < 5 or creditnumtotal mod 10 > 7 then
validcard <-  true
Else
validcard <-  false
print “Warning”
EndIf
End
Use the following credit card number to check the algorithm. 2 marks
4 6 9 4 3 7 0 1
creditnumtotal
validcard

----

Every client at SmallPort Financial has a Portfolio Manager assigned to them. Portfolio Manager
assignments are reviewed every three months to ensure that clients are linked with the best professional to
advise them and manage their investments. The new cloud-based intranet currently does not have a built-in
auto-assign feature, so Jessica has asked Ryan to also develop this feature for SmallPort Financial.
Each Portfolio Manager at SmallPort Financial specialises in one of three areas: cryptocurrencies (CRP),
real estate (RES) or stocks (STK). Portfolio Managers are assigned according to the following criteria:
• CRP investments equal to or over $100 000 are assigned to Rachael, while those under this amount are
assigned to David.
• RES investments equal to or over $1 000 000 are assigned to José, while those under this amount are
assigned to David.
• STK investments equal to or over $60 000 are assigned to Frederick, while those under this amount are
assigned to Christine.
Below is the pseudocode that Ryan has written for the new intranet module to auto-assign Portfolio
Managers to clients.
BEGIN
    Case Category
        CRP: If accBalance >= 100000 Then
                Manager <-  Rachael
            Else
                Manager <-  David
            EndIf
        RES: If accBalance >= 1000000 Then
                Manager <-  José
            Else
                Manager <-  David
            EndIf
        STK: If accBalance <= 60000 Then
                Manager <-  Frederick
            Else
                Manager <-  Christine
            EndIf
    End Case
END






















------------------------------
end

