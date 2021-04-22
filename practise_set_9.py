# Python practise problem 9 (Medium, 20 points) = Jumpbled Funny Names

"""
Jumpbled funny names:

Its result day at school and not everyone is happy. You decided to make your friend laught by jumbling their 
names to come up with some funny names.

You program should take the number of the names and the names separated by spaces as input. Output
should be funny names i9n the same order.


Input:
Enter number of frineds:
3

Enter the names of your 3 friends :
Abhinav Choudhary
Sibam Gopale
Aniket bhagat


Output:

Abhinav Gopale
Aniekt choudhary
Sibam Bhagat 
# I will it meanse Abhinav will make more effective to this program and make laugh as I will make the computer to speak also in english which will defenatly make laught to the user lol


"""

# Author = Abhinav
# Date = 22 April 2021
# Pourpose = Just for the python practise here to become expert and get sucess by accheving my AIM
from random import choice



def jumpble(first_names, last_names):
    jumpbledNames = list()
    for i in first_names:
        print(f"{i} {choice(last_names)[0]}")



if __name__ == "__main__":
    no_of_friends = int(input("Enter a total number of your friends :\t"))
    first_names = list()
    last_names = list()

    print("Enter your friends name one by one :\n")
    for i in range(no_of_friends):
        name = input().split()
        first_names.append(name[0])
        last_names.append(name[1:])
    
    print("Following Are the Funny jumpbled name; Lol :\n")
    jumpble(first_names, last_names)
    