# Python practise 12 (Easy) - Indian Kirana Shop

"""
Indian Kirana shop keeper calculator :

Created the python program that will keep adding a steam of numbers inputted by the user.
The adding stops as soon as user presses q key on the keyboard.

Additionlly at last Show the customer how much prices I bought

Example:
Shree Ram Kirana:
1. #20
2. #30
3. #60
And then totale
"""

# Author = Abhinav
# Date = 23 April 2021
# Pourpose = From the hacker rank picked the question for python practise


if __name__ == "__main__":
    print("Welcome to the Indian Kirana shop keeper's Calculator python program \nKeep Entering your value you wants to add, And to stop the program and get result press 'q'")
    totalSum = list()
    while True:
        value = input("Enter the value and press Enter :\t")
        if value.lower() == "q":
            break
        else:
            try:
                totalSum.append(int(value))
                print(f"Order Total so far : {sum(totalSum)}\n")
            except ValueError:
                print("Enter a league input that will a number or press q to quite.\n")
        
    print(f"Your Bill total is: {sum(totalSum):>10}\nThank you for Shoping with us\n\n")

    print("Shree Ram's Shop Bill :")
    for index, value in enumerate(totalSum):
        print(f"{index+1}. #{value} Rupees item")
