# Python practise 13 (From a practise Series with codewithharry) = Factorial

"""
Factorial :

Part 1:
    Calculate the factorial of a given number by the input.

Part 2:
    Find the number of trailing zero in the factorial

Note : Use functions

"""

# Author = Abhinav
# Date = 23 April 2021
# Pourpose = From the hacker rank picked the question for python practise


def factorial(number):
    """A function to just create a list of factorial and return it, I contain in both way that is iterative and recursive"""
   
    # recursive
    # if number == 1:
    #     return 1
    # else:
    #     return number*factorial(number-1)

    # iterative- returning a list so that we can trailing zero's
    factorials = [1]
    for i in range(1, number+1):
        factorials.append(factorials[i-1]*i)
    del factorials[0]
    return factorials



def trailingZero(factorialList):
    Zeros = list()
    for i in factorialList:
        if '0' in str(i):
            Zeros.append(i)
    return Zeros



if __name__ == "__main__":
    try:
        number = int(input("Enter a number which you want to generate factorial :\t"))
    except ValueError:
        print("Enter a league input that will a number ")
        exit()
    
    print(f"\nFollowing are the factorials of {number} :")
    numberFactorial = factorial(number)
    numberFactorial.reverse()
    for i in numberFactorial:
        print(i)

    trailedZero = trailingZero(numberFactorial)
    print(f"\nFollowing are the trailing zeros number :")
    for i in trailedZero:
        print(i)
    print(f"\nTotal {len(trailedZero)} number are trailing Zeros")