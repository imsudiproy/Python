'''
Topic- Find nth fibonacci number
Program by- Sudip Roy
Company- SR Group
'''

#Function to calculate the value
def fabnum(n):
    if n>0:
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            return (fabnum(n-1) + fabnum(n-2))
    else:
        print("Can't be a negative number!!")

#Calling and printing the value
n=int(input("Enter the number: "))
print("the value of {0}th fibonacci number is {1}".format(n,fabnum(n)))