# Competative Programming Question 162 = A. Ancient Civilization (From CodeForces)

"""
A. Ancient Civilization |

Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1625/A

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 24 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1625/A)

# Solution :

for _ in range(int(input())):
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [bin(_)[2:].zfill(l) for _ in arr]
    ans = ""

    for _ in range(l):
        temp = "".join([i[_] for i in arr])
        if temp.count("1") > temp.count("0"): ans += "1"
        else: ans += "0"
    
    print(int(ans, 2))
