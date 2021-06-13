# Python practise 17 (From hackerrank) = Find the runner up Score!

"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.


Input Format :
The first line contains n. The second line contains an array A[]  of  n integers each separated by a space.


Constraints:
1. 2<n<10
2. -100 < A[i] < 100


Output Format:
Print the runner-up score.


Sample Input 0 :
5
2 3 6 6 5


Sample Output 0 :
5


Explanation 0 :
Given list is[2, 3, 6, 6, 5] . The maximum score is 6, second maximum is 5. Hence, we print  5 as the runner-up score.

"""

# Author = Abhinav
# Date = 24 April 2021
# Motive = Just for the python practise to not just learn python also to expert it


if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    print(sorted(arr)[-2])
