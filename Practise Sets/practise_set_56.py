# Python Practise 56 = Subarray Division (From hackerrank)

"""
Subarray Division | Problem Statment :


Ger the Problem statemnet here : https://www.hackerrank.com/challenges/the-birthday-bar/problem
And the solution here : |

"""

# Author = Abhinav
# Date = 30 July 2021
# Pourpose = Just for practise and imporving skills
# Source =  https://www.hackerrank.com/challenges/the-birthday-bar/problem

# Solution :

#!/bin/python3

# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m


def birthday(s: list, d: int, m: int):
    # Write your code here
    return sum([1 for _ in range(len(s)) if sum(s[_:_+m]) == d])


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)
