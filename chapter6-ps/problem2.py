# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input('enter marks 1 :'))
marks2 = int(input('enter marks 2 :'))
marks3 = int(input('enter marks 3 :'))

total_persentage = ((marks1+marks2+marks3)/300)*100

if (total_persentage==40 and marks1>=40 and marks2>=40 and marks3>=40):
    print('congratulation you are pass, percentage is :',total_persentage)
else:
    print('sorry you are failed ! try again, next time\n percentage is :', total_persentage)
    