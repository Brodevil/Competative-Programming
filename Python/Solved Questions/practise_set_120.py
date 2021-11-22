# Algorithm Question 120  =  A. Computer Game (From CodeForces)

"""
A. Computer Game |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1598/A

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 17 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1598/A)

# Solution :

for _ in range(int(input())):
    n = int(input())
    x_axis, y_axis = input(), input()
    
    for i, j in zip(x_axis, y_axis):
        if i == '1' and j == '1':
            print("NO")
            break
    else:
        print("YES")
