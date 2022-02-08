# Competative Programming Question 170 = B. Minority (From CodeForces)

"""
B. Minority |

Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1633/B

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 08 February 2022
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1633/B)

# Solution :

for _ in range(int(input())):
    s = input()
    print(min((len(s) - 1) // 2, s.count('0'), s.count('1')))
