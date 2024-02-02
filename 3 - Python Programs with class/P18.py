# Write a Python program to Check Armstrong Number.

class Armstrong:
    def Arm(self,n):
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

m1 = Armstrong()
number = int(input("Enter the number:\n"))
m1.Arm(number)

