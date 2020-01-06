'''
Program to calculate area of a circle
program by- Sudip Roy
Company- SR group
'''

PI=3.14
r=float(input("Enter the radius of the circle: "))

#function to calculate area
def findArea():
    area=PI*(r*r)
    return area

#function to calculate circumference
def findCer():
    cir=2*PI*r
    return cir

#driver method
print("Area and Circumference calculator: ")
print("1. Circumference     2. Area     3.Print Both ")
choice=int(input("Your choice: "))
if(choice==1):
    print(" Circumference is: ",findCer())
elif(choice==2):
    print("Area is: ", findArea())
elif(choice==3):
    print("Circumference is: ", findCer())
    print("Area is: ", findArea())
else:
    print("Wrong Input")