# Write a program to calculate the factorial of a given number using for loop.
# 5! = 1*2*3*4*5

num = int(input('Enter a num:'))

product =1

for i in range(1,num+1): # i = 1,2,3,4,5,...num
    product = product * i  

print (f"factorial of {num} is {product}")