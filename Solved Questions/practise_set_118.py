# Algorithm Question 118  =  Weighted Uniform Strings (From HackerRank)

"""
Weighted Uniform Strings |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/weighted-uniform-string/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 11 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/weighted-uniform-string/problem)

# Solution :

#!/bin/python3


# Complete the 'weightedUniformStrings' function below.

# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries


def weightedUniformStrings(s: str, queries: list) -> list:
    a = ord(s[0]) - 96
    result = set()
    s = s + "_"
    for _ in range(1, len(s)):
        result.add(a)
        if s[_] == s[_-1]:   
            a += ord(s[_]) - 96
        else:
            a = ord(s[_]) - 96
    
    return ["Yes" if _ in result else "No" for _ in queries]


if __name__ == '__main__':
    s = input()
    queries_count = int(input())
    queries = list()

    for _ in range(queries_count): queries.append(int(input()))

    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))
