# Practise set 3 - Foods and Calories
"""
You visit a resturant called Dance with Devil and food items in this resturant are sorted based on their amount of calories.
You have to reverse this list of food items and their calories

You have to use following three methods to reverse this list :

    - Inbuilt method of python
    - Listname[::-1] slicing tricks
    - Swapping first element with last one and second with second last one so on...


Input:
Take a list as an input from the user

Output :
[3, 2, 1]
[3, 2, 1]
[3, 2, 1]
All the three method give same results

Example :
[2, 4, 6]   # got input

>>> [6, 4, 2]
>>> [6, 4, 2]
>>> [6, 4, 2]

All the three method give same results

"""

lst = list(input().split())


# by usering inbuild method of list
result_1 = lst.copy()
result_1.reverse()

# by using list clicing method
result_2 = lst[::-1]

# by using poping method from last to first
resutl_3 = lst.copy()


for index, element in enumerate(resutl_3):
    if len(resutl_3)/2 == index:
        break
    elif len(resutl_3)//2 == index:
        break
    from_last = resutl_3[len(lst)-1-index]
    resutl_3[len(lst)-1-index] = element
    resutl_3[index] = from_last
    print(resutl_3)

print(result_1)
print(result_2)
print(resutl_3)
if resutl_3 == result_1 == result_2:
    print("All the three method give same results")
