# scope:it defines the life of a variable
# 1.global
# 2.local 
# 3.enclosed

# x=10 #x is having global scope
# def func1():
#     print(x)
# func1()
# def sample():
#     x=5 #here x is having local scope, 
#     # we can access only in this function only
#     print("hello")
# sample()
# print(x)
# def func1():
#     print(x)
#     def func2():
#         x=10 #so here x is having enclosed scope
#     func2()
# func1()

# def func1():
#    global x #declaring x globally
#    x=10 # assigning value to that variable
# func1()
# print(x)

# x=5
# def sample():
#     global x
#     x=10
# sample()
# print(x)

#global is a scope modifier to change the scope to global
x="hello"
def fun1():
    x=5
    def func2():
       nonlocal x
       x=10
    func2()
    print(x)
fun1()
print(x)
#nonlocal is used to change scope from enclosed to local but not global