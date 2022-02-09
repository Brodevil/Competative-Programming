# Competative Programming Question 172 = Game of Thrones - I (From HackerRank)

"""
Game of Thrones - I |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/game-of-thrones/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 09 February 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/game-of-thrones/problem)

# Solution :

from collections import Counter

s = input()
s = dict(Counter(s))
n = False

for item, no in s.items():
    if no % 2 != 0 and n:
        print("NO")
        break
    elif no % 2 != 0 and not n:
        n = True
else:
    print("YES")

