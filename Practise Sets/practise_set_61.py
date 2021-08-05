# Python Practise 61 = Sales by Match (From hackerrank)

"""
Sales by Match | Problem Statment :


Get the Problem Statement online on Hakerrank : https://www.hackerrank.com/challenges/sock-merchant/problem

And get the solved solution in python here : |


"""


# Author = Abhinav
# Date = 4 April 2021
# Pourpose = Just for practise and imporving skills
# Source =  https://www.hackerrank.com/challenges/sock-merchant/problem


# Solution :


#!/bin/python3

# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar


def sockMerchant(n: int, ar: list) -> int:
    paires = 0
    for _ in set(ar):
        count = ar.count(_)
        if count >= 2:
            paires += (count//2)

    return paires


if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
