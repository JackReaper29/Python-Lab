# Write a Python program to Check Prime Number.

class prime:
    def prime(self,n):
        if(n>1):
            # loop to check if n is divisible by any number from 2 to n/2
            for i in range(2,int(n/2)+1):
                if(n % i == 0):
                    print(n, "is not a prime number")
                    break
            else:
                print(n, "is a prime number")
        else:
            print("Enter a number greater than 1")

m1 = prime()
num = int(input("Enter a Number:\n"))
m1.prime(num)