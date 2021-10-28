# Algorithm Question 131  =  Add two Number (From LeetCode)

"""
Add two Number | (It's not Easy, Please go throught the Question)


Get the Problem Statement on LeetCode : https://leetcode.com/problems/add-two-numbers/

And get the solution, solved by me, here :}

"""

# Author = Abhinav
# Date = 27 Output 2021
# Pourpose = Just for practise and imporving skills
# Source =  [LeetCode](https://leetcode.com/problems/two-sum/submissions/)

# Solution :


class Solution(object):
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _l1 = int("".join([str(_) for _ in l1[::-1]]))
        _l2 = int("".join([str(_) for _ in l2[::-1]]))
        return [int(_) for _ in str(_l1 + _l2)[::-1]]

result = Solution()
output = result.addTwoNumbers(list(map(int, input().split())), list(map(int, input().split())))
print(output)
