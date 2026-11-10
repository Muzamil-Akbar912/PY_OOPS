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
