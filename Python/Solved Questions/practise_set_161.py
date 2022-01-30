# Competative Programming Question 161 = Find the Median (From HackerRank)

"""
Find the Median |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/find-the-median/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 24 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/find-the-median/problem)

# Solution :


def partition(l, start, end):
    pivot = l[start]
    bound = start + 1
    for i in range(start + 1, end + 1):
        if l[i] < pivot:
            l[i], l[bound] = l[bound], l[i]
            bound += 1

    bound -= 1
    l[start], l[bound] = l[bound], l[start]
    return bound


def find_median(l, start, end, k):
    if start == end:
        return l[end]

    cur = partition(l, start, end)
    if cur == k:
        return l[k]
    elif cur > k:
        return find_median(l, start, cur - 1, k)
    else:
        return find_median(l, cur + 1, end, k)


n = int(input())
l = list(map(int, input().split()))

k = n // 2

print(find_median(l, 0, n - 1, k))
