# Algorithm Question 91  =  Taum and B'day (From HackerRank)

"""
Taum and B'day | 


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/taum-and-bday/problem

And get the Solved solution in python by Brodevil, here :|

"""


# Author = Abhinav
# Date = 6 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/taum-and-bday/problem)


# Solution :

# Complete the 'taumBday' function below.

# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z


def taumBday(b: int, w: int, bc: int, wc: int, z: int) -> int:
    # Write your code here
    return 0


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        print(result)
