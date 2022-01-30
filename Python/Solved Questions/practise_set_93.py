# Algorithm Question 93  =  A. Domino Disaster (From CodeForces)

"""
A. Domino Disaster |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1567/A

And get the solved solution in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 7 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1567/A)

# Solution :

for _ in range(int(input())):
    n = int(input())
    s = input()
    result = ""

    for _ in s:
        if _ == "U":
            result += "D"
        elif _ == "D":
            result += "U"
        else:
            result += _
    print(result)
