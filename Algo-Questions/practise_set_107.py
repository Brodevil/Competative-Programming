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
    for _ in range(int(input())):
        n, c, m = map(int, input().split())
        wrapper = [n // c]
        remains = list()
        while wrapper[-1] > 1:
            if (wrapper[-1] / m) % 1 == 0:
                temp = ((wrapper[-1] + sum(remains)) % m) 
                if temp == 0:
                    del remains[:]
                    wrapper.append(temp)
                else:
                    wrapper.append((wrapper[-1] )// m)
                    
            else:
                remains.append(wrapper[-1] % m)
                wrapper.append(wrapper[-1]//m) 
        
        print(wrapper, remains)

