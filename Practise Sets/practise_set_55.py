# Python Practise 54 = Breaking the Records (From hackerrank)

"""
Breaking the Records | Problem Statement :


Get the Problem statment here : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
And the soluction here :|

"""

# Author = Abhinav
# Date = 29 July 2021
# Pourpose = Now I am getting very less time to touch my laptop, so in few time lets Practise some new thing in Python
# Source =  https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# Solution :

#!/bin/python3

# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.


def breakingRecords(scores: list):
    # Write your code here
    lowest = list()
    highest = list()

    for _ in range(len(scores)):
        if _ == 0:
            lowest.append(scores[_])
            highest.append(scores[_])
        else:
            if scores[_] < lowest[-1]:
                lowest.append(scores[_])
            elif scores[_] > highest[-1]:
                highest.append(scores[_])
            
    return [len(highest)-1, len(lowest)-1, ]


if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
