# Algorithm Question 94  =  B. MEXor Mixup (From CodeFoces)

"""
B. MEXor Mixup | 


Get the Problem Statement on CodeFroces : https://codeforces.com/problemset/problem/1567/B

And get the solved solution in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 8 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1567/B)

# Solution :

def minOpeartions(arr: list, n, x: int) -> int:
    k = x
    i = 0
    n = len(arr) -1
    while (n>-1) :
         
        if (arr[n] < x) :
            k -= 1
        if (arr[n] == x) :
            k += 1
        n -= 1
    return k
 


for _ in range(int(input())):
    a, b = map(int, input().split())
    