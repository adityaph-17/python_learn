# in this code we learn about if elif else ladder 

age = int(input('Enter yor age to check you are able to apply for driving licence :'))

if(age> 18):
    print('you are able for apply')

elif ( age==0 ):
    print ('your enter age is 0 which is not valid.')

elif ( age<0 ):
    print ('your entered age is negative which is not valid.')

else :
    print ('you are not able to apply , your age must be above 18.')
