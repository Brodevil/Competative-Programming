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

n, m = map(int, input().split())
c = list(map(int, input().split()))
c.sort()

maxgap = max(a - b for a, b in zip(c[1:], c)) if len(c) > 1 else 0
ans = max(maxgap // 2, c[0], n - 1 - c[-1])

print(ans)
