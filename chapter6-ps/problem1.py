# Write a program to find the greatest of four numbers entered by the user.

n1= int(input('Enter num 1:'))
n2= int(input('Enter num 2:'))
n3= int(input('Enter num 3:'))
n4= int(input('Enter num 4:'))

if(n1>n2 and n1>n3 and n1>n4):
    print ('Entered number n1 is gretet :', n1)

elif(n2>n1 and n2>n3 and n2>n4):
    print ('Entered number n1 is gretet :', n2)

elif(n3>n1 and n3>n2 and n3>n4):
    print ('Entered number n1 is gretest :', n3)
    
else:
    print ('Entered number n4 is gretest :', n4)