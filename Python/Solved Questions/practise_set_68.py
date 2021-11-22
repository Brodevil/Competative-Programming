# Python Practise 68 =  Ezzat and Two Subsequences (From codeforces)

"""
Ezzat and Two Subsequences | Problem Statment (A):


Get the Problem Statment on Code Forces : https://codeforces.com/problemset/problem/1557/A

And get the solved solution in python here :|

"""


# Author = Abhinav
# Date = 10 August 2021
# Pourpose = Just for practise and imporving python skills
# Source =   https://codeforces.com/problemset/problem/1557/A


# Solution :


def solve(array: list) -> str:
    largest = 0
    for _ in range(len(array)):
        currect_array = array.copy()
        currect_array.remove(array[_])
        ans = array[_] + (sum(currect_array) / len(currect_array))

        if ans > largest:
            largest = ans
        elif _ == 0:
            largest = ans
    
    return f"{largest:.9f}"


if __name__ == "__main__":
    for _ in range(int(input())):
        input()
        array = list(map(int, input().split()))
        result = solve(array)
        print(result)
