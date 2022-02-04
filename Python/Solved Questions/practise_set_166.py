# Competative Programming Question 165 = K-Goodness String (5pts, 7pts) (From Google KickStart 2021 Round A)

"""
K-Goodness String (5pts, 7pts) |

Get the Problem Statement on CodeForces : https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 3 February 2022
# Pourpose = Just for practise and imporving skills
# Source =  [Google KickStart 2021 Round A](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3)

# Solution :

for i in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    score = 0

    for _ in range(n//2):
        if s[_] != s[n-_-1]:
            score += 1

    print(f"Case #{i+1}: {abs(score-k)}")
