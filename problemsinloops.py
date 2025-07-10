# num=123
# cnvrt=str(num)
# for x in cnvrt:
#     print(x)

# for x in range(len(cnvrt)-1,-1,-1):
#     print(cnvrt[x])


# print(num%10)
# print(num//10)

# while(num>0): #123>0 #12>0 #1>0 #0>0
#     ld=num%10 #ld=123%10=>3 ld=12%10=>2 ld=1%10=>1
#     print(ld) #321
#     num=num//10 #123//10=>12 12//10=>1==>0



    # num=123890546
    # num=123890546//10
    # num=12389054

# num=125
# #sum of all digits in given num
# sum=0
# while(num>0):
#     ld=num%10 #5 #2 #1
#     sum+=ld #0+5=>5 #2+5=>7 # 7+1=>8
#     num=num//10 #12 #1
# print(sum)


# num=125
# #sum of squares of  all digits in given num
# sum=0
# while(num>0):
#     ld=num%10 
#     sum+=ld**2 
#     num=num//10
# print(sum)

#to find the cound of total digits in given num using while loop
# eg:12504-->6
# num=12504
# count=0
# while num>0:
#     ld=num%10 #4 #0 #5 #2 #1
#     count+=1 #1 #2 #3 #4 #5
#     num=num//10 #1250 #125 #12 #1 #0
# print(count)


# # reverse a num using while loop without cnverting into string
# rev=0

# rev x 10+ld==>0x10+5=5

# rev=5
# revx10+ld==>5x10+2=52

# rev=52
# revx10+ld==>52x10+1=521
# num=123654
# num1=num
# if(num%10 !=0):
#     rev=0
#     while (num>0):
#         ld=num%10
#         rev=rev*10+ld
#         num=num//10
#     print(rev)
#     if(num1==rev):
#       print("given num is palindrome")
#     else:
#         print("given num is not a palindrome")
# else:
#     print("give numbers which are non divisible by 10 becaus we cannot check for palindrome")

# 125===>1^3+2^3+5^3=125 then 125 is armstrong num
#1504===>1^4+5^4+0^4+4^4=1504 then 1504 is armstrong
#12====>1^2+2^2=12 then 12 is armstroing

#we know how to count digits of a given num
#we knoe how to find sum of power of count of digits of given number

#what is neon number
#what is sunny number