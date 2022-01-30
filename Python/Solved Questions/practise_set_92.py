# Algorithm Question 92  =  Organizing Containers of Balls  (From HackerRank)

"""
Organizing Containers of Balls |


Get the Problem Statement On HackerRank : https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

And get the solved solution in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 6 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem)

# Solution :

q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    M = list()
    for M_i in range(n):
        M_t = [int(M_temp) for M_temp in input().strip().split(" ")]
        M.append(M_t)

    var1 = list()
    var2 = list()

    for i in range(n):
        var1.append(0)
        var2.append(sum(M[i]))
        for j in range(n):
            var1[i] += M[j][i]

    var1.sort()
    var2.sort()

    if var1 == var2:
        print("Possible")
    else:
        print("Impossible")
