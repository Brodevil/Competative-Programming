# Algorith Question 89  =  Queen's Attack II  (From HackerRank)

"""
Queen's Attack II |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/queens-attack-2/problem

And get the solved solution in python By Brodevil, here :|

"""

# Author = Abhinav
# Date = 3 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/queens-attack-2/problem)


# Solution :

# Complete the 'queensAttack' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles


def queensAttack(n: int, k: int, r_q: int, c_q: int, obstacles: list) -> int:
    # Write your code here
    attack = 0

    # Rows Downwards
    for _ in range(r_q - 1, 0, -1):
        if [_, c_q] not in obstacles and _ != 0:
            attack += 1
        else:
            break

    # Rows Upwards
    for _ in range(r_q, n):
        if [_, c_q] not in obstacles and _ != 0:
            attack += 1
        else:
            break

    # Columns Downwards
    for _ in range(c_q - 1, 0, -1):
        if [r_q, _] not in obstacles and _ != 0:
            attack += 1
        else:
            break

    # Columns Upwards
    for _ in range(c_q, n):
        if [r_q, _] not in obstacles and _ != 0:
            attack += 1
        else:
            break

    # Horizontally Right - dowwards
    position = [r_q, c_q]
    while position not in obstacles:
        position = [position[0] - 1, position[1] - 1]
        attack += 1
        if 1 in position or n in position:
            break

    # Horizontally Right - upwards
    position = [r_q, c_q]
    while position not in obstacles:
        position = [position[0] + 1, position[1] + 1]
        attack += 1
        if 1 in position or n in position:
            break

    # Horizontally Left - dowwards
    position = [r_q, c_q]
    while position not in obstacles:
        position = [position[0] + 1, position[1] - 1]
        attack += 1
        if 1 in position or n in position:
            break

    # Horizontally Left - upwards
    position = [r_q, c_q]
    while position not in obstacles:
        position = [position[0] - 1, position[1] + 1]
        attack += 1
        if 1 in position or n in position:
            break

    return attack


if __name__ == "__main__":
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
