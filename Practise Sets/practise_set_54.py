# Python Practise 54 = Between Two Sets (From hackerrank)

"""
Between Two Sets | Problem Statement 


Get the Problem statement here : https://www.hackerrank.com/challenges/between-two-sets/problem
And the Solution here |

"""

# Author = Abhinav
# Date = 28 July 2021
# Pourpose = Now I am getting very less time to touch my laptop, so in few time lets Practise some new thing in Python
# Source = https://www.hackerrank.com/challenges/between-two-sets/problem

# Solution :


#!/bin/python3

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b


def getTotalX(a, b):
    # Write your code here
    return 0


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
