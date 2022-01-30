# Competative Programming Question 160 = Closest Numbers (From HackerRank)

"""
Closest Numbers |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/closest-numbers/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 24 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/closest-numbers/problem)

# Solution :

n = int(input())
arr = sorted(list(map(int, input().split())))
diff = abs(arr[0] - arr[1])
ans = list()

for _ in range(n - 1):
    d = abs(arr[_] - arr[_ + 1])
    if diff == d:
        ans += [arr[_], arr[_ + 1]]
        diff = d
    elif d < diff:
        ans = [arr[_], arr[_ + 1]]
        diff = d

print(*ans)
