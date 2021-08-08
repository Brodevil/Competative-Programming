# Python Practise 65 = Cats and a Mouss (From hackerrank) 


"""
Cats and a Mouse | Problem Statment :


Get the Problem Statment on Hackerrank : https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

And get the solved solution in python by Brodevil here :|

"""

# Author = Abhinav
# Date = 7 August 2021
# Pourpose = Just for practise and imporving skills
# Source =   https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

# Solution :

# Complete the catAndMouse function below.


def catAndMouse(x: int, y: int, z: int):
    catA = abs(x-z)
    catB = abs(y-z)
    
    if catA < catB:
        return "Cat A"
    elif catA > catB:
        return "Cat B"
    elif catA == catB:
        return "Mouse C"
    


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)
