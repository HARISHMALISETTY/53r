import re 

# match,search,findall
# ip="hello world hello hello"
# regex=r"hello" 
#if match founds in starting of the given string then return matched object
#if it is not found then returns none.
# op=re.match(regex,ip)
# print(op)

# op=re.search(regex,ip)
#returns the matched object if it is found anywhere in the given string.
#if not found returns none.
#once it found the match then stops searching.
# op=re.findall(regex,ip)
# print(op)

# regex=r"c.t"
# op=re.search(regex,"c21tcultcajt")
# if(op):
#     print('valid input')
# else:
#     print('invalid input')

#username should contain a 3 letter word with starting p and ending t anywhere in the string.then i will allow it
#otherwise i wont allow.

# regex1=r"p.t"
# op=re.search(regex1,"okcdpkt")
# if(op):
#     print('valid')
# else:
#     print('invalid')

# regex1=r"^sbin"
# op=re.match(regex1,"sbin02326")
# if(op):
#     print("valid ifsc code")
# else:
#     print("invalid ifsc code")

# regex1=r"com$"
# op=re.search(regex1,"harish@gmail.com")
# if(op):
#     print("valid email")
# else:
#     print("invalid email")


# regex1=r"\s"
# op=re.search(regex1,'hello world')
# if(op):
#     print("valid input")
# else:
#     print("invalid input")

# # regex1=r"[aeiou]"
# regex1=r"[A-Z]"
# op=re.search(regex1,"abcdAVG")
# if(op):
#     # print("vowels are present")
#     print("valid")
# else:
#     # print("vowels are not present")
#     print("invalid")


# regex1=r"[^aeiou]" #this will not allow a string with pure owels
# op=re.search(regex1,"welcome")
# if(op):
#     print("valid")
# else:
#     print("invalid")

#accept a input when it have length more then 5
# regex1=r"\w{5,}"
#accept a input when it have length more then 5 and less than 10
regex1=r"^\w{5,10}$"

op=re.search(regex1,"hell0worldnew")
if(op):
    print("valid")
else:
    print("invalid")