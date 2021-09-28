# Algorithm Question 109  =  Lisa's Workbook (From HackerRank)

"""
Lisa's Workbook |


Get the Problem Statement on HackerRank : https://www.hackerrank.com/challenges/lisa-workbook/problem

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 24 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [HackerRank](https://www.hackerrank.com/challenges/lisa-workbook/problem)

# Solution :


def lisas_workbook(n: int, k: int, a: list) -> int:
    num_special = 0
    cur_page = 1

    for i in range(len(a)):
        num_probs_in_chapter = a[i]
        num_full_pages, leftover_probs = divmod(num_probs_in_chapter, k)

        total_pages = num_full_pages + ( 1 if leftover_probs else 0 )
        problems_in_chapter = iter(range(1, a[i]+1))

        for _ in range(total_pages):
            probs_on_page = [next(problems_in_chapter, None) for _ in range(k)]    
            if cur_page in probs_on_page:
                num_special += 1
            cur_page += 1        
    
    return num_special


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(lisas_workbook(n, k, arr))
