# Write a Python program to Check Leap Year.
  
y = int(input("Enter the Year:\n"))
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(y,"is a Leap Year")
else:
    print(y,"is not a Leap Year")

