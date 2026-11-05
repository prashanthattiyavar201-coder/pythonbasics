class Employee: # Parent
    a = 1

class Programmer(Employee): # Child 1
    b = 2

class Manager(Programmer): # Child 2
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)