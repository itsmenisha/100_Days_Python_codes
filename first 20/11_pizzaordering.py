print("Welcome to Nisha pizza shop!!")
a = input("what size of pizza do you want? L or M or S?? ")
b = input("Do you want perperoni? Y or N?? ")
c = input("Do you want extra cheese? Y or N?? ")
if a == "l":
    d = 25
    if b == "Y":
        d += 3
    if c == "Y":
        d += 1
    print(f"The total is ${d} for large pizza with {
          b} perperoni and {c} extra cheese")
elif a == "M":
    d = 20
    if b == "Y":
        d += 3
    if c == "Y":
        d += 1
    print(f"The total is ${d} for Medium pizza with {b} perperoni and {c} extra cheese")

elif a == "S":
    d = 15
    if b == "Y":
        d += 2
    if c == "Y":
        d += 1
    print(f"The total is ${d} for Small pizza with {b} perperoni and {c} extra cheese")
else:
    print("place the order correctly")
