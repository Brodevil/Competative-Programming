# Competative Programming Question 150 = Two Characters (From HackerRank)

"""
Two Characters |

Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/two-characters/problem

And get the solution here, solved in python by me :}

"""

# Author = Abhinav
# Date = 9 January 2022
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/two-characters/problem)

# Solution :

def validate(inp):
    for i in range(len(inp)-1):
        if inp[i+1]==inp[i]:
            return False
    return True    
    

s_len = int(input())
s = input()

ans = 0
chtoindex = list()
for ch in set(s):
    chtoindex.append((ch, len([j for j, x in enumerate(s) if x == ch])))
    

for i, pack in enumerate(chtoindex[:-1]):
    char_i, lenchar_i = pack[0], pack[1]
    
    for j, otherpack in enumerate(chtoindex[i+1:]):
        char_j, lenchar_j = otherpack[0], otherpack[1]
        if abs(lenchar_i-lenchar_j)<2:
            c = [cha for cha in s if cha is char_i or cha is char_j]
            
            if validate(c):
                ans = max(ans, lenchar_j+lenchar_i)

print(ans)
