print("ahihi")
a = 5
print(a)

# name = input('Enter your name: ')
def hi(name):
    print('hello ' + name)

# hi(name)

# n = input('n = ')
s = 0

for i in range(1,int(n)+1):
    s+=i

# print(s)

class employee:
    'base class for all employee'
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print('name '+ self.name  + 'salary :' + str(self.salary))


A = employee('quyet', 1000)
A.display()
A.salary = 2
A.display()
print(employee.__doc__)