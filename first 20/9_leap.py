print("Welcome to leap year checker!!   ")
a=int(input("enter the year tat you want to check:"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("this is leap year")
        else:
            print("this is Not leap year")
    else:
        print("this is leap year")
else:
    print("this is Not leap year")  