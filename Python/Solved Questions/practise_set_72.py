# Python Practise 72 = Angry Professor (From hackerrank)

"""
Angry Professor | Problem Statement :


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/angry-professor/problem

And get the solved solution in python By Brodevil here :|

"""

# Author = Abhinav
# Date = 15 August 2021 (Independence day)
# Pourpose = Just for practise and imporving python skills
# Source =  [Hackerrnak](https://www.hackerrank.com/challenges/angry-professor/problem)


# Solution :

#!/bin/python3

# Complete the 'angryProfessor' function below.

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a


def angryProfessor(k: int, a: list) -> str:
    c = sum([1 for _ in a if _ <= 0])

    if c >= k:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)
