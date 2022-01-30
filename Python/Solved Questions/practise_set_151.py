# Competative Programming Question 151 = Caesar Cipher (From HackerRank)

"""
Caesar Cipher |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/caesar-cipher-1/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 9 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/caesar-cipher-1/problem)

# Solution :

from string import ascii_lowercase, ascii_uppercase

n, s, k = int(input()), input(), int(input())
new = ""


def work(s, ls):
    global new
    n = ls.index(s) + k
    new += ls[n % 26]


for _ in s:
    if _ in ascii_lowercase:
        work(_, ascii_lowercase)

    elif _ in ascii_uppercase:
        work(_, ascii_uppercase)
    else:
        new += _

print(new)
