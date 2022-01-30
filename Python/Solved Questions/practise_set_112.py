# Algorithm Question 112  =  A. Countdown  (From CodeForces)

"""
A. Countdown |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1573/A

And get solved solution, here :|

"""

# Author = Abhinav
# Date = 30 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1573/A)

# Solution :

for s in [*open(0)][2::2]:
    print(sum(int(x) + (x > "0") for x in s[:-2]) + int(s[-2]))
