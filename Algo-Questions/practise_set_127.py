# Algorithm Question 127  =  Big Sorting (From HackerRank)

"""
Big Sorting |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/big-sorting/problem

And the solution in python, by me, here :}

"""

# Author = Abhinav
# Date = 24 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/big-sorting/problem)

# Solution :

# In Python, This is the fasted solution, but still we aren't getting all the test cases correct. Its becoming wrong due to time exceeds
ls = list()
for _ in range(int(input())): ls.append(input())
for _ in sorted(ls, key= lambda x : int(x)): print(_)
    