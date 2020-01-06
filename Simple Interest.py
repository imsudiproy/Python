'''
Program to calculate simple interest
program by- Sudip Roy
Company- SR group
'''

#Defining variables:
p=float(input("Enter amount: "))
r=float(input("Enter rate: "))
t=float(input("Enter time: "))

#function to calculate simple interest
def simpleInterest():
    SI=(p*r*t)/100
    return SI

#function calling
print("Simple interest is: ", simpleInterest())