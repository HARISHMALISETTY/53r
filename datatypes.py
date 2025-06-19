# x=5 #integer
# y=12.5 #float
# z="something" #string
# a=3+8j
# is_available=True

# value1=25
# print(id(value1))
# value1=40
# print(id(value1))

# print(value1)

# list--->[]
#tuples---->()
#set---->{}
#dictionary--->{}

# fruits=["apple","mango","banana"] # collection of strings and list of fruits
# print(id(fruits))

# fruits[1]="pineapple"

# print(id(fruits))

# ids=[1,2,3,4] #collection of integers and list of ids
# prices=[125.67,256.2,450.2,116.22] #collection of floatingvalues and list of prices
# mixed=[1,2,"hi",12.5,True]
# print(type(fruits))
# print(type(ids))
# print(type(prices))
# print(type(mixed))

#so we can say a list can be a collection of homogeneous / heterogeneous elements.

# print(len(fruits))

#length of the fruits collection is 3

# print(f"length of the fruits collection is {len(fruits)}")

# print(fruits[len(fruits)-1]) 

# a="harish"
# print(id(a))
# a="kiran"
# print(id(a))

# #for every new value it will create new memory address, so we can say primitives are immutable in same memory.

# x=["harish","naresh","suresh","mahesh"]

# print(id(x)) #before changing the values inside the list


# x[2]="kiran"

# print(id(x))

#in lists we can update elements in the list within the same memory. so we can say 
# lists are mutable

# x=[1,2,3]
# x[len(x)]=4

# print(x)

# x=[]+[4]
# print(x)

list=[1,2,"hi","hello","somthing",[1,2,3],5,67]

# op=list+["python"]+[12]

# print(op)


# str="hello  world"
# str1="welcome"

# # print(str[-1])

# op=str+str1+"[okokk]"

# print(op)


ip=[1,2,[4,5],[6,7],8,"something"]

# print(ip[2][0])
print(ip[5][5])