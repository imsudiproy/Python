'''
Program to calculate Compound Interest
Program by- Sudip Roy
Company- SR Group
'''

"""
Compound Interest= p*(1+ (r/100))^T
Where
P= Principle amount
r= rate
T=Time
"""
p=float(input("Enter Principle amount: "))
r=float(input("Enter rate: "))
t=float(input("Enter time: "))
CI=p*(pow((1+(r/100)),t))
print("Compound interest is: ", CI)
