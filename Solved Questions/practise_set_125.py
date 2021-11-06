# Algorithm Question 125  =  Strange Counter (From HackerRank)

"""
Strange Counter |


Get the Problem Statment on HackerRank : https://www.hackerrank.com/challenges/strange-code/problem

And get the solved solution in python, here :}

"""

# Author = Abhinav
# Date = 22 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/strange-code/problem)

# Solution :

from math import ceil, log2

if __name__ == '__main__':
    t = int(input())
    n = ceil(log2(1+t / 3))
    print(3 * (2**n - 1) - t + 1)
