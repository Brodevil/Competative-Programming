# Algorithm Practise 107  =   Chocolate Feast (HackerRank)

"""
Chocolate Feast |


Get the problem Statement on HackerRank : https://www.hackerrank.com/challenges/chocolate-feast/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 21 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/chocolate-feast/problem)

# Solution :


if __name__ == "__main__":
    # for _ in range(int(input())):
    n, c, m = map(int, input().split())
    wrapper = [n // c]
    remains = (wrapper[-1]) % m
    while wrapper[-1] > 1 or remains > 0:
        print(wrapper, wrapper[-1], remains, m)

        remains = (wrapper[-1] + remains) % m
        wrapper.append((wrapper[-1] + remains) // m)        

    print(wrapper, sum(wrapper))
