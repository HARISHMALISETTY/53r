# # num=16
# # isPerfect=False

# # for x in range(1,num):
# #     if(x**2==num):
# #         isPerfect=True
# #         break
# # if(isPerfect):
# #     print("it is a perfectsquare")
# # else:
# #     print("it is not a perfect square")


# # num=8
# # isSunny=False
# # for x in range(1,num):
# #     if(x**2==num+1):
# #         isSunny=True
# #         break
# # if(isSunny):
# #     print("it is a sunny number")
# # else:
# #     print("it is not a sunny number")


# # num=9
# # square=num**2
# # sum=0

# # while(square>0):
# #     ld=square%10
# #     sum+=ld
# #     square=square//10
# # if(sum==num):
# #     print("it is a neon")
# # else:
# #     print("it is not a neon")

# # num=5
# # isPrime=True
# # if(num<=1):
# #     print("please give number greaterthan 1")
# # else:
# #     for x in range(2,num):
# #         if(num%x==0):
# #             isPrime=False
# #             break
# #     if(isPrime):
# #         print("it is a prime number")
# #     else:
# #         print("it is not a prime number")


# #list of prime numbers from 1 to 50 usnig comprehensions

# def prime(num):
#     isPrime=True
#     if(num<=1):
#         print("please give number greaterthan 1")
#     else:
#         for x in range(2,num):
#             if(num%x==0):
#                 isPrime=False
#                 break
#         if(isPrime):
#             return True
#         else:
#             return False


# # op=tuple(x for x in range(2,51) if(prime(x)) ) tuple comprehesnions
# # op={x for x in range(2,51) if(prime(x))} #set comprehensions
# # print(op)


ip=["hello","hii","welcome","some","more"]

for x in ip: #x=hello #x=hii #x=welcome
    rev="" #rev= "" #rev="" rev=""
    for i in range(len(x)-1,-1,-1): #4 3 2 1 o # 2 1 0 #6543210
        rev+=x[i] #olleh #iih #emoclew 
    print(rev) #olleh iih emoclew

#create list of perfectsquares,neon,sunny using comprehensions
#create list of reversed strings using comprehensions