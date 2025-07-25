# # class SampleClass:
# #     -------
# #     -------
# #     -------

# class Person:
#     name="kiran"
#     age=25
#     gender="male"
    
# obj1=Person()
# obj2=Person()
# print(obj1)
# print(obj2)
# print(obj1.name)
# print(obj2.name)

# obj1.name="kiran kumar"
# #updating value in obj1
# print(obj2.name) #does not reflected to object2
# print(obj1.name) #reflecting only in obj1
# print(Person().name) #does not reflect to person class also.


# class Person:
#     def __init__(self,name,gender,age):
#         self.name=name 
#         self.gender=gender 
#         self.age=age 

# obj_rakesh=Person("rakesh","male",24)
# obj_kiran=Person("kiran","male",25)        

# print(obj_kiran.name)
# print(obj_rakesh.name)


class Application:
    def __init__(app,name,color,category):
        app.name=name
        app.color=color
        app.category=category
    def purpose(self,app_name,purpose):
        print(f"{app_name} is used for {purpose}")

insta=Application("instagram","pink","social media")
youtube=Application("Youtube","red","entertainment")
Ola=Application("ola","black","travelling")
zomato=Application("zomato","red","food")

# print(insta.name,insta.color,insta.category)
# print(youtube.name,youtube.color,youtube.category)
# print(Ola.name,Ola.color,Ola.category)
# print(zomato.name,zomato.color,zomato.category)
insta.purpose("instagram","socialmedia")
youtube.purpose("youtube","entertainment")
Ola.purpose("ola","travelling")
zomato.purpose("zomato","food")
