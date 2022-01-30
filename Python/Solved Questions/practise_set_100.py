# Algorithm Question 100  =  Encryption (From HackerRank)

"""
Encryption | 


Get the Probelm Statement on HackerRank : https://www.hackerrank.com/challenges/encryption/problem

And get the solved solution in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 14 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/encryption/problem)

# Solution :

from math import sqrt, floor, ceil

if __name__ == "__main__":
    s = input()
    s = s.replace(" ", "")
    r = floor(sqrt(len(s)))
    c = ceil(sqrt(len(s)))
    for i in range(c):
        print(s[i::c], end=" ")
