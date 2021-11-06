# Algorithm Question 117  =  Pangrams (From HackerRank)

"""
Pangrams |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/pangrams/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 11 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/pangrams/problem)

# Solution :

from string import ascii_lowercase

if __name__ == "__main__":
    n = input().lower()
    for _ in ascii_lowercase:
        if _ not in n:
            print("not pangram")
            break
    else:
        print("pangram")
