print("Welcome! this is a mary go round")
a = int(input("enter your height : "))
b = int(input("enter your age : "))
if a >= 120:
    print("Enjoy your ride!!")
    if b >= 18:
        print("your total will be $12")
    elif b > 12:
        print("your total will be $7")
    else:
        print("your total will be $5")
else:
    print("sorry you are too short for the ride")
