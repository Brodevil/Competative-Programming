# Advent of code 2021 : Day 1 | Part 2

# Author = Abhinav
# Date = 1st of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/1)

# Solution : 

inputs = open("input.txt", "rt")
inputs = list(map(int, inputs.read().splitlines()))

increased = 0
cum_depths = [sum(inputs[i:i+3]) for i in range(len(inputs) - 2)]
for i in range(len(cum_depths) - 1):
    if cum_depths[i + 1] > cum_depths[i]:
        increased += 1

print(increased)

# Answer : 1217
