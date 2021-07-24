# Python Practise 52 = 3D Surface Area (From hackerrank) 


"""
3D Surface Area | Problem Statement :


Problem statement : https://www.hackerrank.com/challenges/3d-surface-area/problem

"""

# Author = Abhinav
# Date = 22 July 2021
# Pourpose = Now I am getting very less time to touch my laptop, so in few time lets Practise some new thing in Python
# Source = https://www.hackerrank.com/challenges/3d-surface-area/problem

# Solution :

#!/bin/python3

# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.



def surfaceArea(A):
    # Write your code here
    return 0


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(result)

# Little bit hard question but will solve it soon