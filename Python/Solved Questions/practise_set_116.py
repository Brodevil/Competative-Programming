# Algorithm Question 116  =  Fair Rations (From HackerRank)

"""
Fair Rations |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/fair-rations/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 7 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/fair-rations/problem)

# Solution :

# Complete the 'fairRations' function below.

# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.


def fairRations(B: list) -> int:
    idx = [i for i, x in enumerate(B) if x % 2 == 1]
    if len(idx) % 2 == 1:
        return "NO"
    else:
        return sum([(idx[i + 1] - idx[i]) * 2 for i in range(0, len(idx), 2)])


if __name__ == "__main__":
    N = int(input())
    B = list(map(int, input().split()))
    result = fairRations(B)
    print(result)
