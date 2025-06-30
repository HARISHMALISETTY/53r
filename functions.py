# # def sample():
# #     print("hello world")
# # sample()
# # sample()

# # def demo(name):
# #     print(f"hello{name}")
# #     # return "something" #execution will stops here itself
# #     print("welcome")
# #     print("one")


# # print(demo("harish"))

# # def addition(a,b):
# #     sum=a+b
# #     return sum
# # # print(addition(4,5))
# # op=addition(10,12,13)
# # print(op)


# def sample(a,b,c=15):
#     print(a,b,c)
# # sample(2,4)

# # idly-->15 +5%
# # dosa-->25 +5%
# # poori--->30 +5%


# # def hotel(item,quantity,gst=5):
# #     total=item*quantity+((item*quantity*gst)/100)
# #     return total
# # # op=hotel(30,2)
# # op=hotel(25,2,12)
# # print(op)


# # def shopping(*cart):
# #     print(cart)

# # shopping("soap","shampoo","deodrant","facecream","icecream")

# # def fullName(firstName,LastName):
# #     fullname=firstName+LastName
# #     print(fullname)

# # fullName(LastName="charan",firstName="ram")

# def family(**childrens):
#     print(childrens)
# family(first="ram",second="lakshman",third="bharath",fourth="sathrugn")
# invoking a function

# def sample():
#     # return "hi"
#     print("hello")
# print(sample())

# A FUNCTION CALLING ITSELF CONTINUOSLY UNTIL IT MET A SPECIFIC CONDITION THEN IT IS CALLED
# RECURSIVE FUNCTION.

def sample(n):
    if(n==0):        
        print("found gift")
    else:
        print(f"{n} box opened")
        sample(n-1)

sample(5)

#incase if u didnt add any condtion in recursive function, it will limits function call itself
# for 997-1000 times