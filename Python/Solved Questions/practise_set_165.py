# Competative Programming Question 165 = B. Fun with Even Subarrays (From CodeForces)

"""
B. Fun with Even Subarrays |

Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1631/B

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 2 February 2022
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1631/B)

# Solution :

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    a = a[::-1]
    
    _ = 1
    while _ < n:
        if a[0] != a[_]:
            _ += _
            ans += 1
        else:
            _ += 1
    
    print(ans)
