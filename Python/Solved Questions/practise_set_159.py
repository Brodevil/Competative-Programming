# Competative Programming Question 159 = Counting Sort 4 (From HackerRank)

"""
Counting Sort 4 |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/countingsort4/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 23 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/countingsort4/problem)

# Solution :

n = int(input())
arr = [[] for _ in range(n//2+1)]

for _ in range(n):
    x, s = input().split()
    x = int(x)
    if _ < n//2:
        arr[x].append("-")
    else:
        arr[x].append(s)

ans = ""
for _ in arr:
    for _0 in _:
        ans += f"{_0} "

print(ans)
