# Python practise 13 (From a practise Series with codewithharry) = Factorial

"""
Factorial :

Part 1:
    Calculate the factorial of a given number by the input.

Part 2:
    Find the number of trailing zero in the factorial

Note : Use functions

"""

def factorial(number):
    # if number == 1:
    #     return 1
    # else:
    #     return number*factorial(number-1)
    while number <= 1:
        result = number * number-1
        number -= 1
    return result

if __name__ == "__main__":
    print(factorial(5))