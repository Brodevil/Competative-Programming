# Algorithm Question 119 = Separate the Numbers (From HackerRank)

"""
Separate the Numbers |


Get the Problem Statment on HackerRank : https://www.hackerrank.com/challenges/separate-the-numbers/problem

And get the solved solution in python... here:|

"""

# Author = Abhinav
# Date = 14 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/separate-the-numbers/problem)

# Solution :


for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        print("NO")
    for _ in range(len(s)):
        n = s[_]
        
