# Advent of code 2021 : Day 4 | Part 2

# Author = Abhinav
# Date = 4th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/4)

# Solution :

import re

with open("input.txt", "rt") as f:
    nums = list(f.read().rstrip().split('\n\n'))

comp = list(map(int, nums[0].split(',')))
suml, ll = list(), list()
for i in range(1, len(nums)):
    lol = map(lambda x: re.split(
        '  | ', x.lstrip(" ")), nums[i].split('\n'))
    lol1 = [[int(k) for k in j] for j in lol]
    lol2 = list(map(list, zip(*lol1)))
    lol = lol1+lol2
    ll.append(lol)
    suml.append(sum([sum(j) for j in lol1]))

flag, check, marked = 0, [], [0]*len(ll)

for k in range(len(comp)):
    check.append(comp[k])
    for ind, m in enumerate(ll):
        for j in m:
            if all(x in check for x in j):
                flat_m = [item for sublist in m for item in sublist]
                ans = (
                    suml[ind]-sum(set(flat_m).intersection(check)))*check[-1]
                marked[ind] = -1
                if len(set(marked)) == 1:
                    print(ans)
                    flag = 1
                    break
        if flag == 1:
            break
    if flag == 1:
        break


# Answer : 8468
