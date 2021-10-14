# Algorithm Question 118  =  Weighted Uniform Strings (From HackerRank)

"""
Weighted Uniform Strings |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/weighted-uniform-string/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 11 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/weighted-uniform-string/problem)

# Solution :

from string import ascii_lowercase as lc

if __name__ == "__main__":
    s = input()
    result = list()

    for _ in s:
        weight = lc.index(_)+1
        for i in range(1, s.count(_)+1): result.append(weight*i)
    
    for _ in range(int(input())): 
        queary = int(input())
        if queary in result:
            print("Yes")
        else:
            print("No")
