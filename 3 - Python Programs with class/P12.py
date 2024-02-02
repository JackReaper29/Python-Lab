# Write a Python program to Check Leap Year.

class leapyear:
    def leap_year(self,y):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            print(y,"is a Leap Year")
        else:
            print(y,"is not a Leap Year")

m1 = leapyear()
year = int(input("Enter the Year:\n"))
m1.leap_year(year)