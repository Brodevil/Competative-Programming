# Copetative Programming Question 147  = Quicksort 1 - Partition  (From HackerRank)

"""
Quicksort 1 - Partition |

Get the Problem Statement on CodeForces : https://www.hackerrank.com/challenges/quicksort1/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 15 December 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/quicksort1/problem)

# Solution :

n = int(input())
arr = list(map(int, input().split()))
p = arr[0]
right = list()
left = list()

for _ in range(1, n):
    _ = arr[_]
    if _ > p:
        right.append(_)
    elif _ < p:
        left.append(_)

print(*[*left, p, *right])
