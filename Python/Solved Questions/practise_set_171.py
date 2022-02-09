# Competative Programming Question 171 = B. Peculiar Movie Preferences (From CodeForces)

"""
B. Peculiar Movie Preferences |

Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1628/B

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 09 February 2022
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1628/B)

# Solution :

for _it in range(int(input())):
    n = int(input())
    ans = "NO"
    set1 = set()
    set2 = set()

    for i in range(n):
        s = input()
        ss = s[::-1]
        if s == ss or s in set2 or s in set1 or s[1:] in set1:
            ans = "YES"
        set1.add(ss)
        
        if len(ss) == 3:
            set2.add(ss[1:])
    
    print(ans)
