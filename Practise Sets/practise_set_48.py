# Python practise 48 = Time Conversion (From hackerrank) = (https://www.hackerrank.com/challenges/time-conversion/problem)

"""
Time Conversion | Problem Statement :


Given a time in 12-hour AM/PM format, 
convert it to military (24-hour) time.


Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
      - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.



Example :
    - s = "12:001:00PM"
        Return '12:01:00'.

    - s - "12:01:00 AM"
        Return '00:01:00'.


Function Description :

    Complete the timeConversion function in the editor below. 
    It should return a new string representing the input time in 
    24 hour format.

    timeConversion has the following parameter(s):

    - string s: a time in 24 hour format


Returns :

    string: the time in 24 hour format



Input Format :
    A single string  that represents a time in -hour clock format 
    (i.e.:  or ).


Constraints :

    - All input times are valid


Sample Input 0 :
    07:05:45PM


Sample Output 0 :
    19:05:45


"""



# Author = Abhinav
# Date = 15 July 2021
# Pourpose = Now I am getting very less time to touch my laptop, so in few time lets Practise some new thing in Python
# Source = https://www.hackerrank.com/challenges/time-conversion/problem


# Soluction :

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    meridium = s[-2:]
    s = s.replace(s[-2:], "")
    times = list(map(int, s.split(":")))
    
    if meridium == "PM":
        times[0] += 12
    
    elif meridium == "AM" and times[0] == 12:
        times[0] = 0
    
    for _ in range(len(times)):
        if len(str(times[_])) == 1:
            times[_] = f"0{times[_]}"
        else:
            times[_] = str(times[_])
        
    return ":".join(times)         
    


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
