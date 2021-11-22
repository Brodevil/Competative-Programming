# Algorith Question 75 =  Save the Prisoner! (From Hackerrank)

"""
Save the Prisoner! | Problem Statement :


Get the Problem Statment on HackerRank : https://www.hackerrank.com/challenges/save-the-prisoner/problem

And get the solved solution in python by Brodevil here :|


"""

# Author = Abhinav
# Date = 20 August 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrnak](https://www.hackerrank.com/challenges/save-the-prisoner/problem)


# Solution :

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s


def saveThePrisoner(prisoners: int, candy: int, chair: int) -> int:
    # for _ in range(candy):
    #     if _ != 0:
    #         chair += 1
    #     if chair > prisoners:
    #         chair = 1
        
    # return chair

    # another quick solution :
    return ((chair - 1 + candy - 1) % prisoners) + 1


if __name__ == '__main__':
    for t_itr in range(int(input())):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        print(result)
