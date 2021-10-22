# Algorithm Question 124  =  Happy Ladybugs (From HackeRRank)

"""
Happy Ladybugs |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/happy-ladybugs/problem

And get the solved solution in python, here :}

"""

# Author = Abhinav
# Date = 21 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank]](https://www.hackerrank.com/challenges/happy-ladybugs/problem)

# Solution :


# Complete the 'happyLadybugs' function below.

# The function is expected to return a STRING.
# The function accepts STRING b as parameter.


def happyLadybugs(b: list) -> str:
    bugs = {_: b.count(_) for _ in set(b)}
    if bugs.get("_") is None:
        return "NO"
    for _, __ in bugs.items():
        if __ == 1 and _ != "_":
            return "NO"
    return "YES"


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        b = input()
        result = happyLadybugs(list(b))
        print(result)
