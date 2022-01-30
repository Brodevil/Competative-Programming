# Competitive Programming Question 140  =  Word Order (From HackerRank)

"""
Word Order |


Get the Problem Statement on HackerRnak : https://www.hackerrank.com/challenges/word-order/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 10 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/word-order/problem)

# Solution :

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


d = OrderedCounter(input() for _ in range(int(input())))

print(len(d))
print(*d.values())
