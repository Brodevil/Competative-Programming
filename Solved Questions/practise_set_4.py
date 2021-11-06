# Practise set 4 - The next Polindrome (10 points)
"""
The Next Polindrome:

Problem content:
A palindrome is a string which when revedrse it equal to itself. Example of palindrome includes
616, mom, 676, 10001.
You have to take a number as an input from teh user. You have to find the next palindrome 
corresponding to that number. Your first input should be 'number of the test cases' And then
take all the cases as input from the user.

Input:
3
451
10
2133

Output:
Next polindrome for 451 is 454
Next polindrome for 10 is 11
Next polindrome for 2133 is 2222

"""
# Author : Abhinav
# Date : 18 April
# Purpose ; For the just practising in python


# condition hadnling for the inputs
try:
    times = int(input("Enter the number of test cases : \t"))

    # this will take the input as per the number of times 
    for i in range(times):
        before_num = int(input("Enter the number :\t"))     
        store = before_num

        # by infnite loop checking in the sequence the next polidrome number
        while True:
            before_num += 1
            if str(before_num)[::-1] == str(before_num):
                print(f"Next polindrome for {store} is {before_num}")
                break   
            
except ValueError:  # exception handling
    print("Enter a league Input i.e. numbers")
    exit()