# Write a Python program to Find the Sum of Natural Numbers.

def sum(n):
    if n < 0:
        print("Enter a positive number")
    else:
        sum = 0
        while(n > 0):
            sum += n
            n -= 1
        print("The sum is",sum)

num = int(input("Enter a number: "))
sum(num)