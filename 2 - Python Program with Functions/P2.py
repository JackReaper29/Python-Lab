# Demostrate different mathematical functions.

def add(a,b):
    c=a+b
    print('Addition is',c)


def sub(a,b):
    c=a-b
    print('Subtraction is',c)

def mul(a,b):
    c=a*b
    print('Multiplication is',c)

def div(a,b):
    c=a/b
    print('Division is',c)

def divf(a,b):
    c=a//b
    print('Division Floor is',c)

def mod(a,b):
    c=a%b
    print('Modolus is',c)

def powe(a,b):
    c=a**b
    print('Power is',c)

x=int(input('Enter the 1st Number - '))
y=int(input('Enter the 2nd Number - '))
add(x,y)
sub(x,y)
mul(x,y)
div(x,y)
divf(x,y)
mod(x,y)
powe(x,y)