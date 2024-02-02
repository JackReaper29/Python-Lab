# Write a Python Program to swap two variable.

def swap(a,b):
    temp=a
    a=b
    b=temp
    print('\nSwaped values are :\n x = ',a,'\ny = ',b)

x=input('Enter x = ')
y=input('Enter y = ')
swap(x,y)