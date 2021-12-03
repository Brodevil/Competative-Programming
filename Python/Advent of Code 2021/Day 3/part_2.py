# Advent of code 2021 : Day 3 | Part 2

# Author = Abhinav
# Date = 3rd of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/3#part2)

# Solution :


inputs = open("input.txt", "r")
inputs = inputs.read().splitlines()


A = list(inputs)
B = list(inputs)

for i in range(len(inputs[0])):
    if len(A) > 1:
        a0 = len([x for x in A if x[i] == '0'])
        a1 = len([x for x in A if x[i] == '1'])
        if a1 >= a0:
            A = [x for x in A if x[i] == '1']
        else:
            A = [x for x in A if x[i] == '0']
    
    if len(B) > 1:
        b0 = len([x for x in B if x[i] == '0'])
        b1 = len([x for x in B if x[i] == '1'])
        if b1 >= b0:
            B = [x for x in B if x[i] == '0']
        else:
            B = [x for x in B if x[i] == '1']

print(int(A[0], 2) * int(B[0], 2))

# Answer : 6124992
