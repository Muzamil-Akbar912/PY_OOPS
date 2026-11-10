# Attributes 

# 1. class attributes -> belongs to class
# 2. instance attributes -> belongs to object

class Student:
    college_name = "DBIT" # class
    PI = 3.1

    def __init__(self, name, gpa): # instance
        self.name = name
        self.gpa = gpa
        self.PI = 3.14

stud1 = Student("Adnan", 9.2)

print(stud1.name)
print(stud1.college_name)
print(Student.college_name)
print(stud1.PI)

# instance attribute has higer priority.


class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self): # instance method
        print(f"laptop has {self.RAM} RAM and {self.storage} {self.storage_type}")

l1 = Laptop("16GB", "512GB")
l2 = Laptop("8GB", "256GB")
l3 = Laptop("4GB", "128GB")

l1.get_info()
l2.get_info()