# Algorithm Question 101  =  Bigger is Greater

"""
Bigger is Greater |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/bigger-is-greater/problem

And get the solved solution in python, below :|

"""

# Author = Abhinav
# Date = 15 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/bigger-is-greater/problem)

# Solution :

# Complete the 'biggerIsGreater' function below.

# The function is expected to return a STRING.
# The function accepts STRING w as parameter.


def biggerIsGreater(w: str) -> str:
    arr = list(w)

    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"

    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    arr[i:] = arr[len(arr) - 1 : i - 1 : -1]
    return "".join(arr)


if __name__ == "__main__":
    for _ in range(int(input())):
        print(biggerIsGreater(input()))
