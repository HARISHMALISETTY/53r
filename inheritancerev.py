# class 
# object
# inheritance

# class Parent:
#     def __init__(self):
#         print("method from Parent")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("method from Child")

# obj=Child()

# class Parent:
#     def __init__(self):
#         self.valParent=125        
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.Valchild=250

# obj=Child()
# print(obj.valParent)

#whenever we r trying to access attributes from parentclass which are in a method.we can't
#access them directly. so we need to use super(). to get access for those variables.

# class Parent:
#     def __init__(self,pv):
#         self.Valparent=pv
# class Child(Parent):
#     def __init__(self, pv,cv):
#         self.Valchild=cv
#         super().__init__(pv)
#         print(f"parent value is {self.Valparent} and child value is {self.Valchild}")
# class grandChild(Child):
#     def __init__(self,gcv,pv,cv):
#         self.ValGrandChild=gcv
#         super().__init__(pv,cv)
#         print(f"grandchild value is {self.ValGrandChild} and child value is{self.Valchild} and parent value is {self.Valparent}")

# # obj1=Child(111,222)
# obj1=grandChild(gcv=100,cv=200,pv=250)

class Parent1:
    def __init__(self,pv1):
        self.ValParent1=pv1 
class Parent2:
    def __init__(self,pv2):
        self.ValParent2=pv2
class Child(Parent1,Parent2):
    def __init__(self,cv,pv1,pv2):
        self.ValChild=cv
        Parent1.__init__(self,pv1)
        Parent2.__init__(self,pv2)
    def show(self):
        print(f"total value of child from two parents and his own value is{self.ValChild+self.ValParent1+self.ValParent2}")
obj=Child(cv=100,pv1=200,pv2=300)
obj.show()



