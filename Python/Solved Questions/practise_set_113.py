# Algorithm Question 113  =  Cavity Map (From HackerRank)

"""
Cavity Map |

Get the Probblem Statement on HackerRank : https://www.hackerrank.com/challenges/cavity-map/problem

And get the solved solution in python, here :}

"""

# Author = Abhinav
# Date = 1 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/cavity-map/problem)

# Solution :

# Complete the 'cavityMap' function below.

# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.


def cavityMap(grid: list) -> list:
    grid = [list(_) for _ in grid]

    for _ in range(1, n - 1):
        for i in range(1, n - 1):
            if (
                grid[_][i] > grid[_ - 1][i]
                and grid[_][i] > grid[_ + 1][i]
                and grid[_][i] > grid[_][i - 1]
                and grid[_][i] > grid[_][i + 1]
            ):
                grid[_][i] = "X"

    return ["".join(_) for _ in grid]


if __name__ == "__main__":
    n = int(input())
    grid = list()
    for _ in range(n):
        grid.append(input())
    result = cavityMap(grid)
    print("\n".join(result))
