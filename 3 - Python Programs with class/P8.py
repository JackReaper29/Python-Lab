# Write a Python program to convert C to F

class C_to_F:
    def convert(self,a):
        f=(a*(9/5))+32
        print('\n',f,'F')


m1 = C_to_F()
c=int(input('Enter the Temp in Cels - '))
m1.convert(c)
