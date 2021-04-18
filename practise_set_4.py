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
try:
    times = int(input("Enter the number of test cases : \t"))

    
    for i in range(times):
        before_num = int(input("Enter the number :\t"))
        while True:
            if int(str(before_num)[::-1]) == before_num:
                print(before_num)
                break   
            before_num += 1
except ValueError:
    print("Enter a league Input i.e. numbers")
    exit()