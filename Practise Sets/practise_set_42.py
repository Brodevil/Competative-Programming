# Python practise 42 =  No Idea! (From HackerRank)  = (https://www.hackerrank.com/challenges/no-idea/problem)


"""
No Idea! 


There is an array of N integers. There are also 2 disjoint sets, A and B, each containing M integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i belongs to A, you add 1 to your happiness. 
If i belongs to b, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.


Constraints :
1 <= n <= 10**5
1 <= m <= 10**5
1 <=  any integer as a input  <=  10**5



Input Format :

 - The first line contains integers n and m separated by a space.
 - The second line contains n integers, the elements of the array.
 - The third and fourth lines contain m integers, A and B, respectively.



Output Format :
Output a single integer, your total happiness.



Sample Input :

3 2
1 5 3
3 1
5 7


Sample Output :
1



Explanation

You gain  unit of happiness for elements 3 and 1 in set A. 
You lose 1 unit for 5 in set B. 
The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1 = 1.


"""


# Author = Abhinav
# Date = June 13 2021
# Source = (https://www.hackerrank.com/challenges/no-idea/problem)
# Pourpose = Just for python practicing will lots of dedications


if __name__ == "__main__":
    _ = input()
    array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    happiness = 0

    for _ in array:
        if _ in A:
            happiness += 1
        elif _ in B:
            happiness -= 1

    print(happiness)

