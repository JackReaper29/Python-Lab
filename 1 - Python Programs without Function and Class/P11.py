# Python program to check if the input number is odd or even.


n = int(input("Enter a number:\n"))
if(n % 2 == 0):
    print("Number {0} is even".format(n))
else:
    print("Number {0} is odd".format(n))