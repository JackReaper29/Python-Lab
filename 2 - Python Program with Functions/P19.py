# Write a Python program to Find Armstrong Number in an Interval.

def arm(low,up):
    for n in range(low,up + 1):
        digits = len(str(n))
        temp = n
        add_sum = 0
        while temp != 0:
            k = temp % 10
            add_sum += k**digits
            temp = temp//10
        if add_sum == n:
            print(n)

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
arm(lower,upper)