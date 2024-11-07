#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
uni = int(input('Enter how many units you have consumed'))
if (uni<50):
    amount = uni*2.60
    tax=25

elif (uni<=100):
    amount=130+((uni-50)*3.25)
    tax=35
elif (uni<=200):
    amount=130+((uni-100)*5.26)
    tax=45
else: 
  
    amount=130+((uni-200)*8.45)
    tax=75
total=amount+tax
print('\n Your elecricity bill is',total)