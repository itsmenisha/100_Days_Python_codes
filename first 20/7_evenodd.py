print("To check wether the number is even or odd")
a = (int(input("enter your number : ")))
if a % 2 == 0:
    print(f"the input number {a} is even")
elif a % 2 == 1:
    print(f"the input number {a} is odd")
else:
    print("invalid input, please enter a valid integer")
