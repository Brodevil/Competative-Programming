# Algorithm Question 96  =  Designer PDF Viewer

"""
Designer PDF Viewer |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

And get the solved solution in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 10 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/designer-pdf-viewer/problem)

# Solution :

from string import ascii_lowercase as lc

heights = list(map(int, input().split()))
name = input()
hightest = 0

for _ in name:
    height = heights[lc.index(_)]
    if height > hightest:
        hightest = height

print(len(name)*hightest)