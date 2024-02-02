# Write a Python program to Display the multiplication Table.

class tables:
    def table(self,n):
        for i in range(1,11):
            print(n,"x",i,"=",n*i)

m1 = tables()
num = int(input("Enter the Number for Multiplication Table :-\n"))
m1.table(num)