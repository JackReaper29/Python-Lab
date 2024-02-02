# Write a Python program to convert Kilometer into miles.

class KM_to_mm:
    def convert(self,a):
        a=a*0.621371
        print('\n',a,'miles')

m1 = KM_to_mm()
x=int(input('Enter the distance in Kilometer - '))
m1.convert(x)