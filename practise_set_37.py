# Python practise 37 (From hackerrank) = Capitalize! = (https://www.hackerrank.com/challenges/capitalize/problem)

"""
Capitalize! :


You are asked to ensure that the first and last names of people begin with a capital
letter in their passports. For example, alison heck should be capitalised correctly as
Alison Heck.

 - alison heck => Alison Heck

Given a full name, your task is to capitalize the name appropriately.


Input Format :
A single line of input containing the full name, S.


Constraints :
- 0 <len(S)<1000
- The string consists of alphanumeric characters and spaces.


Note: in a word only the first character is capitalized.
Example 12abc when capitalized remains 12abc.

Output Format :
Print the capitalized string, S.


Sample Input :
chris alan


Sample Output :
Chris Alan

"""


# Author = Abhinav
# Date = 24 May 2021
# Purpose = Just for the python practise to not just learn python also to expert it


# Complete the solve function below.
def solve(s):
    # return " ".join(map(lambda x: x.capitalize(), s.split()))
    # for x in s.split():
    #     s = s.replace(x, x.capitalize())
    # return s
    return " ".join(map(lambda x:x.capitalize(), s.split()))


if __name__ == '__main__':
    s = input()
    print(solve(s))

