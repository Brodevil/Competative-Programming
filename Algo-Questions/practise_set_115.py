# Algorithm Question 115  =  A. Simply Strange Sort (From CodeForces)

"""
A. Simply Strange Sort |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1561/A

And get the solved solution in python, here :}

"""

# Author = Abhinav
# Date = 4 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1561/A)

# Solution :

for _ in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    iterate = 0
    while a != sorted(a):
        CONDITION = False
        for _ in range(0, n, 2):
            if _ != n-1 and a[_] > a[_+1]:
                a[_], a[_+1] = a[_+1], a[_]
                CONDITION = True
                print(a, _, a[_], CONDITION)
        if CONDITION:
            iterate += 1
        


    print(iterate)
