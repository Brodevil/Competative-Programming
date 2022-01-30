# Algorithm Question 138  =  Intro to Tutorial Challenges (From HackerRank)

"""
Intro to Tutorial Challenges |


Get the Problem Satement on HackerRank : https://www.hackerrank.com/challenges/tutorial-intro/problem

And get the solution here, solved by me in python :}

"""

# Author = Abhinav
# Date = 8 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/tutorial-intro/problem)

# Solution :

# Complete the 'introTutorial' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr


def introTutorial(V: int, arr: list) -> int:
    # Shortest method
    result = arr.index(V)

    # Still this is algorithm Learning Process I will do it myself
    result = [_ for _ in range(n) if arr[_] == V][0]

    return result


if __name__ == "__main__":
    V, n = int(input()), int(input())
    arr = list(map(int, input().rstrip().split()))
    result = introTutorial(V, arr)
    print(result)
