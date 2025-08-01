# class Sample:
#     def __init__(self):
#         self.__name='harish'

# obj=Sample()
# print(obj.__name)

#name-->public-->we can access without restrictions 
#_name-->protected-->we are not suppose to access but we can access.
#__name-->private-->we can't access out of the class but we 
# can hack it using name mangling approach.which is not recommended.

# but we can access private variables using getter and setter methods which will define in the same class.

#whenever we use only single class...we are not suppose to use protected variable outside of the class.

#whenever if we do inheritance then protected variables are allowed to use in both child and parent.


# class Parent:
#     def __init__(self):
#         self._user='harish'
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print(self._user) #it is allowed

# obj1=Child()


# class Parent:
#     def __init__(self):
#         self.__user='harish'
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print(self.__user) #it is restriced to Parent class only

# obj1=Child()



# class Sample:
#     def __init__(self):
#         self.__name='harish'

#     def getDetails(self):
#         # print(self.__name)
#         return self.__name

# obj=Sample()
# print(obj.getDetails())


# class Demo:
#     def __init__(self):
#         self.name='harish'

# obj=Demo()
# print(obj.__dict__)
# obj.name='kiran'
# print(obj.__dict__)


# class Demo:
#     def __init__(self):
#         self._name='harish'

# obj=Demo()
# print(obj.__dict__)
# obj._name='kiran'
# print(obj.__dict__)


# class Demo:
#     def __init__(self):
#         self.__name='harish'

# obj=Demo()
# print(obj.__dict__) #{_Demo__name:'harish'}
# obj.__name='kiran' #{_Demo__name:'harish',__name:'kiran'}
# print(obj.__dict__)

class Demo:
    def __init__(self):
        self.__name='harish'
    def setDetails(self):
        self.__name='kiran'

obj=Demo()
print(obj.__dict__)
obj.setDetails()
print(obj.__dict__)



