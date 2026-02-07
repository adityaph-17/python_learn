age = int(input('enter you age :'))

# this will run independent if statement no : 1
if(age%2==0):
    print ('age is even !')
else:
    print ('age is not even !')

# this will run independent if statement no : 2
if(age> 18):
    print('you are able for apply')

elif ( age==0 ):
    print ('your enter age is 0 which is not valid.')

elif ( age<0 ):
    print ('your entered age is negative which is not valid.')

else :
    print ('you are not able to apply , your age must be above 18.')

print('Thank You')



