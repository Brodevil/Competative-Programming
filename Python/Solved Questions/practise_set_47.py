# Python practise 47 = Birthday Cake Candles (From hackerrank) = (https://www.hackerrank.com/challenges/birthday-cake-candles/problem)


"""
Birthday Cake Candles | Problem Statement :


You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.


Example :
    candles = [4, 4, 1, 3]

The maximum height candles are  units high. There are  of them, so return .



Function Description :

    Complete the function birthdayCakeCandles in the editor below.

    birthdayCakeCandles has the following parameter(s):

    - int candles[n]: the candle heights


Returns :
     - int: the number of candles that are tallest


Input Format :

The first line contains a single integer, n, the size of candles[].
The second line contains n space-separated integers, where each integer i describes the height of candles[].


Constraints :
    - 1 < n < 10^5
    - 1 < candles[i] < 10^7



Sample Input 0 :
    4
    3 2 1 3


Sample Output 0 :
    2


Explanation 0 :

Candle heights are [3, 2, 1, 3]. The tallest candles are 3 units, and there are 2 of them.


"""


# Author = Abhinav
# Date = 14 July 2021
# Pourpose = Now I am getting very less time to touch my laptop, so in few time lets Practise some new thing in Python
# Source = https://www.hackerrank.com/challenges/birthday-cake-candles/problem


# Soluction :


# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles: list):
    # Write your code here
    return candles.count(sorted(candles)[-1])


if __name__ == "__main__":
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)
