# Python Practise problem 5 (Easy, 10 points) = Palindromify the list
"""
Palindromify the list :-

You are given a array which contains some numbers. You have to print a list of next palindromes only if 
the number is greater then 10 otherwaise you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]

"""


# Author : Abhinav
# Date : 19 April 2021
# Pourpose : For more python practise 

        
def palindromify(lis):
    """
    This find the next palindrom of value having more then 10
    """
    for index, value in enumerate(lis):
        print(index, value)
        if value >= 10:
            while True:
                value += 1
                # cheacking whether the value are same which make it reverse
                if str(value)[::-1] == str(value):
                    lis[index] = value
                    break
    return lis
        
            
if __name__ == "__main__":
    # getting the int of input and putting as a list
    lst = list(map(int, input("Enter your list of numbers by space :\n").split()))
    print("This is dones")

    '''
    # one more another method to take list as a input :
    times = int(input("Enter lenght of your list : \t"))
    lst = list()
    for i in range(times):
        item = int(input("Enter the number : \t"))
        lst.append(item)
    print(lst)
    '''
    # called the functions in the fstring
    print(f"Palindromify of your list {lst} is :=: \t{palindromify(lst)}")

