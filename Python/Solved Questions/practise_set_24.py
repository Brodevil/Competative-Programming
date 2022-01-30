# Python practise 24 (From hackerrank) = String Split and Join


"""
String Split and Join :


In Python, a string can be split on a delimiter.


Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 


Task :
You are given a string. Split the string on a " " (space) delimiter and join using 
a - hyphen.


Function Description :
Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

 - string line: a string of space-separated words 

Returns :
 - string: the resulting string


Input Format :
The one line contains a string consisting of space separated words.
 

Sample Input :
this is a string  


Sample Output :
this-is-a-string

"""

# Author = Abhinav
# Date = 26 April 2021
# Motive = Just for the python practise to not just learn python also to expert it


def split_and_join(line):
    return "-".join(line.split())


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
