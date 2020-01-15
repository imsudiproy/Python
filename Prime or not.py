'''
Program to find whether a number is prime or not
Program by- Sudip Roy
Company- SR Group
'''

n=int(input("Enter the number: "))
count=0

for i in range(2,n):
    if(n%i)==0:
        count=count+1
if n>1:
    if(count>=1):
        print("Not a prime number ")
    else:
        print("Prime Number!! ")
else:
    print("Not a prime number.")