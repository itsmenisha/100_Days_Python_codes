print("welcom to your tip calculator")
a = float(input("Enter the total bill: "))
b = int(input("Enter the number of people you want to split the bill: "))
c = int(input("Enter the tip percentage (12, 10, or 15): "))

if c == 12:
    d = (a * (1+0.12)) / b
elif c == 10:
    d = (a * (1+0.10)) / b
elif c == 15:
    d = (a * (1+0.12)) / b
else:
    print("Enter 12, 15, or 10 for tip percentage.")
    exit()  # Terminate the program if an invalid tip percentage is entered
e = round(d, 2)
print(f"Each person should pay:${e}")

# c = c/100
# d = (a*(1+c)/b)
# e = round(d, 2)
# print(f"Each person should pay:${e}")
