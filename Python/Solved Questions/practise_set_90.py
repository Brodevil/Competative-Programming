# Algorithm Question 90  =  ACM ICPC Team (From HackerRank)

"""
ACM ICPC Team |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/acm-icpc-team/problem

And get the solved solution in python by Brodevil, here :|

"""

# Author = Abhinav
# Date = 5 September 2021
# Pourpose = Just for practise and imporving skills
# Source =  [Hackerrank](https://www.hackerrank.com/challenges/acm-icpc-team/problem)


# Solution :

line = input().split()
n = int(line[0])
m = int(line[1])

people = [input() for i in range(n)]
skills = []
max_skills = 0

for i in range(len(people)):
    j = i
    while j < n:
        first_person = people[i]
        second_person = people[j]

        skill = bin(int(first_person, 2) | int(second_person, 2))[2:].count("1")
        if skill > max_skills:
            max_skills = skill
        skills.append(str(skill))

        j += 1

print(max_skills)
print(skills.count(str(max_skills)))
