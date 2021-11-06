# Algorithm Question 136  =  Insertion Sort - Part 1 (From HackerRank)

"""
Insertion Sort - Part 1 |


Get the Problem statement on HackerRank : https://www.hackerrank.com/challenges/insertionsort1/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 6 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/insertionsort1/problem)

# Solution :

if __name__ == '__main__' :
    n = int(input())
    arr = list(map(int, input().split()))

    num = arr[-1]
    index = n-1
        
    while arr[index-1] > num and index != 0:
        a = arr.copy()
        a[index] = arr[index-1]
        print(*a)
        arr[index-1], arr[index] = arr[index], arr[index-1]
        index -= 1

    print(*arr)
