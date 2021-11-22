# Algorithm Question 111 =  A. Casimir's String Solitaire (From CodeForces)

"""
A. Casimir's String Solitaire |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1579/A

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 29 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1579/A)

# Solution :

for s in[*open(0)][1:]:
    print('YNEOS'[2*s.count('B')!=len(s)-1::2])
