'''
Topic- To check a number is perfect square or not
Program by- Sudip Roy
Company- SR Group
'''

import math

def perfect_sq(x):
    s=int(math.sqrt(x))
    return s*s==x

x=int(input("Enter the number: "))
print(perfect_sq(x))