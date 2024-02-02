# Write a Python program to Check if a Number is Positive, Negative or Zero.

def check(n):
    if n>0:
        print("Number is Positive")
    elif n<0:
        print("Number is Negative")
    else:
        print("Number is ZERO")

num = float(input("Enter a Numbert:\n"))
check(num)