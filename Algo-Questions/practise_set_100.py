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

# Complete the 'encryption' function below.

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

from math import sqrt


def encryption(s: str) -> str:
    l = int(sqrt(len(s)))
    new = ''
    for _ in range(l):
        for i in range(_, len(s), l+1):
            new += s[i]

        new += " "
    for _ in range(l, len(s), l+1):
        new += s[_]
    return new


if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)
