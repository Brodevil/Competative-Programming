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
    a, b, c = map(int, input().split())
    if (a + b == c or a + c == b or b + c == a) or (
        (a == b and c % 2 == 0) or (b == c and a % 2 == 0) or (a == c and b % 2 == 0)
    ):
        print("YES")
    else:
        print("NO")
