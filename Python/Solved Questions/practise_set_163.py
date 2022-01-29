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

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for _ in range(n-1):
        while arr[_] > arr[_+1]:
            arr[_], arr[_+1] = arr[_+1], arr[_]
            ans += 1
            if _ != 0: _ -= 1
    
    print(ans)
