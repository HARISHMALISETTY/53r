# loops

# expression inside loop

#conditions inside the loop

#
# list=[]
# for x in range(1,10):
#     if(x%2==0):
#         list.append(x)
#         # print(x+2)
# print(list)


#comprension is a combination of iteration,filteration(it is optional) and expression.

# 1.list comprehension
# 2.tuple comprehension
# 3.sets comprehension
# 4.dictionary comprehensions



# op=[x+2 for x in range(1,10)]
# print(op)

# op=[x for x in range(2,15)]

# print(op)

# create a list of squares of numbers from 1to 20 using comprehensions

# op=[x**2 for x in range(1,21)]
# print(op)

# list=["kiran","harish","pradeep","nandini","akhil"]

# op=[x.upper() for x in list]
# print(op)

#i want to print square of numbers from 10 to 30 only even numbers

# op=[x**2 for x in range(10,31) if x%2==0]

# print(op)

# list1=["hie","hello","welcome","something","king","queen"]

# # op1=[x.upper() for x in list1 if len(x)%2==0]

# # print(op1)
# def vowelccount(ip):
#     count=0
#     for x in ip:
#         if(x in['a','e','i','o','u']):
#             count+=1
#     if(count%2==0):
#         return True
#     else:
#         return False

# op1=[x.upper() for x in list1 if vowelccount(x) ]
# print(op1)


# num=28
# sum=0
def perfectnumber(num):
    sum=0
    for x in range(1,num):
        if(num%x==0):
        # print(x)
            sum+=x
    if(sum==num):
        # print("it is a perfect number")
        return True
    else:
        return False
        # print("it is not a perfect number")

#create a list of perfect numbers from 1 to 50 range using comprehensions


op3=[x for x in range(1,50) if perfectnumber(x)]
print(op3)

#create a list of armstrong numbers from 100 to 1000
#do research how to generate tuple comprehension






    
