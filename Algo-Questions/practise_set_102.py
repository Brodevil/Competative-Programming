# Algorithm Question 102  =  Modified Kaprekar Numbers

"""
Modified Kaprekar Numbers |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/kaprekar-numbers/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 16 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/kaprekar-numbers/problem)

# Solution :

if __name__ == "__main__":
    p, q = int(input()), int(input())
    results = list()
    for _ in range(p, q+1):
        sq = _*_
        d = len(str(sq))
        temp = list(str(sq))
        l, r = ''.join(temp[:d//2]), int(''.join(temp[d//2:]))

        if not len(l):
            l += "0"
            l = int(l)
        else:
            l = int(l)
        
        if l + r == _:
            results.append(_)
        
    print(*results)
