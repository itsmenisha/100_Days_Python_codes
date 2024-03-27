a = int(input("enter your height: "))
b = int(input("enter your age:"))
if a >= 120:
    print("Welcome to the mary go round")
    if b > 18:
        c = 12
        print("your total will be $12")
    if 12 >= b <= 18:
        c = 7
        print("your total will be $7")
    if b < 12:
        c = 5
        print("your total will be $5")
    d = int(input("Do you want to take photos? say 1 for yes and 0 for no "))
    if d == 1:
        print("the cost for photo is 3 dollars")
        c += 3

    print(f"the total is {c}")
if a < 120:
    print("Your height is less than required to play mary go round")
