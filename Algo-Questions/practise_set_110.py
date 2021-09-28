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
    space = list()
    for _ in range(n):
        gaps = list()
        for i in c:
            gaps.append(abs(_ - i))
        space.append(min(gaps))
    
    print(max(space))
