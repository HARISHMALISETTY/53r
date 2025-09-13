# X= lambda:print("")
#i can store a function into a variable

# ip=[X,'hi','ok']
#iam able to store function in a data structure also
#
# i can pass a function as a arg into another funcion
# i can allow a function to take another function as a parm also.


# def  sample():
#     print("hello world")
# def main(x):
#     x()
# main(sample)


def add(x,y):
    sum=x+y
    return sum 
def sub(x,y):
    sub=x-y
    return sub
def calculator(func,a,b):
   op=func(a,b)
   print(f"result is {op}")
# calculator(add,3,4)
# calculator(sub,10,4)
# calculator(lambda x,y:x*y,2,5)
# calculator(lambda x,y:x%y,10,3)

# ip-->[1,2,3,4,5]
# op--->[1,4,9,16,25]


def process(fun,x):
    result=[]
    for i in x:
       op=fun(i)
       result.append(op)
    print(result)
process(lambda x : x**2,[1,2,3,4,5])


# def manipulation(fun,x):
#     result=[]
#     for i in x:
#         op=fun(i)
#         result.append(op)
#     return result

op=map(lambda x:'hello'+x,{'harish','harsha','sushma','nandu','akhil'})
print(set(op))

op1=map(lambda x:len(x)>5,['hello','welcome','something','wow','like'])
print(list(op1))

#map is a built-in higher order function which performs
# a specifc task for all elements
#in the list/tuple/set and returns an object
#that we can convert into list or tuple/set
#as per our requirement

#filter is also a built-in higher order function which check a specfici condtion using a function for every elememnt
#in the list/tuple/set and filter that dataset and return an object. so that we can build set/list/tuple
#based on our requirement.






