# Practise set 70 = Climbing the Leaderboard (From Hackerrank) 

"""
Climbing the Leaderboard | Problem Set :


Get the Problem Statment on hackerrank : https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

And get the solved solution in python by Brodevil here :|

"""


# Author = Abhinav
# Date = 11 August 2021
# Pourpose = Just for practise and imporving python skills
# Source =  https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


# Solution :

#!/bin/python3

# Complete the 'climbingLeaderboard' function below.

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player

def index(iterator, element, result=True):
    for index, value in enumerate(iterator):
        if value == element:
            if result:
                return len(iterator) - (index)
            else:
                return index+1

def climbingLeaderboard(ranked: list, player: list) -> int:
    ranks = {index(set(sorted(ranked)), _) : _ for _ in ranked}

    result = list()
    for _ in range(len(player)):
        new = set(sorted([*ranked, player[_]]))
        print(new)
        temp = index(new, player[_], result=False)
        print(temp, player[_])
        result.append(temp)

    return result

if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)


"""
4
100 90 90 80
3
70 80 105
"""