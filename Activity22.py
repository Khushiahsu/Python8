#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

med = input('Do you have a medical cause?If yes, type Y,else type N')
att = int(input('Enter your attendance'))
if med=='Y':
    print('You are allowed to conduct the exam.')
else:
    if att>=75:
        print('You are allowed.Have fun!')
    else:
        print('I am very sorry but you cannot do the exam!')