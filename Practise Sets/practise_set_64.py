# Python Practise 64 = Electronics Shop (From Hackerrank)

"""
Electronics Shop | Problem Statment :


Get the Problem Statment on Hackerrank : https://www.hackerrank.com/challenges/electronics-shop/problem

And Get the solved solution in python here :|

"""


# Author = Abhinav
# Date = 7 April 2021
# Pourpose = Just for practise and imporving skills
# Source =   https://www.hackerrank.com/challenges/electronics-shop/problem

# Solution :

#!/bin/python3

# Complete the getMoneySpent function below.


def getMoneySpent(keyboards: list, drives: list, b: int):
    under_budget = -1

    for board in keyboards:
        if board > b:
            continue
        for _ in drives:
            cost = board + _ 
            if cost <= b and cost > under_budget:
                under_budget = cost

    return under_budget


if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))
    
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    
    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
