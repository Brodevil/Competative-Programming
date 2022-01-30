# Python practise 23 (From hackerrank) = sWAP cASE

"""
sWAP cASE :

You are given a string and your task is to swap cases. In other words, convert all lowercase 
letters to uppercase letters and vice versa.


For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  


Function Description :
Complete the swap_case function in the editor below.
swap_case has the following parameters:
 - string s: the string to modify


Returns :
string: the modified string


Input Format :
A single line containing a string s.


Constraints :
0 <len(s)<100


Sample Input 0 :
HackerRank.com presents "Pythonist 2".


Sample Output 0 :
hACKERrANK.COM PRESENTS "pYTHONIST 2".


"""


# Author = Abhinav
# Date = 26 April 2021
# Motive = Just for the python practise to not just learn python also to expert it


def swap_case(s):
    return s.swapcase()


if __name__ == "__main__":
    result = swap_case(input())
    print(result)
