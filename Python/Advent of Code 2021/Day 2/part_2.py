# Advent of code 2021 : Day 1 | Part 2

# Author = Abhinav
# Date = 2nd of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/2#part2)

# Solution : 

inputs = open("input.txt", "rt")
inputs = inputs.read().splitlines()
forward, depth, aim = 0, 0, 0

for _ in inputs:
    x = int(_[-1])
    if "forward" in _:
        forward += x
        depth += (aim * x)
    elif "up" in _:
        aim -= x
    elif "down" in _:
        aim += x

print(forward * depth)

# Answer : 2120734350
