class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class Student(User):
    def __init__(self,name,email,enrolledcourses):
        super().__init__(name,email)
        self.enrolledcourses=enrolledcourses
    def getCourses(self):
        print(f"{self.name} is learning {self.enrolledcourses}")
    def removeCourse(self,course):
        self.enrolledcourses.remove(course)
        self.getCourses()
    def addCourse(self,course):
        self.enrolledcourses.append(course)
        self.getCourses()

class Instructor(User):
    def __init__(self,name,email,courses_training):
        super().__init__(name,email)
        self.courses_training=courses_training
    def getCourses(self):
        print(f"{self.name} is teaching {self.courses_training}")

Student_obj=Student("shanmukh","shanmukh@gmail.com",["html","css","python","js"])
Student_obj.removeCourse("html")
Student_obj.addCourse("sql")
# Student_obj.getCourses()
# Trainer_obj=Instructor("Harish","harish@gmail.com",["frontend","backend","db","AI"])
# Trainer_obj.getCourses()


