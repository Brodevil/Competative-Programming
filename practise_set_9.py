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
import pyttsx3


def speak(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()


def jumpble(firstNames, lastNames):
    for index, firstName in enumerate(firstNames):
        name = f'{firstName.capitalize()} {choice(lastNames)[0]}'
        print(name)
        speak(name)


if __name__ == "__main__":
    try:
        noOfFriends = int(input("Enter the total numbers of friends : \t"))
    except ValueError:
        print("Enter the league input that will a integer\n")
        exit()

    firstNames = list()
    lastNames = list()
    for i in range(noOfFriends):
        try:
            name = input("Enter the full name of your friend :\t").split()
            firstNames.append(name[0]), lastNames.append(name[1:])
        except IndexError:
            print("Enter the Full name \n")
            exit()

    jumpble(firstNames, lastNames)
