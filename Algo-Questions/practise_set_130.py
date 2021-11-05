# Algorithm Question 130  =  Two Sum (From LeetCode)

"""
Two Sum |


Get the Problem Statement on LeetCode : https://leetcode.com/problems/two-sum/submissions/

And get the Solved solution by me, in python, here :}

"""

# Author = Abhinav
# Date = 27 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [LeetCode](https://leetcode.com/problems/two-sum/submissions/)

# Solution :

nums = list(map(int, input().split()))
target = int(input())

for i in range(len(nums)):
    for _ in range(len(nums)):
        if i != _ and (nums[i] + nums[_]) == target:
            print([i, _])
