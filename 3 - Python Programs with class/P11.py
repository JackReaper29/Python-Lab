# Python program to check if the input number is odd or even.

class oddeven:
    def odd_even(self,n):
        if(n%2==0):
            print("Number {0} is even".format(n))
        else:
            print("Number {0} is odd".format(n))

m1 = oddeven()
num = int(input("Enter a number:\n"))
m1.odd_even(num)