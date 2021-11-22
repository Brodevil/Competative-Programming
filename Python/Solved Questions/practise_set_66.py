# Python practise 66 = Forming a Magic Square (From hackerrank)

"""
Forming a Magic Square  |  Problem Statment :


Get the Problem Statment on hackerrank : https://www.hackerrank.com/challenges/magic-square-forming/problem

And get the solved solution in python by Brodevil here :|


"""


# Author = Abhinav
# Date = 8 August 2021
# Pourpose = Just for practise and imporving skills
# Source =   https://www.hackerrank.com/challenges/magic-square-forming/problem

# Solution :

#!/bin/python3

if __name__ == "__main__":
    import itertools
    s = []
    for i in range(3):
        s.extend(list(map(int, input().split(" "))))

    min_cost = 1000
    best = None
    def is_magic(s):
        for i in range(3):
            if sum(s[i*3:i*3+3]) != 15:
                return False
            if sum(s[i::3]) != 15:
                return False
        if s[0] + s[4] + s[8] != 15:
            return False
        if s[2] + s[4] + s[6] != 15:
            return False
        return True

    best = None
    for p in itertools.permutations(range(1,10)):
        cost = sum([abs(p[i] - s[i]) for i in range(len(s))])
        if cost < min_cost and is_magic(p):
            min_cost = cost
            best = p
            
    print(min_cost)