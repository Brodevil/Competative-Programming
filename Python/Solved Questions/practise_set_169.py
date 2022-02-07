# Competative Programming Question 169 = A. Div. 7 (From CodeForces)

"""
A. Div. 7 |

Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1633/A

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 7 February 2022
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1633/A)

# Solution :

def diff(i, j):
    n = 0
    for h, a in zip(i, j):
        if h != a:
            n += 1
    return n

for _ in range(int(input())):
    n = int(input())
    s1, s2 = str((n//7+1)*7), str((n//7)*7)
    if diff(str(n), s1) > diff(str(n), s2):
        print(s2)
    else:
        print(s1)
