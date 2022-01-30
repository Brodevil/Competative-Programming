# Competative Programming Question 158 = Counting Sort 3 (From HackerRank)

"""
Counting Sort 3 |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/countingsort3/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 20 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/countingsort3/problem)

# Solution :

arr = list()
for _ in range(int(input())):
    x = int(input().split()[0])
    arr.append(x)

fq = [0] * 100
for _ in arr:
    fq[_] += 1

ans = list()
for _ in range(1, 101):
    ans.append(sum(fq[:_]))

print(*ans)
