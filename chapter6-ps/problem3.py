# A spam comment is defined as a text containing following keywords:“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

m1 = 'Make a lot of money'
m2 = 'buy now'
m3 = 'subscribe this'
m4 = 'click this'

msg = input (' enter message to check it spam or not :')

if (m1 in msg or m2 in msg or m3 in msg or m4 in msg ):
    print ('\n stay away this is spam!')
else:
    print('this is not a spam.')
