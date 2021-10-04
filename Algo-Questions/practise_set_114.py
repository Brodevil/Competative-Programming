# Algorithm Practise 114 = Manasa and Stones (From HackerRank)

"""
Manasa and Stones |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/manasa-and-stones/problem

And get the Solved solution in python, here :|

"""

# Author = Abhinav
# Date = 2 Output 2021 (Gandhi Ji)
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/manasa-and-stones/problem)

# Solution :

for _ in range(int(input())):
    n, a, b = int(input()), int(input()), int(input())
    print(*sorted(set(x * a + (n - 1 - x) * b for x in range(n))))
