# Competative Programming Question 157 = Counting Sort 2 (From HackerRank)

"""
Counting Sort 2 |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/countingsort2/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 19 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/countingsort2/problem)

# Solution :

n = int(input())
arr = list(map(int, input().split()))

# Sorted list in index form
index_ls = [0] * 100
for _ in arr:
    index_ls[_] += 1

# Converting into sorted form
ls = list()
for i, j in enumerate(index_ls):
    for _ in range(j):
        ls.append(i)

print(*ls)
