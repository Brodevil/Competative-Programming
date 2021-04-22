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


You have to write a function isCorrect(table, number) and return  teh index where rohan's function is wrong 
and print it to screen! if the table is correct, Your funtion returns None.


"""
import random

def rohanMultiplications(number):
    wrong_place = random.randint(2, 9)
    table = list()
    for i in range(1, 11):
        if i== wrong_place:
            table.append(i*number+random.randint(1, 8))
        else:
            table.append(i*number)
    return table

def abhinavChecker(table, number):
    correctTable = [i*number for i in range(1, 11)]
    return correctTable == table


if __name__ == "__main__":
    rohans_table = rohanMultiplications(5)
    print(abhinavChecker(rohans_table, 5))