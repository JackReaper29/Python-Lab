# Find the data type of values.

class data:
    def datatype(self,x1):
        print('\n',x1,'is of type',type(x1))

m1 = data()
a=10
m1.datatype(a)
b=3.24
m1.datatype(b)
c=2+3j
m1.datatype(c)
name="Mohan"
m1.datatype(name)
list1=['Messi','Ronaldo','Beckham']
m1.datatype(list1)
tuple1=('Paurush',256,9.66)
m1.datatype(tuple1)
dic={'Nepal': 'Kathmandu','Italy': 'Rome', 'England':'London'}
m1.datatype(dic)
x = True
m1.datatype(x)
y = b"hello"
m1.datatype(y)
set1={112,443,22,66,99}
m1.datatype(set1)
set2=frozenset({"APPLE", "ORANGE", "BANANA"})
m1.datatype(set2)