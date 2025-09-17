#two types of errors--->compile time  and runtime.
#errors which occurs during compilation due to syntax errors mainly
#can be considered as compiletime errors

#errors which occurs during runtime/executiontime due to inputs
#from the user can be considered as runtime errors.


#compiletime errors we need to resolve by writing code without
#any syntax mistakes.

#runtime errors we have to handle by using some techniques like
#exception handling.

#try and except blocks.


# if True:
#     print("hello world")


# try:
#     x=4
#     y=5
#     sum=x+y
#     print(sum)
# except:
#     print('error occured')

# x=5
# y=0
# print(x/0)

# try:
#     x=int(input('enter x value :'))
#         y=int(input('enter y value :'))
#         print(x+y+z)
# except TypeError as error:
#     print('division can be done only b/w numbers',error)
# except ZeroDivisionError as error:
#     print('we cant divide any number with 0',error)
# except ValueError as error:
#     print('input should be a number',error)
# except NameError:
#     print('variable is not defined')
# except IndentationError:
#     print('indentation is not proper')
# except:
#      print('something went wrong')
# finally:
#     print('code execution is completed ')


# try:
#     # x=[1,4,8,9]
#     # print(x[6])
#     x=5
#     x.append(15)
# except IndexError:
#     print('index is out of range')
# except AttributeError:
#     print('this method is not available for integers')    

# try:
#     dict={'name':'Nandu','gender':'female'}
#     print(dict['city'])
# except:
#     print('key is not available in given dictionary')    

# try:
#     open('./harish.txt','r')
# except FileNotFoundError:
#     print('file not found')

# try:
#     import some 
# except ModuleNotFoundError:
#     print('module is not available')

