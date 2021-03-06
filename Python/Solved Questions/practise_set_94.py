# Algorithm Question 94  =  B. MEXor Mixup (From CodeFoces)

"""
B. MEXor Mixup | 


Get the Problem Statement on CodeFroces : https://codeforces.com/problemset/problem/1567/B

And get the solved solution in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 8 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1567/B)

# Solution :

for s in [*open(0)][1:]:
    a, b = map(int, s.split())
    x = (0, a - 1, 1, a)[a % 4]
    print(a + (b != x) + (b ^ x == a))
