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


if __name__ == "__main__":
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    results = 0

    for i in range(n):
        if arr[i] + d in arr and arr[i]+2*d in arr:
            results += 1

    print(results)
