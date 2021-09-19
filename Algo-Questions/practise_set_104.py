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


if __name__ == "__main__":
    int(input())
    arr = list(map(int, input().split()))
    minimum = 0

    for _ in range(len(arr)):
        if arr.count(arr[_]) > 1:
            ar = arr.copy()
            ar.pop(_)
            gap = (ar.index(arr[_])-1) - _

            if gap > minimum:
                minimum = gap
    
    if minimum != 0:
        print(minimum)
    else:
        print(-1)
