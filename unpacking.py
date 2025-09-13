# x={1,2,3}

# print(x)

# values={9,4,7,3}
# # a,b,c,d=values
# # print(a,b,c,d)

# a,*b=values

# print(a,b)

# a=5
# b=4

# a,b=b,a

# print(a,b)

a=(1,2)
b=(3,4)
op=(*a,*b)
print(op)
# op=a+b
# print(op)

a=[1,2]
b=[3,4]
op=[*a,*b]
print(op)

a={1,2}
b={3,4}
op={*a,*b}
print(op)

x={'name':"bargav",'gender':'male'}
y={'city':'hyd','role':'developer'}

op={**x,**y}
print(op)


x=4
print(x)
x+=4
del x



