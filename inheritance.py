# acquiring methods and attributes from already defined class into newly created 
# class is called inheritance.

#creatig new class from already created class.

# types of inheritance:
# 1.single inheritance:
# if we derive one child class from single parent class then it is a single inheritance
# 2.multiple inheritance
# if we derive one child class from more than one parent class then it is a multiple inheritance 
# 3.multilevel inheritance
# 4.hierarchical inheritance
# 5.hybrid inheritance

class Parent:
    def Pmethod(self):
        print("iam a method from parent")
    def Pmethod2(self):
        print("iam a secnd method from parent")

class Child(Parent):
    def Cmethod(self):
        print("iam a method from child")
        super().Pmethod2() #calling method from super class using super() 


obj1=Child()
obj1.Cmethod()
# obj1.Pmethod()
# obj1.Pmethod2()
