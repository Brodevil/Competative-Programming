# Python practise 73 = Beautiful Days at the Movies (From HackerRank)

"""
Beautiful Days at the Movies | Problem Statement :


Get the Problem Statment on Hackerrank : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

And get he solved solution in python by brodevil here :|


"""

# Author = Abhinav
# Date = 17 August 2021 
# Pourpose = Just for practise and imporving python skills
# Source =  [Hackerrnak](https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem)


# Solution :

#!/bin/python3

# Complete the 'beautifulDays' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k


def beautifulDays(i: int, j: int, k: int) -> int:
    results = 0
    for _ in range(i, j):
        num = (_ - int(str(_)[::-1]))/k
        if num % 1 == 0 and num >= 0:
            results += 1
    
    return results



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(result)
