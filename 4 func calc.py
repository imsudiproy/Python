'''
Four function calculator using python
Program by- Sudip Roy
'''

print("FOUR FUNCTION CALCULATOR ")
print("Operations: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
n=int(input("Select your operation (1-4): "))
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if(n==1):
    print("Result=",a+b)
elif(n==2):
    print("Result= ",a-b)
elif(n==3):
    print("Result= ",a*b)
elif(n==4):
    print("Result= ",round(a/b,2))
else:
   print("Wrong Input!! ")