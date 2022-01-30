# Competative Programming Question 152 = Mars Exploration (From HackerRank)

"""
Mars Exploration |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/mars-exploration/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 11 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/mars-exploration/problem)

# Solution :

s = input()
ss = "SOS" * (len(s) // 3)
print(sum([1 for i, j in zip(s, ss) if i != j]))
