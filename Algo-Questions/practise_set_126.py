# Algorithm Practise 126  =  A. Regular Bracket Sequences (From CodeForces)

"""
A. Regular Bracket Sequences |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1574/A

And get the Solution, solved by me, here :}

"""

# Author = Abhinav
# Date = 23 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1574/A)

# Solution :

for _ in range(int(input())):
    n = int(input())
    for _ in range(n):
        print("("*(n-_)+")"*(n-_)+"()"*_)
