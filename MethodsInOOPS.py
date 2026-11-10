# Methods

# init() method -> Also known as Constructor
class Student:
    def __init__(self, name, cgpa):
        print("This is the constructor")
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stud1 = Student("Muzamil", 8.21)
stud2 = Student("Adnan", 9.1)

print(stud1.name, stud1.cgpa)
print(stud2.name, stud2.cgpa)

print(f"{stud1.name} has cgpa = {stud1.get_cgpa()}")