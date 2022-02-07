# Competative Programming Question 168 = Larry's Array (From HackerRank)

"""
Larry's Array |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/larrys-array/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 7 February 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/larrys-array/problem)

# Solution :


for _ in range(int(input())):
    count = 0
    n = int(input())
    l = list(map(int, input().split()))

    for i in range(n-1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                count += 1
            print(l[i], l[j], count)
    
    if count % 2 == 0:
        print("YES")
    else:
        print("NO")
