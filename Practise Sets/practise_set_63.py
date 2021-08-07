# Python Practise 63 = Counting Valleys (From hackerrank)


"""
Counting Valleys | Problem Statment :


Get the Problem Statment online on hackerrank : https://www.hackerrank.com/challenges/counting-valleys/problem

And get the solved solution in Python3 here :|


"""


# Author = Abhinav
# Date = 6 April 2021
# Pourpose = Just for practise and imporving skills
# Source =   https://www.hackerrank.com/challenges/counting-valleys/problem


# Solution :

#!/bin/python3

# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path


def countingValleys(steps: int, path: str):
    position = 1
    for _ in path.split():
        if _ == "U":
            position += 1
        elif _ == "D":
            position -= 1
    
    return position


if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)
