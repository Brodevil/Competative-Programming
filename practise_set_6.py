# Python practise problem 6 (Easy, 10 points) - Guess the number

"""
Guess the number :

Problem Statement:-
Generate a randome integer from a and b. You and your friend have to guess a number between tow number a and b and 
both are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and 
your program must tell whether the number is greater than the number. You playteh same game and then the person with minimum number of trials wins!

Randomly generate a number after taking a and b taking input and don't show that number to the user.


Input:
Enter the value of a :
4
Enter the value of b :
13


Output:
Player 1:
Please guess the number between 4 and 13

5
Wrong! Guess a greater number again

8 
Wrong! Guess a greater number again


6 
Correct You tooked 3 trials to guess the number

Player 2:
Please guess the number between 4 and 13
.
.
.
Correct You tooked 7 trials to guess the number

>>> Player 1 wins as He tooked 3 trials and 

"""
from random import randint as rt

# Author = Abhinav
# Date = 20 April 2021
# Pourpose = Just For the python practise in very much josh


def num_checker(actual_num, check_num):
    if actual_num > check_num:
        return  "Wrong! Guess a greater number"
    
    elif actual_num < check_num:
        return "Wrong! Guess a smaller number"
    
    elif actual_num == check_num:
        return True

if __name__ == "__main__":
    try:
        players = {i : 0 for i in input("Enter the name of the playser by putting comma ', ' :\t").split(", ")}
        a = int(input("Enter the value of a i.e. first number of Range : \t"))
        b = int(input("Enter the value of b i.e second number of Range : \t "))
    except ValueError:
        print("Enter a league input that will a number :\n")

    # rt is randome.randit for choosing a randome number as a python choose
    python_choose = rt(a, b)

    for i in players.keys():
        print(f"{i}'s Turn :\nPlease Guess the number between {a} & {b}")
        while True:
            user_guess = int(input())
            checked = num_checker(python_choose, user_guess)
            if checked == True:
                print(f"Correct {players[i]}")
                break
			else:
				print(checked)
				players[i] += 1

