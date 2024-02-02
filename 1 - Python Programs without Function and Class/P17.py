# Write a Python Program to Print Fibonacci Series.

n = int(input("Enter the Number:-\n"))
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if n <= 0:
    print("Please Enter the Positive Number.")
# if there is only one term, return n1
elif n == 1:
    print("Fibonacci Sequence of numbers up to",n,":")
    print(n1)
# generate fibonacci sequence
else:
    print("The Fibonacci Sequence of Numbers is :- ")
    while count < n:
        print(n1)
        fibo = n1 + n2
        # Update Values
        n1 = n2
        n2 = fibo
        count += 1
