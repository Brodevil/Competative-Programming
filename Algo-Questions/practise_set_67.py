# Python practise 67 = Picking Numbers (From hackerank)

"""
Picking Numbers | Problem Statement :


Get the Problem Statment on hackerrank : https://www.hackerrank.com/challenges/picking-numbers/problem

And get the sovled solution in python by Brodevil here :|


"""


# Author = Abhinav
# Date = 9 August 2021
# Pourpose = Just for practise and imporving python skills
# Source =   https://www.hackerrank.com/challenges/picking-numbers/problem

# Solution :


def pickingNumbers(a: list):
    # Write your code here
    maximum=0
    for i in a:
        c = a.count(i)
        d = a.count(i-1)
        c = c + d
        if c > maximum:
            maximum=c

    return maximum


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
