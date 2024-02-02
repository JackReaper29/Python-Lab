# Write a Python program to display calendar.

import calendar
class cal:
    def init(self,y,m):
        print(calendar.month(yy,mm))


m1 = cal()
yy = int(input("Enter year: "))  
mm = int(input("Enter month: ")) 
m1.init(yy,mm)
