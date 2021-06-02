# Python practise 38 (From hackerrank) = The Minion Game = (https://www.hackerrank.com/challenges/the-minion-game/problem)

"""
The Minion Game :


Kevin and Stuart want to play the 'The Minion Game'.

Game Rules :
 - Both players are given the same string, S.
 - Both players have to make substrings using the letters of the string S.
 - Stuart has to make words starting with consonants.
 - Kevin has to make words starting with vowels.
 - The game ends when both players have made all possible substrings.



Scoring :
A player gets +1 point for each occurrence of the substring in the string S.


For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


For better understanding, see the image below:

For better understanding, see the image below:
Image = {https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png}




Your task is to determine the winner of the game and their score.



Function Description :
Complete the minion_game in the editor below.

minion_game has the following parameters:
 - string string: the string to analyze


Prints :
 - string: the winner's name and score, separated by a space on one line, or Draw if there is no winner


Input Format :-
A single line of input containing the string S.

Note: The string  will contain only uppercase letters: .



Constraints :-
0<len(S)<10**6



Sample Input :
BANANA


Sample Output :
Stuart 12


Note :
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
"""


# Author = Abhinav
# Date = 24 May 2021
# Purpose = Just for the python practise to not just learn python also to expert it


def minion_game(string):
    KevinResults = set()
    StuartResults = set()
    vowels = ["A", "E", "I", "O", "U"]

    for _ in range(len(string)):
        for i in range(len(string)):
            if i > _:
                queary = string[_:i]
                if string[_] in vowels:
                    KevinResults.add(queary)
                else:
                    StuartResults.add(queary)

    if len(KevinResults) > len(StuartResults):
        print(f"Kevin {len(KevinResults)}")
    else:
        print(f"Sturat {len(StuartResults)}")


if __name__ == '__main__':
    s = input()
    minion_game(s)
