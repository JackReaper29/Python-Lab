# Write a Python program to Display the multiplication Table.

def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

num = int(input("Enter the Number for Multiplication Table :-\n"))
table(num)