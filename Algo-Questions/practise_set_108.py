# Algorithm Question 108  =  Service Lane (From HackerRank)

"""
Service Lane |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/service-lane/problem

And get the python solution, here :|

"""

# Author = Abhinav
# Date = 23 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/service-lane/problem))

# Solution :


if __name__ == "__main__":
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(t):
        i, j = map(int, input().split())
        print(min(arr[i: j+1]))
