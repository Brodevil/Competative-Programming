# Copetative Programming Question 145  = B. Divan and a New Project  (From CodeForces)

"""
B. Divan and a New Project |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1614/B

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 12 December 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1614/B)

# Solution :


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = [0] * (n + 1)
    s = 0
    b = sorted([[a[i], i] for i in range(len(a))], reverse=True)
    pos = 1
    
    for k, i in b:
        res[i + 1] = pos
        s += 2 * k * abs(pos)
        if pos > 0:
            pos = -pos
        else:
            pos = -pos + 1
    
    print(s)
    print(*res)
