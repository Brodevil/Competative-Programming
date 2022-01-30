# Algorithm Question 132  =  The Grid Search (From HackerRank)

"""
The Grid Search |


Get the Problem Statment on HackerRank : https://www.hackerrank.com/challenges/the-grid-search/problem

And get the solution in python here :}, solved by me.

"""

# Author = Abhinav
# Date = 28 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [The Gride Search](https://www.hackerrank.com/challenges/the-grid-search/problem)

# Solution :


n = 0
n2 = 0

for i in range(0, int(input())):
    n, c = map(int, input().split())
    thegrid = list()

    for i in range(0, n):
        thegrid.append(input())

    n, c = map(int, input().split())
    subgrid = list()

    for i in range(0, n):
        subgrid.append(input())

    found = False

    for i in range(0, len(thegrid)):
        for j in range(0, len(subgrid)):
            if subgrid[j] in thegrid[i + j]:
                if j == len(subgrid) - 1:
                    found = True
                    print("YES")
                    break
                continue
            else:
                break
            break

    if not found:
        print("NO")
