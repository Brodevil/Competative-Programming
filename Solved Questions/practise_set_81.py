# Algorithm Question 81 = Append and Delete (From HakcerRank)

"""
Append and Delete | Problem Statement :


Get the problem Statement on HackerRank : https://www.hackerrank.com/challenges/append-and-delete/problem

And get the solved solution in python By Brodevil here :|

"""

# Author = Abhinav
# Date = 26 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/append-and-delete/problem)

# Solution :


# Complete the 'appendAndDelete' function below.

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k


def appendAndDelete(s: str, t: str, k: int) -> str:
    # 1st solution :
    for ops_left in reversed(range(1, k + 1)):
        if s == t[:len(s)] and len(t) - len(s) == ops_left or len(s) == 0:
            break
        s = s[:-1]
    return ("Yes" if len(t) - len(s) <= ops_left else "No")


    # another solution
    """
    same = ""
    for _, __ in zip(s, t):
        if _ == __:
            same += _
        else:
            break
    
    if (len(s.replace(same, "")) + len(t.replace(same, ""))) <= k:
        return "Yes"
    else:
        return 'No'
    """


if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)
