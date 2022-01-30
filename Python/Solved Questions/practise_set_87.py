# Algorithm Question 87 = Jumping on the Clouds (From HackerRank)

"""
Jumping on the Clouds | Problem Statement : 


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

And get the solved solution in python By Brodevil, here :|

"""

# Author = Abhinav
# Date = 1 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem)


# Solution :

# Complete the 'jumpingOnClouds' function below.

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.


def jumpingOnClouds(c: list) -> int:
    x, y = 0, 0
    while x < len(c) - 2:
        x = x + 1 if c[x + 2] else x + 2
        y += 1
    if x < len(c) - 1:
        y += 1
    return y


if __name__ == "__main__":
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
