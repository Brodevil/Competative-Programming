# Algorithm Question 109  =  Lisa's Workbook (From HackerRank)

"""
Lisa's Workbook |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/lisa-workbook/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 24 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/lisa-workbook/problem)

# Solution :

def foo(n):
    global k, page, special
    i = 1
    for _ in range(1, int(n)+1):
        print(_, page, special, _)
        if _ == page:
            special += 2
        if i % k == 0:
            page += 1
            i = 1
        i += 1


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    page = 1
    special = 0
    for _ in arr:
        foo(_)
        page += 1

    print(special)
        