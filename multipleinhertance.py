class Parent1:
    def P1method(self):
        print("iam a method from parent1")
class Parent2:
    def P2method(self):
        print("iam a method from parent2")
class Child(Parent1,Parent2):
    def CMethod(self):
        print("iam a method from child")

obj1=Child()
# obj1.CMethod()
# obj1.P1method()
obj1.P2method()
