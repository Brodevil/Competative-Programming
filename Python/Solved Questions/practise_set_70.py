# Practise set 70 =  The Hurdle Race (From Hackerrank) 

"""
The Hurdle Race | Problem Statement :


Get the Problem Set on hackerrank : https://www.hackerrank.com/challenges/the-hurdle-race/problem

And get the solution in python here :|

"""

# Author = Abhinav
# Date = 13 August 2021
# Pourpose = Just for practise and imporving python skills
# Source =  https://www.hackerrank.com/challenges/the-hurdle-race/problem


# Solution :

# Complete the 'hurdleRace' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height


def hurdleRace(k: int, height: list) -> int:
    dose = sorted(height)[-1]
    if dose > k:
        return dose - k
    return 0 



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
