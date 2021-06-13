# Python practise problem 2(Easy, 10 points)
"""
Divide The apples

Abhinav had get n numbers of apples. Abhinav has students among whom, he want to distributes the apples. 
These n number of apples are provided to Abhinav by his friends and he can request for few more or few less apples.

You need to print whether a number is range mn to mx is divisor of n or not.

Imput:
Take input n, mn and mx from the user

Output:
Print whether the number between mn and mx are divisor of n or not. If mn=mx,show that this is not a range and mn is equal to mx.
Show the result of the number


Example :
if n is 20 and mn = 2 and mx = 5

2 is divisor of 20
3 is not divisor of 20
4 is divisor of 20
5 is divisor of 20

"""
try:
    n = int(input("Enter the number of apple Abhinav got :\n"))
    mn = int(input("Enter the first number of range minimul value  : \n"))
    mx = int(input("Enter the second number of the range maximum value: \n"))
except ValueError:
    print("Plz enter the league input ")
    exit()

if mn == mx:
    print("This is nor a range and minimul and maximum : ")
    exit()
    
if mn > mx:
    print("Not a expected range okay, minimal is greater then maximum it should be small then maximum range : ")
    exit()

for i in range(mn, mx+1):
    if n % i == 0:
        print(f"{i} is divisor of {n}")
    else:
        print(f"{i} is not divisor of {n}")
