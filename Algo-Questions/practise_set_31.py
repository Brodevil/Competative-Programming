# Python practise 31 (From hackerrank) = Find a string = (https://www.hackerrank.com/challenges/find-a-string/problem)

"""
Find a string :

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.


NOTE: String letters are case-sensitive.


Input Format :
The first line of input contains the original string. The next line contains the substring.


Constraints :
1 < len(string) < 200
Each character in the string is an ascii character.


Output Format :
Output the integer number indicating the total number of occurrences of the substring in the original string.


Sample Input :
ABCDCDC
CDC


Sample Output :
2


Concept :

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where S is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])

A range function is used to loop over some length:

range (0, 5)
Here, the range loops over 0  to 4.5  is excluded.

"""

# Author = Abhinav
# Date = 6 May 2021
# Pourpose = Just for the python practise to not just learn python also to expert it


def count_substring(string, sub_string):
    return sum([1 for i in range(len(string)) if string[i : i+len(sub_string)] == sub_string])


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
