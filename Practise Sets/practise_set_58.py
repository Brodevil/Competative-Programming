# Python Practise 58 = Migratory Birds (From hackerrank)

"""
Migratory Birds | Problem Statement :


Get the Problem Statment online on hackerrank : https://www.hackerrank.com/challenges/migratory-birds/problem

And get the Solved solution here :|


"""


# Author = Abhinav
# Date = 1 August 2021
# Pourpose = Just for practise and imporving skills
# Source =  https://www.hackerrank.com/challenges/migratory-birds/problem

# Solution :


#!/bin/python3

# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


def migratoryBirds(arr: list):
    # Write your code here
    arr2 = [[arr.count(_), _] for _ in set(arr)]
    highest = sorted(arr2)[-1][0]
    return sorted([_[1] for _ in arr2 if _[0] == highest])[0]


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
