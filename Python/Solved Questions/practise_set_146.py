# Copetative Programming Question 146  = Anagram  (From HackerRank)

"""
Anagram |

Get the Problem Statement on CodeForces : https://www.hackerrank.com/challenges/anagram/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 13 December 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/anagram/problem)

# Solution :

from collections import Counter

def anagram(s):
    if len(s) % 2: return -1
    l = len(s)//2
    a = Counter(s[:l])
    b = Counter(s[l:])
    return l-sum((a & b).values())

for _ in range(int(input())):
    print(anagram(input()))
