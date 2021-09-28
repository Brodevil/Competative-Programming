# Algorithm Practise 110  =  Flatland Space Stations (From HackerRank)

"""
Flatland Space Stations |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/flatland-space-stations/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 28 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/flatland-space-stations/problem)

# Solution :


if __name__ == '__main__':
    n, m = map(int, input().split())
    c = list(map(int, input().rstrip().split()))
    spaces = list()
    if len(c) == 1:
        print(min([c[0] - n, c[0] - 0]))

