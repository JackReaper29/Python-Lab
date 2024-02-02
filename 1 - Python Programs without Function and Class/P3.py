# Find the Area of the tringle.

x=int(input('Enter the length of 1st side - '))
y=int(input('Enter the length of 2nd side - '))
z=int(input('Enter the length of 3rd side - '))

s=(x+y+z)/2
Ar=(s*(s-x)*(s-y)*(s-z))**0.5
print("\nArea of the Trinagle is ",Ar)