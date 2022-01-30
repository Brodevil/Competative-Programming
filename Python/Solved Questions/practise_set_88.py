# Algorith Question 88 = Equalize the Array (From HackerRank)

"""
Equalize the Array |


Get the Problem Statement : https://www.hackerrank.com/challenges/equality-in-a-array/problem

And get the solved solution in python by Brodevil, here :

"""

# Author = Abhinav
# Date = 2 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/equality-in-a-array/problem)


# Solution :

# Complete the 'equalizeArray' function below.

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


def equalizeArray(arr: list) -> int:
    # Write your code here
    largest = 0
    for _ in arr:
        num = arr.count(_)
        if num > largest:
            largest = num
    return len(arr) - largest


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)
