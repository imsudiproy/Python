'''
Find all Prime numbers in a range
Program by- Sudip Roy
Company- SR Group
'''

count=0
print("Enter the range of number: ")
a=int(input("Enter lower limit: "))
b=int(input("Enter upper limit: "))
for i in range(a,b):
    for j in range(2,i):
        if (i%j)==0:
            count=count+1
    if(count==0):
        print(i)
    count=0