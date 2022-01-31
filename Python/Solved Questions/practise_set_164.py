# Competative Programming Question 164 = A. Min Max Swap (From CodeForces)

"""
A. Min Max Swap |

Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1631/A

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 31 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1631/A)

# Solution :

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_copy, b_copy = a.copy(), b.copy()
    
    for _ in range(n):
        a_max, b_max = max(a_copy), max(b_copy)
        
        