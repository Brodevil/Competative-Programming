# Algorithm Question 135  =  CamelCase  (From HackerRank)

"""
CamelCase |


Get the Problem Statemen on HakerRank : https://www.hackerrank.com/challenges/camelcase/problem

And get the solution here, solved by me in python :}


"""

# Author = Abhinav
# Date = 5 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/camelcase/problem)

# Solution :

from string import ascii_uppercase as up

if __name__ == "__main__":
    s = input()
    no = 0
    for _ in s:
        if _ in up:
            no += 1

    print(no + 1)
