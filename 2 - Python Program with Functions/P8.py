# Write a Python program to convert C to F

def convert(a):
    f=(a*(9/5))+32
    print('\n',f,'F')

c=int(input('Enter the Temp in Cels - '))
convert(c)
