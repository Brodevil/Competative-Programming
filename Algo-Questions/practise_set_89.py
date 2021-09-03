# Algorith Question 89  =  Queen's Attack II  (From HackerRank)

"""
Queen's Attack II |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/queens-attack-2/problem

And get the solved solution in python By Brodevil, here :|

"""

# Author = Abhinav
# Date = 2 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/equality-in-a-array/problem)


# Solution :

# Complete the 'queensAttack' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles


def queensAttack(n: int, k: int,
                 r_q: int, c_q: int, 
                 obstacles: list) -> int:
    # Write your code here
    return 0


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
