# Python Practise 60 = Bill Division  (From hackerrank)

"""
Bill Division | Problem Statment :


 - Get the Problem Statment online on hackerrank : https://www.hackerrank.com/challenges/bon-appetit/problem
 - And Get the solved solution in pyhton here :|


"""


# Author = Abhinav
# Date = 3 August 2021
# Pourpose = Just for practise and imporving skills
# Source =  https://www.hackerrank.com/challenges/bon-appetit/problem


# Solution :



#!/bin/python3

# Complete the 'bonAppetit' function below.

# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b


def bonAppetit(bill: list, k: int, b: int):
    print('Bon Appetit' if (sum(bill) - bill[k]) // 2 == b else bill[k] // 2)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
