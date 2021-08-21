# Algorithm Question 76 = Circular Array Rotation (From HackerRank)

"""
Circular Array Rotation | Problem Statement :


Get the Problem Statement on Hackerrank : https://www.hackerrank.com/challenges/circular-array-rotation/problem

And get the solved solution in python by Brodevil here :|

"""

# Author = Abhinav
# Date = 21 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrnak](https://www.hackerrank.com/challenges/circular-array-rotation/problem)


# Solution :

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries


def circularArrayRotation(a: list, k: int, queries: list):
    # Write your code here
    return 0


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = list()

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print(result)
