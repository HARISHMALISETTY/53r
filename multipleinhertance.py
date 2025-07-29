# class Parent1:
#     def P1method(self):
#         print("iam a method from parent1")
# class Parent2:
#     def P2method(self):
#         print("iam a method from parent2")
# class Child(Parent1,Parent2):
#     def CMethod(self):
#         print("iam a method from child")

# obj1=Child()
# # obj1.CMethod()
# # obj1.P1method()
# obj1.P2method()

# Parent class 1
class Developer:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")

# Parent class 2
class Mentor:
    def courses(self, courses):
        self.courses = courses
        print(f"courses: {', '.join(self.courses)}")

# Child class
class Trainer(Developer, Mentor):
    def __init__(self, emp_id, salary, courses):
        super().__init__(emp_id, salary)
        self.courses = courses

    def teach(self):
        print(f"Training courses are: {self.courses}")

# Create object
Trainer1 = Trainer("T102", 50000, ["frontend","backend","database"])

# Accessing methods from both parent classes
Trainer1.show_details()         # from Employee
Trainer1.courses(["html", "python"])  # from Mentor
Trainer1.teach()                # from Teacher
