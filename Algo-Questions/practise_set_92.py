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

for x in range(q):
    
    n = int(input().strip())
    m = []
    rowsum = [0]*n
    colsum = [0]*n
    
    for i in range(n):
        m.append(map(int, input().strip().split(' ')))
        rowsum[i] = sum(m[-1])
        colsum = map(lambda a, b: a+b, colsum, m[-1])
        
    rowsum.sort()
    colsum.sort()
    
    if rowsum == colsum:
        print('Possible')
    else:
        print('Impossible')
