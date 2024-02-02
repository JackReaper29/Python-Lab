# Write a Python program to Find Armstrong Number in an Interval.

class ArmIntervel():
    def arm(self,low,up):
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

m1 = ArmIntervel()
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
m1.arm(lower,upper)