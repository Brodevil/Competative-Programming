# Python Practise 59 = Day of the Programmer  (From hackerrank)

"""
Day of the Programmer | Problem Statment 


Get the Problem Statment online on hackerrank : https://www.hackerrank.com/challenges/day-of-the-programmer/problem
And Get the solved solution in python here :


"""


# Author = Abhinav
# Date = 2 April 2021
# Pourpose = Just for practise and imporving skills
# Source =  https://www.hackerrank.com/challenges/day-of-the-programmer/problem

# Solution :

#!/bin/python3

# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.


def dayOfProgrammer(year: int):
    if year == 1918:
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' % year
    else:
        return '13.09.%s' % year


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)
