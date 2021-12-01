# Advent of code 2021 : Day 1 | Part 1

# Author = Abhinav
# Date = 1st of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/1)

# Solution : 

from os import path


inputs = open("input.txt", "rt")
inputs = list(map(int, inputs.read().splitlines()))

print(sum([1 for _ in range(1, len(inputs)) if inputs[_-1] < inputs[_]]))

# Answer : 1266