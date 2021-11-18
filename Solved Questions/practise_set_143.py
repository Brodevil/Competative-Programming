# Competitive Programming Question 143  =  B. Odd Grasshopper (From CodeForces)

"""
B. Odd Grasshopper |


Get the problem Statement on CodeForces : https://codeforces.com/problemset/problem/1607/B

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 17 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1607/B)

# Solution :

for _ in range(int(input())):
    x, n = map(int, input().split())
    for _ in range(1, n+1):
        if x % 2 == 0:
            x -= _
        else:
            x += _
    
    print(x)
