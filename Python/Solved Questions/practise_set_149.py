# Copetative Programming Question 147  = Quicksort 2 - Sorting  (From HackerRank)

"""
Quicksort 2 - Sorting |

Get the Problem Statement on CodeForces : https://www.hackerrank.com/challenges/quicksort2/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 16 December 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/quicksort2/problem)

# Solution :


def quick_sort(ar: list):
    if len(ar) <= 1:
        return ar
    left, equal, right = partition(ar)
    newarr = quick_sort(left) + equal + quick_sort(right)
    print(" ".join(str(e) for e in newarr))
    return newarr


def partition(ar: list):
    left = []
    equal = [ar[0]]
    right = []
    for elem in ar[1:]:
        if elem == ar[0]:
            equal.append(elem)
        elif elem < ar[0]:
            left.append(elem)
        else:
            right.append(elem)
    return left, equal, right


n = input()
ar = list(map(int, input().split()))

quick_sort(ar)
