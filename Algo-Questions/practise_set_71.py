# Python Practise 71 =  Utopian Tree (From Hackerrank)

"""
Utopian Tree | Problem Statement :


Get the Problem Statement on hackerrank : https://www.hackerrank.com/challenges/utopian-tree/problem

And get the solved solution in python by brodevil here :|


"""

# Author = Abhinav
# Date = 14 August 2021
# Pourpose = Just for practise and imporving python skills
# Source = [HackerRank](https://www.hackerrank.com/challenges/utopian-tree/problem)


# Solution :


def utopianTree(n: int) -> int:
    height = 1
    for _ in range(n):
        if _ % 2 == 0:
            height = height * 2
        else:
            height += 1
    
    return height


if __name__ == '__main__':
    # t = int(input().strip())

    # for t_itr in range(t):
    n = int(input().strip())

    result = utopianTree(n)

    print(result)
