# Algorithm Practise 107  =   Chocolate Feast (HackerRank)

"""
Chocolate Feast |


Get the problem Statement on HackerRank : https://www.hackerrank.com/challenges/chocolate-feast/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 21 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/chocolate-feast/problem)

# Solution :


if __name__ == "__main__":
    for _ in range(int(input())):
        n, c, m = map(int, input().split())
        count = n // c
        x = count
        while x >= m:
            a, b = divmod(x, m)
            count += a
            x = a + b
        print(count)
