# Algorithm Questino 105  =  Halloween Sale (From HackerRank)

"""
Halloween Sale | 


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/halloween-sale/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 19 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/halloween-sale/problem)

# Solution :

# Complete the 'howManyGames' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s


def howManyGames(p: int, d: int, m: int, s: int) -> int:
    n = (p-m) // d+1
    c = int(n/2*(2*p+(n-1)*-d))
    if c <= s:
        return n + (s-c) // m
    else:
        while n/2 * (2*p+(n-1)* -d) >s:
            n -= 1
        else:
            return n



if __name__ == '__main__':
    p, d, m, s = map(int, input().split())
    result = howManyGames(p, d, m, s)
    print(result)
