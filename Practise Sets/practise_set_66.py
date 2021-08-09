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
    ans = 18
    for _ in permutations(range(1, 10)):
        if sum(_[0:3]) == 15 and sum(_[3:6]) == 15 and sum(_[0::3]) == 15 and sum(_[1::3]) == 15 and _[0] + _[4] + _[8] == 15 and (_[2] + _[4] + _[6] == 15):
            ans = min(ans, sum(abs(_[i] - s[i]) for i in range(0,9)))

    return ans


if __name__ == '__main__':
    s = list()

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)
