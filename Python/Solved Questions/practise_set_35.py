# Python practise 35 (From hackerrank) = Designer Door Mat = (https://www.hackerrank.com/challenges/designer-door-mat/problem)

"""
Designer Door Mat :


Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat
with the following specifications:

 - Mat size must be M X N. (N is an odd natural number, and M is 3 times .)
 - The design should have 'WELCOME' written in the center.
 - The design pattern should only use |, . and - characters.


Sample Designs :

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------


Input Format:
A single line containing the space separated values of N and M.


Constraints :
 - 5 < N <101
 - 15 < M < 303


Output Format :
Output the design pattern.



Sample Input :
9 27


Sample Output :

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""

# Author = Abhinav
# Date = 23 May 2021
# Purpose = Just for the python practise to not just learn python also to expert it


if __name__ == "__main__":
    n, m = map(int, input().split())
    pattern = [(".|." * (2 * i + 1)).center(m, "-") for i in range(n // 2)]
    print("\n".join(pattern + ["WELCOME".center(m, "-")] + pattern[::-1]))
