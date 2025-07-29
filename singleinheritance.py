# class User:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
# class Student(User):
#     def __init__(self,name,email,enrolledcourses):
#         super().__init__(name,email)
#         self.enrolledcourses=enrolledcourses
#     def getCourses(self):
#         print(f"{self.name} is learning {self.enrolledcourses}")
#     def removeCourse(self,course):
#         self.enrolledcourses.remove(course)
#         self.getCourses()
#     def addCourse(self,course):
#         self.enrolledcourses.append(course)
#         self.getCourses()

# class Instructor(User):
#     def __init__(self,name,email,courses_training):
#         super().__init__(name,email)
#         self.courses_training=courses_training
#     def getCourses(self):
#         print(f"{self.name} is teaching {self.courses_training}")

# Student_obj=Student("shanmukh","shanmukh@gmail.com",["html","css","python","js"])
# Student_obj.removeCourse("html")
# Student_obj.addCourse("sql")
# # Student_obj.getCourses()
# # Trainer_obj=Instructor("Harish","harish@gmail.com",["frontend","backend","db","AI"])
# # Trainer_obj.getCourses()


class ParentActor:
    def __init__(self,name,Pworth):
        self.Pname=name
        self.Pworth=Pworth
        print(f"{self.Pname} is the parent")
    def Passets(self):
        print(f"{self.Pname} assets are {self.Pworth} cr")
class ChildActor(ParentActor):    
    def __init__(self,Pname,Cname,Pworth):
        super().__init__(Pname,Pworth)
        self.Cname=Cname
        print(f"{self.Cname}is came by the referrence of{self.Pname}")
    def Cassets(self,worth):
        self.Cworth=worth
        print(f"{self.Cname}is having worth of {self.Cworth}cr")
    def TotalAssets(self):
        print(f"total assets of {self.Cname} is {self.Pworth+self.Cworth}")
ramcharan=ChildActor("chiranjeevi","ramcharan",100)
ramcharan.Cassets(75)
ramcharan.TotalAssets()
ramcharan.Passets()
