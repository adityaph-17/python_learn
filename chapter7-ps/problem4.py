# Write a program to find whether a given number is prime or not.

num = int(input('Enter num :'))

for i in range(2,num):# range(2, 7) → 2, 3, 4, 5, 6 	7 % 2  7 % 3  7 % 4  7 % 5  7 % 6 
    if(num%i)==0:
        print('not prime')
        break
else:
    print('prime number!')