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

def index(iterator, element):
    for index, value in enumerate(iterator):
        if value == element:
            return len(iterator) - (index)
    

def climbingLeaderboard(ranked: list, player: list) -> int:
    ranks = {index(set(sorted(ranked)), _) : _ for _ in ranked}

    result = list()
    for _ in range(len(player)):
        temp = index(set(sorted([*ranked, player[_]])[::-1]), player[_])
        result.append(temp+1)

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