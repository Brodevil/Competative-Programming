# Algorithm Question 129 =  Highest Value Palindrome (From HakerRank)

"""
Highest Value Palindrome |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/richie-rich/problem

And get the solution, solved by me, here :}

"""

# Author = Abhinav
# Date = 26 October 2021
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/richie-rich/problem)

# Solution :

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input()
    
    left = list(s[:n//2])
    right = list(s[n//2+1:][::-1]) if n % 2 == 1 else list(s[n//2:][::-1])
    remainingCount = k
    difference = 0
    length = len(left)
    for i in range(length):
        if(left[i] != right[i]):
            difference += 1

    for i in range(length):
        x = left[i]
        y = right[i]
        if(x == y):
            if(x == '9'):
                continue
            elif(remainingCount-2 >= (difference)):
                left[i] = '9'
                right[i] = '9'
                remainingCount -= 2
        elif(x != y):
            if(x == '9'):
                if(remainingCount-1 >= (difference-1)):
                    right[i] = '9'
                    difference -= 1
                    remainingCount -= 1
                else:
                    print(-1)
            
            elif(y == '9'):
                if(remainingCount-1 >= (difference-1)):
                    left[i] = '9'
                    difference -= 1
                    remainingCount -= 1
                else:
                    print(-1)
            else:
                if(remainingCount-2 >= (difference-1)):
                    left[i] = '9'
                    right[i] = '9'
                    difference -= 1
                    remainingCount -= 2
                elif(remainingCount-1 >= (difference-1)):
                    if(x > y):
                        right[i] = left[i]
                    else:
                        left[i] = right[i]
                    difference -= 1
                    remainingCount -= 1
                else:
                    print(-1)
    if n % 2 == 0:
        ans = "".join(left + (right[::-1]))
    if n % 2 == 1:
        mid = ['9'] if(remainingCount > 0) else [s[n//2]]
        ans = "".join(left + mid + (right[::-1]))
    
    print(ans)
