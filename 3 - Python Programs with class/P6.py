# Write a Python Program to generate random number.

import random
class randomNum:
    def ran(self,a,b):
        # for printing single random number in the range
        c = random.randint(a,b)
        print(c)

        # for printing 10 random number in the range
        rand_list = []
        for i in range(0,10):
            n = random.randint(a,b)
            rand_list.append(n)
        print(rand_list)

m1 = randomNum()
x = int(input('Enter start range: '))
y = int(input('Enter end range: ')) 
m1.ran(x,y)