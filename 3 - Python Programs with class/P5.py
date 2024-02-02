# Write a Python Program to swap two variable.

class swap:
    def init(self,a,b):
        temp=a
        a=b
        b=temp
        print('\nSwaped values are :\n x = ',a,'\ny = ',b)

m1 = swap()
x=input('Enter x = ')
y=input('Enter y = ')
m1.init(x,y)