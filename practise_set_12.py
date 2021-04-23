# Python practise 12 (Easy) - Indian Kirana Shop

"""
Indian Kirana shop keeper calculator :

Created the python program that will keep adding a steam of numbers inputted by the user.
The adding stops as soon as user presses q key on the keyboard.
"""

if __name__ == "__main__":
    print("Welcome to the Indian Kirana shop keeper's Calculator python program \nKeep Entering your value you wants to add, And to stop the program and get result press 'q'")
    sum = 0
    while True:
        value = input("Enter the value and press Enter :\t")
        if value.lower() == "q":
            break
        else:
            try:
                sum += int(value)
                print(f"Order Total so far : {sum}\n")
            except ValueError:
                print("Enter a league input that will a number or press q to quite.\n")
        
    print(f"Your Bill total is: {sum:>10}\nThank you for Shoping with us")
