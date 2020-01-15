'''
Topic- Sum of square of first n natural number
Program by- Sudip Roy
Company- SR Group
'''

n=int(input("Enter the number: "))
sm=0
for i in range (1, n+1):
    sm=sm+(i*i)
print(sm)