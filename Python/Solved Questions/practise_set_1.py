# Practise Problem 1 - Your age in 2090
"""
Your age in 2090
"""
if __name__ == "__main__":
    while True:
        age = input("Enter Your are or birth year : ")
        if age.isalpha():
            raise Exception("Enter the league age they are in digits")

        if len(age) == 2:
            present_age = int(age)

        if len(age) == 4:
            present_age = 2021 - int(age)

        if present_age <= 0:
            raise ValueError("You are not yet born")
        if present_age >= 100:
            raise ValueError("You seem to ve the oldest person alive")

        century = 100 - present_age

        print(f"After {century} years your will be crossing your 100 years :\n")

        further_year = input(
            "Optionally You can just Enter the year I can say your age in that particular year : \t"
        )
        if further_year == "":
            print("Okay as per your choice this will just optional :")
            break

        further_year = int(further_year) - 2021
        if further_year < 0:
            raise ValueError(f"{further_year} year had been passed sir :")

        present_age += further_year
        print(f"You will {present_age} years old in {further_year + 2021} ")
