# Algorithm Question 133  =  A. Array Elimination  (Form CodeFroces)

"""
A. Array Elimination |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1601/A

And get the solution, solved by me, here :}

"""

# Author = Abhinav
# Date = 30 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1601/A)

# Solution :

from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [bin(int(x))[::-1] for x in input().split()]

    l = [0] * 33
    for num in a:
        for i, char in enumerate(num):
            l[i] += char == "1"

    ans = []
    for i in range(1, n + 1):
        if all(x % i == 0 for x in l):
            ans.append(i)
    print(*ans)
