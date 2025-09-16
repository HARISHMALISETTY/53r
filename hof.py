# # # X= lambda:print("")
# # #i can store a function into a variable

# # # ip=[X,'hi','ok']
# # #iam able to store function in a data structure also
# # #
# # # i can pass a function as a arg into another funcion
# # # i can allow a function to take another function as a arg also.


# # # def  sample():
# # #     print("hello world")
# # # def main(x):
# # #     x()
# # # main(sample)


# # def add(x,y):
# #     sum=x+y
# #     return sum 
# # def sub(x,y):
# #     sub=x-y
# #     return sub
# # def calculator(func,a,b):
# #    op=func(a,b)
# #    print(f"result is {op}")
# # # calculator(add,3,4)
# # # calculator(sub,10,4)
# # # calculator(lambda x,y:x*y,2,5)
# # # calculator(lambda x,y:x%y,10,3)

# # # ip-->[1,2,3,4,5]
# # # op--->[1,4,9,16,25]


# # def process(fun,x):
# #     result=[]
# #     for i in x:
# #        op=fun(i)
# #        result.append(op)
# #     print(result)
# # process(lambda x : x**2,[1,2,3,4,5])


# # # def manipulation(fun,x):
# # #     result=[]
# # #     for i in x:
# # #         op=fun(i)
# # #         result.append(op)
# # #     return result

# # op=map(lambda x:'hello'+x,{'harish','harsha','sushma','nandu','akhil'})
# # print(set(op))

# # op1=map(lambda x:len(x)>5,['hello','welcome','something','wow','like'])
# # print(list(op1))

# # #map is a built-in higher order function which performs
# # # a specifc task for all elements
# # #in the list/tuple/set and returns an object
# # #that we can convert into list or tuple/set
# # #as per our requirement

# # #filter is also a built-in higher order function which check a specfici condtion using a function for every elememnt
# # #in the list/tuple/set and filter that dataset and return an object. so that we can build set/list/tuple
# # #based on our requirement.





# # li=[1,2,3,4,5]
# # print(type(li))


# # n=4
# # print(type(n))

# def sample():
#     print('hello world')

# # print(type(sample))

# #function is a object
# #we can assign a function as a value to the variable
# #we can also use a function as a element in the data structure(list,tuple,sets,dictionary)
# #we can allow a function to pass as a arg into another function
# #we can allow a function to return another function
# #we can allow a function to take another fun as a arg.


# # ip=['hi','welcome','some','thing']
# # op=list(map(lambda x:x.upper(),ip))
# # print(op)

# # op1=tuple(filter(lambda x:len(x)>=4,ip))
# # print(op1)

# # ecommerce_data = [
# #     {"id": 1, "name": "iPhone 15", "category": "Electronics", "price": 79999, "stock": 25},
# #     {"id": 2, "name": "Nike Air Max", "category": "Fashion", "price": 8999, "stock": 50},
# #     {"id": 3, "name": "Organic Almonds 1kg", "category": "Grocery", "price": 1200, "stock": 100},
# #     {"id": 4, "name": "Samsung 55-inch 4K TV", "category": "Electronics", "price": 54999, "stock": 15},
# #     {"id": 5, "name": "Wooden Dining Table", "category": "Furniture", "price": 25999, "stock": 10},
# #     {"id": 6, "name": "Sony WH-1000XM5 Headphones", "category": "Electronics", "price": 29990, "stock": 35},
# #     {"id": 7, "name": "Adidas Hoodie", "category": "Fashion", "price": 4999, "stock": 60},
# #     {"id": 8, "name": "Dettol Hand Wash (Pack of 3)", "category": "Health & Hygiene", "price": 299, "stock": 200},
# #     {"id": 9, "name": "Harry Potter Box Set", "category": "Books", "price": 3499, "stock": 40},
# #     {"id": 10, "name": "Lenovo IdeaPad Laptop", "category": "Computers", "price": 42999, "stock": 20}
# # ]
# # f_op=list(filter(lambda x:x['category']=='Fashion',ecommerce_data))
# # print(f_op)

# # price_filter=list(filter(lambda x: x['price']>=3000 and x['price']<=50000,ecommerce_data))
# # print(price_filter)


from functools import reduce
# # reduce(func,iterable,intialvalue(optional))

# li=[5,7,9,3,1]

# op1=reduce(lambda x,y:x+y,li,6)

# # 1st--->x=5 and y=7
# #2nd--->x=12 and y=9
# #3rd--->x=21 and y=3
# #4th--->x=24 and y=1
# #5th--->x=25 

# #1st--->x=6 and y=5
# #2nd-->x=11 and y=7
# #3rd-->x=18 and y=9
# #4th-->x=27 and y=3
# #5th-->x=30 and y=1
# #6th--->x=31 

# print(op1)


# li=(10,4,9,2,5,7,23)

# op=reduce(lambda x,y:x if x>y else y,li)
# print(op)

#1st--->x=10 and y=4--->x<y--->x=4
#2nd-->x=4 and y=9--->x<y---->x=4
#3rd--->x=4 and y=2--->x<y--->x=2
#4th--->x=2 and y=5--->x<y--->x=2
#5th---->x=2 and y=7--->x<y--->x=2
#6th--->x=2 and y=23--->x<y--->x=2
#7th--->x=2

#find the smalled num using reduce method

ip=['I','LOVE','MY','INDIA']
#print smallest length string
#print largest length string
#print I LOVE MY INDIA
# op1=reduce(lambda x,y:x + y,ip)
# print(op1)

ip1=[4,6,3,2,9]
#op=46329

op2=reduce(lambda x,y:x*10+y,ip1)
print(op2)




