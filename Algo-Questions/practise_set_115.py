# Algorithm Question 115  =  A. Simply Strange Sort (From CodeForces)

"""
A. Simply Strange Sort |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1561/A

And get the solved solution in python, here :}

"""

# Author = Abhinav
# Date = 4 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1561/A)

# Solution :

f = sorted
for s in [*open(0)][2::2]:
    *a, = map(int, s.split())
    i = c = 0
    while a > f(a):
        j = i
        while j < len(a)-1:
            a[j:j+2] = f(a[j:j+2])
            j += 2
        c += 1
        i ^= 1
    print(c)
