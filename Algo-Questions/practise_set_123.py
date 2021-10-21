# Algorithm Question 123  =  A. Windblume Ode (From CodeForces)

"""
A. Windblume Ode |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1583/A

And get the solved solution in python, here :}

"""

# Author = Abhinav
# Date = 19 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1583/A)

# Solution :

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    d = sum(a)
    condition = True
    
    for i in range(2, round(d ** 0.5) + 1):
        if d % i == 0:
            condition = False
            break
    if not condition:
        print(n)
        print(*[i + 1 for i in range(n)])
    else:
        for i in range(n):
            if a[i] % 2 == 1:
                print(n - 1)
                print(*[j + 1 for j in range(n) if i != j])
                break
