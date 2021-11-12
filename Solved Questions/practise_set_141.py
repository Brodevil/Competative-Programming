# Question 141  =  HackerRank in a String! (From HackerRank)

"""
HackerRank in a String! |


Get the Problem Statement on HackerRank :  https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 12 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/correctness-invariant/problem)

# Solution :

import re

for _ in range(int(input())):
    print('YES' if re.search(r'.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*',input().strip()) else 'NO')
