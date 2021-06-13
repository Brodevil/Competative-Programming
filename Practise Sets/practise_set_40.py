# Python practise 40 = (From hackerrank) = Merge the Tools!   (https://www.hackerrank.com/challenges/merge-the-tools)

"""
Merge the Tools!


Consider the following :
 - A string, s, of length n where s=c[0] c[1]...[n-1].
 - An integer, k, where k is a factor of n.


We can split S into n/k substrings where each subtring, t, consists of a contiguous block of  characters in k.
Then, use each t to create string u[i] such that:

 - The characters in  are a subsequence of the characters in t.
 - Any repeat occurrence of a character is removed from the string such that each character in u[i] occurs exactly once. 
   In other words, if the character at some index j in t[i] occurs at a previous index <j in t[i], then do not include the character in string u[i].


Given s and k, print n/k lines where each line i denotes string u[i]. 


Example :-
s= 'AAABCADDE' 
k=3


There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u[1] = 'A'. 
The second substring has all distinct characters, so u[2] = 'BCA'. 
The third substring has 2 different characters, so u[3]= 'DE'. Note that a subsequence maintains the original order of characters encountered. 
The order of characters in each subsequence shown is important.


Function Description :

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

 - string s: the string to analyze
 - int k: the size of substrings to analyze


Prints :
Print each subsequence on a new line. There will be n/k of them. No return value is expected.



Input Format :

The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.


Constraints :
 - 1<= n <= 10**4, where  is the length of 
 - 1 <= k <= n

It is guaranteed that n is a multiple of k.


Sample Input :

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3



Sample Output :
AB
CA
AD


Explanation :

Split  into  equal parts of length . Convert each  to  by removing any subsequent occurrences of non-distinct characters in :


(here many things are there just read it out by the given link) (https://www.hackerrank.com/challenges/merge-the-tools/problem)

Print each  on a new line.

"""


# Author = Abhinav
# Date = June 7 2021
# Pourpose = Just for python practicing will lots of dedications


def merge_the_tools(string, k):
    u = [string[i:i+k] for i in range(0, len(string), k)]
    t = ""
    s = list()
    for i in u:
        for j in i:
            if j not in t:
                t += j
        print(t)
        t = ""


def another_solution(string, k):
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

