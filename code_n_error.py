# import string

# alphabet_string = string.ascii_lowercase
# # Create a string of all lowercase letters
# print(alphabet_string)


# import sys
# sys.exit()
# print("I this printing or not")

dictionary = {
    "Abhinav": 20,
    "sivam": 21,
    "kharade": 30,
    "harsh": 12
}

dictionary = {dictionary[key]: key for key in dictionary}
print(dictionary)
