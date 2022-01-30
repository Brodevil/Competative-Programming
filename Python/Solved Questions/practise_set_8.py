# Python Practise problem 8 (10 points) - Rohan Das is a Fraud

"""
Rohan Das is a Fraudby nature

Rohan Das wrote a python frunction to print a multiplication table of given number 
and put one of the values (randomly generated) as wrong.
Rohan Das did this to fool his classmates and make them commit a mistake in a test.
You cannot tolerate this! 

So you decided to use your python skills to counter Rohan's actions by writing 
a python program that validates Rohan's table

Your function should be able to find out the wrong values in Rohan's table and expose Rohan Das as a 
fraud.

Note : Rohans' Function return a list of number like this:


Rohan Das's Function Input:
rohanMultiplication(6)

Rohan Das's Function return this Output:
[6, 12, 18, 26......, 60]


You have to write a function isCorrect(table, number) and return the index where rohan's function is wrong 
and print it to screen! if the table is correct, Your funtion returns None.


"""

# Author = Abhinav
# Date = 22 April 2021
# Pourpose = Just for the python practise here to become expert and get sucess by accheving my AIM


import random


def rohanMultiplications(number):
    """Rohan's cheat function is this"""
    wrong_place = random.randint(2, 9)
    table = list()
    chooise = random.randint(
        0, 1
    )  # this is randomly getting that we rohan will change the table or not
    if chooise == 0:
        for i in range(1, 11):
            if i == wrong_place:
                table.append(i * number + random.randint(1, 8))
            else:
                table.append(i * number)
        return table
    else:
        return [i * number for i in range(1, 11)]


def abhinavChecker(table, number):
    """Abhinav's Checker function for the rohan's functions"""
    correctTable = [i * number for i in range(1, 11)]
    wrongIndex = (
        list()
    )  # I did this because if we want then we can make more then one mistake okay otherwise You can jsut return this value directly
    for index, table in enumerate(zip(correctTable, table)):
        if table[0] == table[1]:
            pass
        else:
            wrongIndex.append(index + 1)
    if len(wrongIndex) == 0:
        return None
    else:
        return wrongIndex


if __name__ == "__main__":
    try:
        tableNum = int(
            input(
                "Enter the number of which table you want from the Rohan's Functions :\t"
            )
        )
    except ValueError:
        print(
            "\nEnter a league input that will a number so that we will find its table by Rohans functions and check through Abhinav's Checker functions \n"
        )
        exit()
    # got the responce from the rohan's functions it might be wrong or write
    rohans_table = rohanMultiplications(tableNum)
    print("\nNow This is the Rohan's Functions Answer \n")

    # print in the readable form for best UI
    for index, value in enumerate(rohans_table):
        print(f"{tableNum} X {index+1} = {value}")

    print("\nWait!, Now checking the table from the Abhinav's checker function \n")

    checkerTable = abhinavChecker(rohans_table, tableNum)
    if checkerTable == None:
        print(f"Everyting was right\n")
    else:
        for i in checkerTable:
            print(
                f"{tableNum} X {i} = {tableNum*i} \t Rohan For Cheating you guys! Abhinav ne baccha liya tumhe shuker manao bhai\n"
            )
