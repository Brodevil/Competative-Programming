# Algorithm Question 116  =  Fair Rations (From HackerRank)

"""
Fair Rations |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/fair-rations/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 7 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/fair-rations/problem)

# Solution :

# Complete the 'fairRations' function below.

# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.



def fairRations(B: list) -> int:
    print(all(map(lambda x: x % 2 == 0, B)))
    breads = 0
    for _ in range(N):
        for _ in range(len(B)):
            if B[_] % 2 != 0:
                B[_] += 1
                if _+1 != B-1 :
                    pass



if __name__ == '__main__':
    N = int(input())
    B = list(map(int, input().split()))
    result = fairRations(B)
    print(result)
