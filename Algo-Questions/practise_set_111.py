# Algorithm Question 111 =  A. Casimir's String Solitaire (From CodeForces)

"""
A. Casimir's String Solitaire |


Get the Problem Statement on CodeForces : https://codeforces.com/problemset/problem/1579/A

And get the solved solution in python, here :|

"""

# Author = Abhinav
# Date = 29 September 2021 
# Pourpose = Just for practise and imporving skills
# Source =  [CodeForces](https://codeforces.com/problemset/problem/1579/A)

# Solution :

for s in[*open(0)][2::2]:
    r=[];i=0
    for x in sorted(a:=s.split(),key=int):j=a.index(x,i)+1;a[i:j]=a[j-1:j]+a[i:j-1];r+=[i:=i+1,j,j-i]*(j>i)
    print(len(r)//3,*r)
