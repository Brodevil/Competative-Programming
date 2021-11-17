# Copetative Programming Question 142  =  A. Linear Keyboard  (From CodeForces)

"""
A. Linear Keyboard |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1607/A

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 12 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1607/A)

# Solution :

for _ in range(int(input())):
    key = input()
    s = input()
    unit = 0
    position = key.index(s[0]) + 1

    for _ in s[1:]:
        x = key.index(_) + 1
        f = abs(x - position)
        # print(_, x, position, f)
        position = x
        unit += f
    
    print(unit)
