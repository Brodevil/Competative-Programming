# Python Practise 62 = Drawing Book (From hackerrank)

"""
Drawing Book | Problem Statemnet :


Get the Problem Statement online only on Hackerrank : https://www.hackerrank.com/challenges/drawing-book/problem

And get the solved solution in python here :|

"""


# Author = Abhinav
# Date = 5 April 2021
# Pourpose = Just for practise and imporving skills
# Source =  https://www.hackerrank.com/challenges/drawing-book/problem


# Solution :

#!/bin/python3

# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p


def pageCount(n: int, p: int):
    # Write your code here
    return int(min(p/2, n/2-p/2))


if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
