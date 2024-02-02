# Write a Python program to print all Prime Numbers in an Interval.

def prime(a,b):
    print("The Prime Number in the Range are :- \n")
    for n in range(a,b+1):
        if n>1:
            for i in range(2,n):
                if(n%i)==0:
                    break
            else:
                print(n)

lower_value = int(input("Enter lower Range :- \n"))
upper_value = int(input("Enter Uppet Range :- \n"))
prime(lower_value,upper_value)