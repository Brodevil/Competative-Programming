# Python Practise 14 - Currency Converter
"""
Created a Currency converter python program that will convert your Currency to several Currency
The currency data is available in the currency.txt file in this directory.

Using those data You have to create the python program to convert any Currency to any other Currency
"""

# Author = Abhinav
# Date = 23 April 2021
# Purpose = Just for the python practise to become expert in the python programming and logic building


if __name__ == "__main__":
    # This part is just creating the currency Dict from by reading the currency.txt file and also by parsing it
    with open("currency.txt", "rt") as f:
        lines = f.readlines()
    currencyDict = dict()
    for line in lines:
        parsed = line.split("\t")
        currencyDict[parsed[0]] = parsed[1]

    # UI Starts from here
    try:
        amount = int(input("Enter the amount :\t"))
    except ValueError:
        print("Enter a league Age that will a number\n")
    else:
        print(
            "Enter the name of the currency you want to convert this amount to? \nAvailable Options :\n"
        )
        [print(item) for item in currencyDict.keys()]
        currency = input(
            "\nNow You have the basic Idea, Now Plz Enter in which currency You want to convert : \n"
        )
        try:
            print(
                f"{amount} INR in {currency} = {amount*float(currencyDict[currency])} {currency}\n"
            )
        except Exception as a:
            print(a)
            print(
                f"Please Enter a League input {currency} is not present Here, Note:> It should be case sensitive\n"
            )
        else:
            print("Thank you for Choosing us")
