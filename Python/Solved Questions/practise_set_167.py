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

def count(g):
    h, w = len(g), len(g[0])

    d, u = [[0] * w for _ in range(h)], [[0] * w for _ in range(h)]
    r, l = [[0] * w for _ in range(h)], [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            d[i][j] = (g[i][j] + d[i - 1][j] if g[i][j] else 0) if i else g[i][j]
            r[i][j] = (g[i][j] + r[i][j - 1] if g[i][j] else 0) if j else g[i][j]
            u[-1 - i][j] = (g[-1 - i][j] + u[-i][j] if g[-1 - i][j] else 0) if i else g[-1 - i][j]
            l[i][-1 - j] = (g[i][-1 - j] + l[i][-j] if g[i][-1 - j] else 0) if j else g[i][-1 - j]
    result = 0
    
    for i in range(h):
        for j in range(w):
            result += max(0, min(d[i][j], r[i][j] // 2) + min(d[i][j] // 2, r[i][j]) - 2)
            result += max(0, min(d[i][j], l[i][j] // 2) + min(d[i][j] // 2, l[i][j]) - 2)
            result += max(0, min(u[i][j], r[i][j] // 2) + min(u[i][j] // 2, r[i][j]) - 2)
            result += max(0, min(u[i][j], l[i][j] // 2) + min(u[i][j] // 2, l[i][j]) - 2)
    
    return result


if __name__ == '__main__':
    for _ in range(int(input())):
        r, c = map(int, input().split())
        grid = [list(map(int, input().split()) for _ in range(r)]
        print(f'Case #{_ + 1}: {count(grid)}')
