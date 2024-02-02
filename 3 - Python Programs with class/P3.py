# Find the Area of the tringle.

class tringle:
    def Area(self,a,b,c):
        s=(a+b+c)/2
        Ar = (s*(s-a)*(s-b)*(s-c))**0.5
        print("\nArea of the Triangle is ",Ar)


m1 = tringle()
x=int(input('Enter the length of 1st side - '))
y=int(input('Enter the length of 2nd side - '))
z=int(input('Enter the length of 3rd side - '))

m1.Area(x,y,z)