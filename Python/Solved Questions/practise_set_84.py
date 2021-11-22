# Algorithms Question 84 = Cut the sticks (From HackerRank)

"""
Cut the sticks | Problem Statement :


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/cut-the-sticks/problem

And get the solved solution in python By Brodevil, here :|

"""

# Author = Abhinav
# Date = 29 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/cut-the-sticks/problem)


# Solution :

# Complete the 'cutTheSticks' function below.

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.


def cutTheSticks(arr: list) -> list:
    result = list()

    while len(arr) != 0:
        result.append(len(arr)) 
        smallest = sorted(arr)[0]
        arr = list(filter((smallest).__ne__, arr))
        for _ in range(len(arr)):
            diff = arr[_] - smallest
            arr[_] = diff

    return result        


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print(result)
