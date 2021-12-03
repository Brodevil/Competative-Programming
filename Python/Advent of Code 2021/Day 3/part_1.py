# Advent of code 2021 : Day 3 | Part 1

# Author = Abhinav
# Date = 3rd of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/3)

# Solution : 

inputs = open("input.txt", "rt")
inputs = inputs.read().splitlines()

gamma, epsilon = "", ""

for i in range(len(inputs[0])): 
    s = ''.join([_[i] for _ in inputs])
    _0, _1 = s.count("1"), s.count("0")
    if _0 > _1:
        gamma += "0"
        epsilon += "1"
    elif _1 > _0:
        gamma += "1"
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))


# Answer : 1071734
