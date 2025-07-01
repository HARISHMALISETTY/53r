# num=int(input("enter a num :"))
# if(num>0):
#     if(num%2==0):
#         print("num is even and positive")
#     else:
#         print("num is odd and positive")
# elif(num<0):
#     if(num%2==0):
#         print("num is even and negative")
#     else:
#         print("num is odd and negative")
# else:
#     print("u have entered zero")

# a=int(input("enter value a : "))
# b=int(input("enter value b : "))
# c=int(input("enter value c : "))

# if(a==b==c):
#     print("we can form equilateral traingle")
# elif((a==b) or (b==c) or (c==a)):
#     print(" we can form isosceles triangle")
# elif(a!=b!=c):
#     print("scalene triangle")
# elif(((a+b)>=c) or ((b+c)>=a) or ((c+a)>=b)):
#     print("inquality triangle")
# else:
#     print("can not form a triangle")


# balance=25000
# withdraw=int(input("enter withdraw amnt : "))

# if(balance>withdraw):
#     if(withdraw%100==0):
#         print(f"rupees {withdraw} successfully withdrawan.")
#     else:
#         print("withdraw amount should be multiple of 100 only")
# else:
#     print("insufficient balance")


# def greet():
#     return "hello,how are you.!"

# print(greet())

# def mul(a,b):
#     mul=a*b
#     return mul 
# print(mul(2,5))

# def add(a,b):
#     add=a+b
#     return add
# print(add(4,5))

def sub(a,b):
    sub=a-b
    return sub
# print(sub(4,5))

def div(a,b):
    div=a/b
    return div
# print(div(4,5))

def calculator(a,b,op):
    if(op == '+'):
        return a+b
    elif(op == '-'):
        return a-b
    elif(op == '*'):
        return a*b
    elif(op == '/'):
        return a/b
    else:
        return "invalid operator"
    
# print(calculator(4,5,'*'))

def greet(stud_name='student',branch='engineering'):
    print(f"hello {stud_name}, hope you doing good in {branch} program")

# st=input("enter student name: ")
# br=input("enter branch name :")    

# greet(branch=br,stud_name=st) #keyword arguments
# greet(input("enter student name: "),input("enter branch name :"))

# greet("kiran","civil") #positional argument
# greet(branch='civil',stud_name="kiran",) #keyword arguments
st=input("enter student name :")
br=input("enter branch name :")
greet(st,br) #positional
greet(stud_name=st,branch=br)