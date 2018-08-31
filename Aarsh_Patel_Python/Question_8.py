distance = int(input("Enter the distance to travel (km): "))
weather = int(input("Press 1 for snowy, 2 for rainy, 3 cloudy, 4 sunny: "))

speed = 0
time_taken = 0

if weather == 1:
    time_taken = distance/40
elif weather == 2:
    time_taken = ((distance*0.25)/40) + ((distance*0.75)/60)
elif weather == 3:
    time_taken = ((distance*0.4)/60) + ((distance*0.6)/100)
else:
    time_taken = distance/100

if time_taken > 2:
    print("Sorry, you will not make it")
else:
    print("You can make it!")
