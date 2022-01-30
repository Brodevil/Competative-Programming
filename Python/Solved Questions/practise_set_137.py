# Compitative Programming Question 137  =  Insertion Sort - Part 2  (From HackerRank)

"""
Insertion Sort - Part 2 |


Get the problem statement on HackerRank : https://www.hackerrank.com/challenges/insertionsort2/problem

And get solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 7 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/insertionsort2/problem)

# Solution :

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    for _ in range(n):
        num = arr[_]
        a = arr.copy()
        if _ == 0:
            continue
        while _ != 0 and num < arr[_ - 1]:
            arr[_ - 1], arr[_] = arr[_], arr[_ - 1]
            _ -= 1

        print(*arr)
