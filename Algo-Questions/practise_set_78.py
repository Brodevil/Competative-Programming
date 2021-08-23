# Algorithms Question 78 = Jumping on the Clouds: Revisited (From HackerRank)

"""
Jumping on the Clouds: Revisited | Problem Statment :


Get the Problem Statement on Hackerrank : https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

And get the solved solution in python By Brodevil here :|

"""

# Author = Abhinav
# Date = 22 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem)

# Solution :


def jumpingOnClouds(c, k):
    return 0


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)
