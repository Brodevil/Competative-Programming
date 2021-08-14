# Python practise 45 = Staircase (From hackerrank) = (https://www.hackerrank.com/challenges/staircase/problem)


"""
Staircase :

Staircase detail:

This is a staircase of size n = 4:
       #
      ##
     ###
    ####


Its base and height are both equal to n. 
It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

 - Write a program that prints a staircase of size n.

 
Function Description :

    Complete the staircase function in the editor below.

    staircase has the following parameter(s):

     - int n: an integer


Print :
    Print a staircase as described above.



Input Format :
    A single integer, n, denoting the size of the staircase.



Constraints :
    0 < n < 100.


Output Format :
    Print a staircase of size  using # symbols and spaces.


Note: The last line must have  spaces in it.


Sample Input :
    6 


Sample Output

     #
    ##
   ###
  ####
 #####
######


Explanation :

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of 
n = 6.

"""

# Author = Abhinav
# Date = 12 July 2021
# Pourpose = Now I am getting very less time to touch my laptop, so in few time lets Practise some new thing in Python
# Source = https://www.hackerrank.com/challenges/staircase/problem


# Solution :

#!/bin/python3

# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    [print(f"{' '*(n-_)}{'#'*_}") for _ in range(1, n+1)]
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
