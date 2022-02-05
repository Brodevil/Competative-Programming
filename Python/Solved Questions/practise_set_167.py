# Competative Programming Question 165 = L Shaped Plots (From Google KickStart 2021 Round A)

"""
L Shaped Plots |

Get the Problem Statement on CodeForces : https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 5 February 2022
# Pourpose = Just for practise and imporving skills
# Source =  [Google KickStart 2021 Round A](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509)

# Solution :

for _ in range(int(input())):
    x, y = map(int, input().split())
    matrix = list()
    l_shape = 0

    for _ in range(x):
        arr = list(map(int, input().split()))
        matrix.append(arr)

    print(matrix)
