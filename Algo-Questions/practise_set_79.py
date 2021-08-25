# Algorithm Question 79 = Find Digits (From HackerRank)

"""
Find Digits | Problem Statement :


Get the Problem Statement on Hackerank : https://www.hackerrank.com/challenges/find-digits/problem

And get the solved solution in python By Brodevil here :|

"""

# Author = Abhinav
# Date = 24 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/find-digits/problem)

# Solution :

# Complete the 'findDigits' function below.

# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.


def findDigits(n: int) -> int:
    return sum([1 for _ in str(n) if _ != '0' and n % int(_) == 0])



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(result)
