# Python practise 20 (From Hackerrank) = Finding the percentage

"""
Finding the precentage :


The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.


Example :

marks key : value parts are
'alpha':[20, 30, 40]
'beta':[30, 50, 70]

queary_name = "beta"
The query_name is 'beta'. beta's average score is (30 + 50 + 70)/3 = 50.0 .


Input Format :
The first line contains the integer n, the number of students' records. 
The next n lines contain the names and marks obtained by a student, each value separated by a space. 
The final line contains query_name, the name of a student to query.


Constraints :
- 2 < n <10
- 0 < marks[i] < 100
- length of marks arrays = 3


Output Format :
Print one line: The average of the marks obtained by the particular student correct to 
2 decimal places.


Sample Input 0 :
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika


Sample Output 0 :
56.00


Explanation 0 :
Marks for Malika are {52, 56, 60} whose average is 52 + 56 + 60 / 3 = 56


Sample Input 1 :
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh


Sample Output 1 :
26.50

"""

# Author = Abhinav
# Date = 25 April 2021
# Motive = Just for the python practise to not just learn python also to expert it

if __name__ == "__main__":
    student_marks = dict()
    for _ in range(int(input())):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))
    query_name = input()
    print(
        format(sum(student_marks[query_name]) / len(student_marks[query_name]), ".2f")
    )
