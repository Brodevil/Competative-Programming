# Algorthms Question 82 = Sherlock and Squares (From HackerRank)

"""
Sherlock and Squares | Problem Statement :


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/sherlock-and-squares/problem

And get the solved solution in python by Brodevil here :|

"""

# Author = Abhinav
# Date = 27 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/sherlock-and-squares/problem)

# Solution :

# Complete the 'squares' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b


def squares(a: int, b: int) -> int:
    # Write your code here
    return 0


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(result)
