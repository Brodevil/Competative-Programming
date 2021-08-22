# Algorithm Question 77 = Sequence Equation (From HackerRank)

"""
Sequence Equation | Problem Statement :


Get the Problem Statement on Hackerrank : https://www.hackerrank.com/challenges/permutation-equation/problem

And get the solution in python by Brodevil here :|

"""

# Author = Abhinav
# Date = 21 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrnak](https://www.hackerrank.com/challenges/permutation-equation/problem)


# Solution :


# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.


def permutationEquation(p: list) -> list:
    result = list()
    for _ in p:
        print(_)
        result.append(p.index(p.index(_)+1)+1)

    return result


if __name__ == '__main__':
    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    for _ in permutationEquation(p):
        print(_)
