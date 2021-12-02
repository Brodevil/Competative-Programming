# Advent of code 2021 : Day 2 | Part 1

# Author = Abhinav
# Date = 2nd of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/2)

# Solution : 

inputs = open("input.txt", "rt")
inputs = inputs.read().splitlines()
forward, depth = 0, 0

for _ in inputs:
    x = int(_[-1])
    if "forward" in _:
        forward += x
    elif "down" in _:
        depth += x
    elif "up" in _:
        depth -= x

print(forward * depth)

# Answer : 1893605
