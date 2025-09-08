#A function calling itself continuosly/repeatedly until a certain condition is
# getting satisfied is called recursion.

# def open_giftbox(n):
#     if n>1:
#         print(f'box{n} is opened')
#         open_giftbox(n-1)
#     else:
#         print(f'gift found in box{n}')
# open_giftbox(5)


# 5--->5x4x3x2x1

# def factorial(n):
#     fact=1
#     if n==1 or n==0:
#         return fact
#     else:
#         factorial_n=n*factorial(n-1) 
#         return factorial_n
# print(factorial(5))

# 0 1 1 2 3 5


# x=5

# y=5.5


# print(isinstance(x,int))

# print(isinstance(y,float))

# print(isinstance([1,2,3],list))


x=[1,2,3,[4,5,6,[3,4,5]]]
sum=0
for val in x:
    if isinstance(val,list):
        for i in val:
            if isinstance(i,list):
                for j in i:
                    sum+=j
            else:
                sum+=i
    else:
        sum+=val
print(sum)

