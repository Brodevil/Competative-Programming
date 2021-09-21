# Algorithm Question 106  =  The Time in Words (From HackerRank)

"""
The Time in Words |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/the-time-in-words/problem

And get the solved soulution in python, here :|

"""

# Author = Abhinav
# Date = 19 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/the-time-in-words/problem)

# Solution :

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

def n2w(n: int) -> int:
    try:
        return num2words[n].lower()
    except KeyError:
        try:
            return num2words[n-n%10] + " " + num2words[n%10].lower()
        except KeyError:
            pass


def timeInWords(h: int, m: int) -> int:
    ho = n2w(h)
    if m == 0:
        return f"{ho} o' clock"
    elif m == 15:
        return f"quarter past {ho}"
    elif m == 30:
        return f"half past {ho}"
    elif m == 45:
        return f"quarter to {n2w(h+1)}"
    elif m < 30:
        if m == 1:
            m = n2w(m).lower()
            return f"{m} minute past {ho}"
        else:
            m = n2w(m).lower()
            return f"{m} minutes past {ho}"

    elif m > 30:
        if m != 1:
            m = n2w(60-m).lower()
            return f"{m} minutes to {n2w(h+1)}"
        else:
            m = n2w(60-m).lower()
            return f"{m} minute to {n2w(h+1)}"


if __name__ == '__main__':
    h, m = int(input()), int(input())
    result = timeInWords(h, m)
    print(result)
