#Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
print("Select Your Ride!!")
print("1.Car")
print("2.Bike")

choice= int(input('What do you think is better?'))

if choice== 1:
    print("What type do u select? \n")
    print("1.Electric Car \n")
    print("2.Diesel Cars \n")
    choice2= (input('What do you think is better?'))

    if choice2==1:
        print("Have some fun with your new car!!")
    else:
        print("Have fun with your diesel car!!")
elif choice==2:
    print('What type of bike do you wish to have? \n')
    print('1. A motorcycle \n')
    print('2. A bicycle \n')
    choice3= (input('Which do you prefer?'))

    if choice3==1:
        print('Have fun with your brand new motorcycle!!')
    else:
        print('Have fun with your new cycle!!')