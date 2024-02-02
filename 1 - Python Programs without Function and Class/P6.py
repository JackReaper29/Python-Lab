# Write a Python Program to generate random number.

import random
a = int(input('Enter start range: '))
b = int(input('Enter end range: ')) 
c = random.randint(a,b)
print(c)
rand_list = []
for i in range(0,10):
    n = random.randint(a,b)
    rand_list.append(n)
print(rand_list)