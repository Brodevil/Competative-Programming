# Algorithm Practise 104  =  Minimum Distances (From HackerRank)

"""
Minimum Distances |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/minimum-distances/problem

And get the solved solution in python, here:|

"""

# Author = Abhinav
# Date = 18 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/minimum-distances/problem)

# Solution :


def minimum_distance(n: int, arr: list) -> int:
    for _ in range(1, n):
        for i in range(n - _):
            if arr[i] == arr[i+_]:
                return _
    return -1

if __name__ ==  "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = minimum_distance(n, arr)
    print(result)
