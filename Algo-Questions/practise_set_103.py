# Algorithm Question 103  =  Beautiful Triplets (From HackerRank)


"""
Beautiful Triplets |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/beautiful-triplets/problem

And get the solved solution in python here :|

"""

# Author = Abhinav
# Date = 17 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/beautiful-triplets/problem)

# Solution :

from itertools import permutations


if __name__ == "__main__":
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    results = list()

    for _ in permutations(arr, 3):
        if _[1] - _[0] == d and _[2] - _[1] == d:
            results.append(_)

    print(len(results))
