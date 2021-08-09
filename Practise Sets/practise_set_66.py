# Python practise 66 = Forming a Magic Square (From hackerrank)

"""
Forming a Magic Square  |  Problem Statment :


Get the Problem Statment on hackerrank : https://www.hackerrank.com/challenges/magic-square-forming/problem

And get the solved solution in python by Brodevil here :|


"""


# Author = Abhinav
# Date = 8 August 2021
# Pourpose = Just for practise and imporving skills
# Source =   https://www.hackerrank.com/challenges/magic-square-forming/problem

# Solution :

#!/bin/python3

from itertools import permutations

# Complete the 'formingMagicSquare' function below.

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.


def formingMagicSquare(s: list) -> int:
    # Write your code here
    for _ in permutations(range(9)):
        pass

    return 0


if __name__ == '__main__':
    s = list()

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)
