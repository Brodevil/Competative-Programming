# Algorithm Question 128  =  A. Gamer Hemose (From CodeForces)

"""
A. Gamer Hemose |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1592/A

And get the solution, solved by me, here :}

"""

# Author = Abhinav
# Date = 25 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [CodeFroces](https://codeforces.com/problemset/problem/1592/A)

# Solution :


for _ in range(int(input())):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    m = arr[0] + arr[1]
    ans = 2 * (h//m)

    if (h % m > arr[0] and h % m > 0):
        ans += 2
    elif h % m > 0:
        ans+=1
    
    print(ans)
