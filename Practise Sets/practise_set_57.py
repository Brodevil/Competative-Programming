# Python Practise 57 = Divisible Sum Pairs (From hackerrank)

"""
Divisible Sum Pairs | Problem Statement :


Get the Problem Statment on Hackerrank here : https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
And Get the solved solution here :|


"""

# Author = Abhinav
# Date = 31 July 2021
# Pourpose = Just for practise and imporving skills
# Source =  https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# Solution :

#!/bin/python3

# Complete the 'divisibleSumPairs' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar


def divisibleSumPairs(n: int, k: int, ar: list) -> int:   
    return sum([1 for _ in range(len(ar)) for i in ar[_+1:] if (ar[_] + i) % 3 == 0])


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
