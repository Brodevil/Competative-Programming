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

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    special = 0
    page = 1
    
    for i in arr:
        for _ in range(1, i+1):
            if page == _:
                special += 1
            if _ > k:
                page += 1
        page += 1

    print(special)
