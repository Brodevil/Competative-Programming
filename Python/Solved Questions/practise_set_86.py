# Algorith Question 86 = Repeated String (From HackerRank)

"""
Repeated String | Problem Statement :

Get the Problem Statement on Hackerrank : https://www.hackerrank.com/challenges/repeated-string/problem

And get the solved solution in python By Brodevil here :|

"""


# Author = Abhinav
# Date = 31 August 2021
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/repeated-string/problem)


# Solution :

# Complete the 'repeatedString' function below.

# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n


def repeatedString(s: str, n: int) -> int:
    if n % len(s) == 0:
        return s.count("a") * n
    else:
        return s[: (n % len(s))].count("a") + (s.count("a") * (n // len(s)))


if __name__ == "__main__":
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)
