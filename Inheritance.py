# Reusing attribute and methods from a parent(Base) class.

class Employee:
    start_time = "10am"
    end_time = "6am"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

staff1 = AdminStaff("Manager")

t1 = Teacher("Math")
t1.change_time("5pm")

print(t1.subject, t1.start_time, t1.end_time)

print(staff1.role, staff1.start_time, staff1.end_time)

acc1 = Accountant(25_000, "CA")

print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)