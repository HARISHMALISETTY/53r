#while loop-->
# whenever if we want to execute the code until the condition become false,
# then we will use while loop there


#for loop--->we no need to mention where we 
# should start no need to mention how should we update.
list=[4,6,8,912,34,56]

# for x in list:
#     print(x)

#here for loop will iterates from start to end by stepping one and iterates 
# through out the list till its length

# x=0 #im telling from where it should start
# while(x<len(list)): #adding condition
#     print(list[x])
#     x+=1 #iam mentioning how to make a step means how to update x value


# for x in range(1,11):
#     print(x)


# y=1 #iam telling from where to start
# while(y<=10): # condition to stop
#     print(y)
#     y+=1 #how to step/update


# flashsale=False
# while(flashsale):
#     print("do shopping with more offers")

#print even numbers using while loop
# num=2
# while(num%2==0 and num<=20):
#     print(num)
#     num+=1

#whenevr condition fail, while loop will exit at that moment

# num=1
# while(num<=20):    
#     if(num%2==0):
#         print(num)
#     num+=1

"hello"

"olleh"

# x1=["a","b","c","d","e"]

# for x in range(len(x1)-1,-1,-1):
#     print(x1[x])

#reverse a string
str="madam"
op=""
for char in range(len(str)-1,-1,-1):
    op+=str[char]
print(op)

if(op==str):
    print("it is palindrome")
else:
    print("it is not a palindrome")

#using while loop check string is palindrome or not
#reverse a num without converting into string using while loop
