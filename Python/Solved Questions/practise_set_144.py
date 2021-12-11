# Copetative Programming Question 144  = A. Divan and a Store  (From CodeForces)

"""
A. Divan and a Store |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1614/A

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 12 December 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1614/A)

# Solution :

for _ in range(int(input())):
    n, l, r, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted([_ for _ in arr if _ >= l and _ <= r])
    n = list()

    for _ in arr:
        if not sum(n) + _ > k:
            n.append(_)
    print(len(n))
