# Write a Python program to Find the Sum of Natural Numbers.

class SumNaturalNumber():
    def sum(self,n):
        if n < 0:
            print("Enter a positive number")
        else:
            sum = 0
            while(n > 0):
                sum += n
                n -= 1
            print("The sum is",sum)

m1 = SumNaturalNumber()
num = int(input("Enter a number: "))
m1.sum(num)

#Can write above program in one line as below:-
#print("Sum of N natural numbers is:", (lambda n: n*(n+1)/2)(int(input("Enter a number: "))))