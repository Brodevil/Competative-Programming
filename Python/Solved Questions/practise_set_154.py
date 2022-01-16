# Competative Programming Question 154 = A. Construct a Rectangle (From CodeForces)

"""
A. Construct a Rectangle |

Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1622/A

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 11 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://codeforces.com/problemset/problem/1622/A)

# Solution :

for _ in range(int(input())):
    l = map(int, input().split())
    print("YES" if sum(l)%2 == 0 else "NO")