print('''This program will ''')
'''This is nisha
this is nisha'''

a = int(input("enter your height: "))
b = int(input("enter your age:"))
c = 0
if a >= 120:
    print("Welcome to the mary go round")
    if b > 18:
        if b > 44 and b < 56:
            d = input("are you having a midlife crisis? y or n ?? ")
            if d == "y":
                print("Everything is going to be fine. Have a free ride on us")
        else:
            c = 12
            print("your total will be $12")
    if 12 >= b or b <= 18:
        c = 7
        print("your total will be $7")
    if b < 12:
        c = 5
        print("your total will be $5")

    d = input("Do you want to take photos? y or n ")

    if d == "y":
        print("the cost for photo is 3 dollars")
        c = c + 3
    print(f"the total is {c}")
if a < 120:
    print("Your height is less than required to play mary go round")
