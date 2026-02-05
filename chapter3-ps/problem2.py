# fill in a letter template given below with name and date.

letter = ''' 
Dear <|NAME|>,
You are selected!
Date: <|DATE|>
'''
name = input('Enter your name :')
date = input('Enter date :')

# chaning replace to replace multiple things in one line
letter1 = letter.replace('<|NAME|>', name).replace('<|DATE|>', date)
print(letter1)

