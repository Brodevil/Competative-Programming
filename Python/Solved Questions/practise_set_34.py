# Practise set 35 (From hackerrank) = Text Wrap = (https://www.hackerrank.com/challenges/text-wrap/problem)

"""
Text Wrap :


You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.


Function Description :-
Complete the wrap function in the editor below.

wrap has the following parameters:
 - string string: a long string
 - int max_width: the width to wrap to


Returns

 - string: a single string with newline characters ('\n') where the breaks should be



Input Format :

The first line contains a string, STRING.
The second line contains the width, Max width.

Constraints :
- 0 < len(string) < 1000
- 0 < max w idth < len(string)


Sample Input 0 :
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4


Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ


"""

# Author = Abhinav
# Date = 18 May 2021
# Purpose = Just for the python practise to not just learn python also to expert it

import textwrap


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == "__main__":
    string, max_width = input(), int(input())
    print(wrap(string, max_width))
