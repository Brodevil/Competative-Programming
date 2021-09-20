# Algorithm Question 106  =  The Time in Words (From HackerRank)

"""
The Time in Words |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/the-time-in-words/problem

And get the solved soulution in python, here :|

"""

# Author = Abhinav
# Date = 19 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/halloween-sale/problem)

# Solution :

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

def n2w(n):
    try:
        return num2words[n]
    except KeyError:
        try:
            return num2words[n-n%10] + num2words[n%10].lower()
        except KeyError:
            pass


def timeInWords(h: int, m: int) -> int:
    return 0


if __name__ == '__main__':
    h, m = int(input()), int(input())
    result = timeInWords(h, m)
    print(result)
