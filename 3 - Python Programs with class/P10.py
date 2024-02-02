# Write a Python program to Check if a Number is Positive, Negative or Zero.

class PNZ:
    def check(self,n):
        if n>0:
            print("Number is Positive")
        elif n<0:
            print("Number is Negative")
        else:
            print("Number is ZERO")

m1 = PNZ()
num = float(input("Enter a Number:\n"))
m1.check(num)