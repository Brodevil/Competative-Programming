# Competative Programming Question 155 = Two vs Ten (From CodeChef)

"""
Two vs Ten |

Get the Problem Statement on CodeChef : https://www.codechef.com/problems/TWOVSTEN

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 17 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [CodeChef](https://www.codechef.com/problems/TWOVSTEN)

# Solution :


for _ in range(int(input())):
    x = input()[-1]
    if x == "5":
        print(1)
    elif x == "0":
        print(0)
    else:
        print(-1)
