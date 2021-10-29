# Algorithm Question 132  =  The Grid Search (From HackerRank)

"""
The Grid Search |


Get the Problem Statment on HackerRank : https://www.hackerrank.com/challenges/the-grid-search/problem

And get the solution in python here :}, solved by me.

"""

# Author = Abhinav
# Date = 28 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [The Gride Search](https://www.hackerrank.com/challenges/the-grid-search/problem)

# Solution :


for _ in range(int(input())):
    R, C = map(int, input().split())
    G = list()
    for _ in range(R):
        G.append(input())
    
    r, c = map(int, input().split())
    P = list()
    for _ in range(r):
        P.append(input())
    
    index = 0
    match = False
    iteration = 0
    
    for _ in G:
        if not match:
            if P[0] in _:
                index = _.index(P[0])
                # print(_, P[0], _[index: index+c], index, iteration)
                match = True
                iteration += 1
        
        else:
            
            if iteration == c-1 and c > 2:
                print("YES")
                # print(iteration, index)
                break

            elif _[index:index+c] != P[iteration]:
                match = False
                iteration = 0
            else:
                # print(_, P[iteration-1], _[index:index+c], index, iteration)
                iteration += 1
            
    else:
        print("NO")
