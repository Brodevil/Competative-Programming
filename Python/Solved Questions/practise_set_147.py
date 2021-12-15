# Copetative Programming Question 147  = Running Time of Algorithm  (From HackerRank)

"""
Running Time of Algorithms |

Get the Problem Statement on CodeForces : https://www.hackerrank.com/challenges/runningtime/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 15 December 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/runningtime/problem)

# Solution :

shifts = 0

n = int(input())
arr = list(map(int, input().split()))

for _ in range(n):
    for i in range(_, n):
        if arr[_] > arr[i]:
            shifts += 1
print(shifts)
