'''
Python program to calculate Armstrong number
Program by- Sudip Roy
Company- SR Group
'''

#calculating number of digits
n=int(input("Enter the number: "))
count=0
while(n>0):
    n=n//10
    count=count+1
print("Number of digits: ",count)