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

def diff(iterator) -> list:
    uniqe = list()
    for _ in iterator:
        if _ not in uniqe:
            uniqe.append(_)
    
    return uniqe


def climbingLeaderboard(ranked: list, player: list) -> list:
    ranks = list()
    for _ in player:
        ranked_uniq = sorted(diff([*ranked, _]))[::-1]
        ranks.append(ranked_uniq.index(_)+1)

    return ranks


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    for _ in result:
        print(_)
