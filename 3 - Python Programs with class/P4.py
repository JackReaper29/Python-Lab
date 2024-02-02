# Write a Python program to solve Quadritic Equation.

import math
class Quadritic:
    def Quad(self,a,b,c):
        d=(b**2)-(4*a*c)
        sqtval = math.sqrt(abs(d))
        if d > 0:
            print("Real and Different Roots\n")
            print((-b+sqtval)/(2*a))
            print((-b-sqtval)/(2*a))
        elif d == 0:
            print("Real and Same Roots\n")
            print(-b/(2*a))
        else:
            print("Complex Roots\n")
            print(-b/(2*a),"+i",sqtval)
            print(-b/(2*a),"-i",sqtval)


m1 = Quadritic()
x=int(input('Enter the 1st Number - '))
y=int(input('Enter the 2nd Number - '))
z=int(input('Enter the 3rd Number - '))
m1.Quad(x,y,z)