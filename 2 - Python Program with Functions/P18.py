# Write a Python program to Check Armstrong Number.

def Arm(n):
    digits = len(str(n))
    temp = n
    add_sum = 0
    while temp != 0:
        k = temp % 10
        add_sum += k**digits
        temp = temp//10
    if add_sum == n:
        print('Given number is an Armstrong Number')
    else:
        print('Given number is not a Armstrong Number')

number = int(input("Enter the number:\n"))
Arm(number)

