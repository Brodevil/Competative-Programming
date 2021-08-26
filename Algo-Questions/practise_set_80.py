# Algorithms Question 80 =  Extra Long Factorials (From HackerRank)

"""
Extra Long Factorials | Problem Statement :


Get the Problem Statment on HackerRank : https://www.hackerrank.com/challenges/extra-long-factorials/problem

And get the Solution in python By Brodevil, here :|

"""

# Author = Abhinav
# Date = 25 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/extra-long-factorials/problem)

# Solution :

# Complete the 'extraLongFactorials' function below.
# The function accepts INTEGER n as parameter.


def extraLongFactorials(n: int) -> int:
    if n == 1:
        return 1
    else:
        return extraLongFactorials(n-1)*n

if __name__ == '__main__':
    n = int(input().strip())
    result = extraLongFactorials(n)
    print(result)
