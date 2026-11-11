# method overriding

class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()

# Duck Typing -> walks like a duck and quaks like a duck

class Teacher1():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")

t2 = Teacher1()
t2.get_designation()

acc1 = Accountant()
acc1.get_designation()