# Algorithm Question 122 = A. Elections (From CodeForces)

"""
A. Elections |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1593/A

And get the solved solution in python, here :}

"""

# Author = Abhinav
# Date = 18 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1593/A)

# Solution :

for _ in range(int(input())):
    i = list(map(int, input().split()))
    h = max(i)
    for _ in i:
        print(0, end=" ") if h == _ and i.count(h) == 1 else print(h-_+1, end=" ")
    print()
