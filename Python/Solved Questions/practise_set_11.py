# Python Practise 10- From the Hacker Rank (Print function)

"""
Print Function :

The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "....." represents the consecutive values in between.

Example
n=5

Print the string 12345.

Input Format:
The first line contains an integer .


Constraints:
1<n<150

Output Format:
Print the list of integers from  through  as a string, without spaces.

Sample Input 0:
3

Sample Output 0:
123


"""

# Author = Abhinav
# Date = 22 April 2021
# Pourpose = From the hacker rank picked the question for python practise


if __name__ == "__main__":
    n = int(input())
    lis = [str(i) for i in range(1, n + 1)]
    print("".join(lis))
