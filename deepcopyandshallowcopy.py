# # print("hello world")
import copy
# x={'name':'harish','city':'hyd','age':26}

# x1=copy.copy(x)
# x2=copy.copy(x)

# x1['name']='naresh'
# x1['age']+=1

# print(x)
# print(x1)

# x=5

# x=6
# info={"details":{"name":'harish','city':'hyd'}}

# x=copy.deepcopy(info)
# y=copy.deepcopy(info)

# x['details']['name']='naresh'

# print(info)
# print(x)
# print(y)

#shallow copy:-> it will create the copies of objects within same referrence.
# copy.copy()

#deep copy:->it will create the copies from the object with new referrences.
#copy.deepcopy()

#to see the difference between s_copy and d_copy, we have to use nested objects only.

# score_board={"score":{'runs':135,'wickets':4,'overs':4.4}}
# Nithish=copy.deepcopy(score_board)
# sravani=copy.deepcopy(score_board)
# sravani['score']['runs']+=6

# print(score_board)
# print(Nithish)
# print(sravani)


pubg={'score':{'kills':0,'health':100}}
shanmukh=copy.deepcopy(pubg)
tharun=copy.deepcopy(pubg)
naveen=copy.deepcopy(pubg)
abdul=copy.deepcopy(pubg)
shanmukh['score']['kills']+=4
naveen['score']['health']-=25
print(pubg)
print(tharun)
print(shanmukh)
print(abdul)
print(naveen)