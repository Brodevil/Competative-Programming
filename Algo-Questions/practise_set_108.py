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

n, t = map(int, input().split())
arr = list(map(int, input().split()))


for _ in range(t):
    x, y = map(int,input().split())
    for i in range(y-x-1):
        mn = min(arr[x+i], arr[x+i+1])
    print(mn)
