# Algorithm Question 90  =  ACM ICPC Team (From HackerRank)

"""
ACM ICPC Team |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/acm-icpc-team/problem

And get the solved solution in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 5 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/acm-icpc-team/problem)


# Solution :

# Complete the 'acmTeam' function below.

# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.


def acmTeam(topic: list) -> list:
    # Write your code here
    return 0


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)
    print(result)
