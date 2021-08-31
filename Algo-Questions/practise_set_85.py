# Algorith Question 85 = Non-Divisible Subset (From HackerRank)

"""
Non-Divisible Subset | Problem Statement :


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/non-divisible-subset/problem

And get the solved solution in python by Brodevil here :|

"""

# Author = Abhinav
# Date = 30 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/non-divisible-subset/problem)


# Solution :

# Complete the 'nonDivisibleSubset' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s


def nonDivisibleSubset(k: int, s: list) -> int:
    counts = [0] * k
    for number in s:
        counts[number % k] += 1

    count = min(counts[0], 1)
    for i in range(1, k//2+1):
        if i != k - i:
            count += max(counts[i], counts[k-i])
    if k % 2 == 0: 
        count += 1

    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)
