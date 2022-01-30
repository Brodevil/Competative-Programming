# Algorithm Question 119 = Separate the Numbers (From HackerRank)

"""
Separate the Numbers |


Get the Problem Statment on HackerRank : https://www.hackerrank.com/challenges/separate-the-numbers/problem

And get the solved solution in python... here:|

"""

# Author = Abhinav
# Date = 14 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/separate-the-numbers/problem)

# Solution :

best = None

for _ in range(int(input())):
    s = input()
    found = False

    for i in range(len(s) // 2):
        a = s[: i + 1]
        f = n = int(s[: i + 1])

        while len(a) < len(s):
            n += 1
            a += str(n)

        if a == s:
            found = True
            print("YES", f)
            break

    if not found:
        print("NO")
