# try:
#     age=int(input('enter age:'))
#     if age<18:
#         raise ValueError('childrens are not allowed')
#     else:
#         print('welcome to the show')
# except ValueError as e:
#     print(e)
# except:
#     print('unexpected error')

#here we are raising a new error for my own rules with existing error class.
# class MyErrorClass(Exception):
#     pass
# try:
#     age=int(input('enter age:'))
#     if age<18:
#         raise MyErrorClass('childrens are not allowed')
#     else:
#         print('welcome to the show')
# except MyErrorClass as e:
#     print(e)
# except:
#     print('unexpected error')


userinfo={'user':'harish','password':'harish123'}
class InvalidUsernameError(Exception):
    pass 
class InvalidPasswordError(Exception):
    pass
try:
    username=input('enter username: ')
    password=input('enter password: ')
    if(username != userinfo['user']):
        raise InvalidUsernameError('Invalid username')
    elif(password!=userinfo['password']):
        raise InvalidPasswordError('invalid password')
    else:
        print('login successful')
except InvalidUsernameError as e:
    print(e)
except InvalidPasswordError as e:
    print(e)
except :
    print('something went wrong')

