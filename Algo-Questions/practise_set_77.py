# Algorithm Question 77 = Sequence Equation (From HackerRank)

"""
Sequence Equation | Problem Statement :


Get the Problem Statement on Hackerrank : https://www.hackerrank.com/challenges/permutation-equation/problem

And get the solution in python by Brodevil here :|

"""

# Author = Abhinav
# Date = 22 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/permutation-equation/problem)


# Solution :


# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.


def permutationEquation(p: list) -> list:
    return [p.index(p.index(_)+1)+1 for _ in sorted(p)]


if __name__ == '__main__':
    input()
    p = list(map(int, input().rstrip().split()))

    for _ in permutationEquation(p):
        print(_)
