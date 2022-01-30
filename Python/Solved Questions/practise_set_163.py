# Competative Programming Question 161 = Insertion Sort Advanced Analysis (From HackerRank)

"""
Insertion Sort Advanced Analysis |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/insertion-sort/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 29 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/insertion-sort/problem)

# Solution :


def merge(arr, L, R):
    i = il = ir = inversion_count = 0
    l_len = len(L)
    r_len = len(R)
    
    while il < l_len and ir < r_len:
        if L[il] <= R[ir]:
            arr[i] = L[il]
            il += 1
        else:
            arr[i] = R[ir]
            ir += 1
            inversion_count += l_len - il
        i += 1
    
    while il < l_len:
        arr[i] = L[il]
        il += 1
        i += 1
    
    while ir < r_len:
        arr[i] = R[ir]
        ir += 1
        i += 1

    return inversion_count


def merge_sort(arr):
    mid = len(arr) // 2
    inversion_count = 0
    if mid > 0:
        L = arr[:mid]
        R = arr[mid:]
        inversion_count += merge_sort(L)
        inversion_count += merge_sort(R)
        inversion_count += merge(arr, L, R)
    return inversion_count


def inversions(arr):
    return merge_sort(arr)


for _ in range(int(input())):
    n = input()
    arr = list(map(int, input().split()))
    counts = inversions(arr)
    print(counts)
