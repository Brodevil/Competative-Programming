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
    s, n = map(int, input().split())
    for i in range((n - 1) // 4 * 4 + 1, n + 1):
        s += i if s % 2 else -i
    print(s)
