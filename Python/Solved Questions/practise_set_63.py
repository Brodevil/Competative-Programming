# Python Practise 63 = Counting Valleys (From hackerrank)


"""
Counting Valleys | Problem Statment :


Get the Problem Statment online on hackerrank : https://www.hackerrank.com/challenges/counting-valleys/problem

And get the solved solution in Python3 here :|


"""


# Author = Abhinav
# Date = 6 August 2021
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
    seaLevel = 0
    valley = 0

    for step in path:
        if step == "U":
            seaLevel += 1
        else:
            seaLevel -= 1

        if step == "U" and seaLevel == 0:
            valley += 1

    return valley


if __name__ == "__main__":
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)
