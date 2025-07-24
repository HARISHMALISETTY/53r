# *
# **
# ***
# ****
# *****

# for x in range(5):
#     str="" 
#     for y in range(x+1): 
#         str+="*"        
#     print(str)

# for x in range(1,6):
#     str=0 
#     for y in range(x): 
#         str=str*10+x        
#     print(str)

# 0
# 11
# 222
# 3333
# 44444

# for x in range(1,6):
#     str=0 
#     for y in range(x+1): 
#         str=str*10+y        
#     print(str)

# for x in range(97,102):
#     str="" 
#     for y in range(97,x+1): 
#         str+=chr(x)       
#     print(str)


# print(chr(97))
# a 
# bb
# ccc
# dddd
# eeeee

# for x in range(97,102):
#     str="" 
#     for y in range(97,x+1): 
#         str+=chr(y)       
#     print(str)

str="something"

# s 
# so 
# som
# some 
# somet 
# someth 
# somethi
# somethin
# something

# op=""
# for i in str:    
#     op+=i
#     print(op)

# for x in range(1,6):
#     num=0 
#     for y in range(1,x+1): 
#         num=num*10+y       
#     print(num)

# 1
# 14
# 149
# 14916
# 1491625

#1
#44
#999
#16161616
#2525252525


# *****
# ****
# ***
# **
# *

# for x in range(1, 6):
#     num = 0
#     place = 1 
#     for y in range(x, 0, -1):  
#         square = y ** 2

#         # Count digits in square
#         temp = square
#         digits = 0
#         while temp > 0:
#             temp = temp // 10
#             digits += 1

#         num = square * place + num
#         place = place * (10 ** digits)

#     print(num)

# list=["hello","welcome","something","hello","apple","apple"]

# op={"hello":2,"apple":2,"welcome":1,"something":1}
# dict={}



# for x in list:
#     if(x in dict):
#         dict[x]+=1
#     else:
#         dict[x]=1
# print(dict)

# ex="BANANA"
# # op={"B":1,"A":3,"N":2}
# dict={}
# for x in ex:
#     if(x in dict):
#         dict[x]+=1
#     else:
#         dict[x]=1
# print(dict)