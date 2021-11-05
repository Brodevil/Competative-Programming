# Algorithm Question 134  =  Ema's Supercomputer  (From HackerRank)

"""
Ema's Supercomputer |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/two-pluses/problem

And get the solution here, solved in python by me :}
 
"""

# Author = Abhinav
# Date = 5 November 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/two-pluses/problem)

# Solution :


def twoPluses(ri, c, grid):

    tem = []
    tem.append(["O"] * (ri + 2))
    for x in grid:
        tem.append(["O"] + list(x) + ["O"])
    
    tem.append(["O"] * (ri + 2))
    grid = tem
    
    ans = 0
    for e in range(1, ri + 1):
        for v in range(1, c + 1):
            r = 0
            
            while grid[e + r][v] == "G" and grid[e - r][v] == "G" and grid[e][v + r] == "G" and grid[e][v - r] == "G":
                
                grid[e + r][v] = grid[e - r][v] = grid[e][v +
                                                          r] = grid[e][v - r] = "g"
                for E in range(1, ri + 1):
                    for V in range(1, c + 1):
                        R = 0
                        
                        while grid[E + R][V] == "G" and grid[E - R][V] == "G" and grid[E][V + R] == "G" and grid[E][
                                V - R] == "G":
                            ans = max(ans, (4*r + 1)*(4*R + 1))
                            R += 1
                r += 1
            
            r = 0
            while grid[e + r][v] == "g" and grid[e - r][v] == "g" and grid[e][v + r] == "g" and grid[e][v - r] == "g":
                grid[e + r][v] = grid[e - r][v] = grid[e][v +
                                                          r] = grid[e][v - r] = "G"
                r += 1

    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = list()
    for _ in range(n):
        grid.append(input())

    result = twoPluses(n, m, grid)
    print(result)
