
# for x in range(1,11):
#     print('x - ',x*2)

#x is nothing but iterator here

#in range--->if u give single arg, 
# then that value will considered as ending value

#in range--->if u give two args, 
# then frst one will be start and secnd one will be stop

# 2 x 1 = 2
# 2 x 2 = 4


# for x in range(1,11):
#     print(f"2 x {x} = {2*x}")

# def mul(num):
#     for x in range(1,11):
#         print(f"{num} x {x} = {num*x}")

# mul(5)

#print squares of first 10 numbers

# for x in range(1,11):
#     print(x**2)



# for x in range(1,11):
#     if(x%2==0):
#         print(x**2,'squares')
#     else:
#         print(x**3,'cubes')


#print numbers from 1 to 20 with specific conditions:
#1.if num is divisible by 2 then print num-fizz
#2.if num is divisible by 3 then print num-buzz
#3.if num is divisible by both 2 and 3 then print num-fizzbuzz


for i in range(1,21):
    if(i%2==0 and i%3==0):
        print(f"{i}-fizzbuzz")
    elif(i%3==0):
        print(f"{i}-buzz")
    elif(i%2==0):
        print(f"{i}-fizz")

# 12345678910
# 1491625.. 



