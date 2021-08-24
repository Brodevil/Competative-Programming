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


def jumpingOnClouds(c: list, k: int) -> int:
    e = 100
    i = k % len(c)

    e -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        e -= c[i] * 2 + 1
        
    return e


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)

"""
energy = 100 #initial energy
i = k % n #initial jump from 0
energy -= c[i] * 2 + 1 #initial energy loss
while i != 0:
    i = (i + k) % n
    energy -= c[i] * 2 + 1
    
print energy
"""