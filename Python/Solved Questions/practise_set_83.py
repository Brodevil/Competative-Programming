# Algorithm Question 83 = Library Fine (From HakcerRank)

"""
Library Fine | Problem Statement :


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/library-fine/problem

And get the solved solutiog in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 28 August 2021
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/library-fine/problem)

# Solution :

# Complete the 'libraryFine' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2


def libraryFine(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    fine = 0
    if d1 - d2 > 0 and m1 == m2 and y1 == y2:
        fine += (d1 - d2) * 15
    if m1 - m2 > 0 and y1 == y2:
        fine += (m1 - m2) * 500
    if y1 - y2 > 0:
        fine += (y1 - y2) * 10000

    return fine


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    print(result)
