# Competitive Programming Question 139  =  Correctness and the Loop Invariant (From HackerRank)

"""
Correctness and the Loop Invariant |


Get the problem statement on HackerRank : https://www.hackerrank.com/challenges/correctness-invariant/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 9 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/correctness-invariant/problem)

# Solution :

if __name__ == "__main__":
    s = int(input())
    arr = list(map(int, input().split()))
    for i in range(s):
        while i != 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i-=1

    print(*arr)
