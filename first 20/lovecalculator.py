print(" Welcome to the love calculator")
a = input("enter your name? ")
b = input("enter your lovers name? ")
c = a+b
true = int(0)
love = int(0)
lowerc = c.lower()
t = lowerc.count("t")
r = lowerc.count("r")
u = lowerc.count("u")
e = lowerc.count("e")
true = t+r+u+e
l = lowerc.count("l")
o = lowerc.count("o")
v = lowerc.count("v")
e = lowerc.count("e")
love = l+o+v+e
print(f"The number of T is {t}")
print(f"The number of r is {r}")
print(f"The number of u is {u}")
print(f"The number of e is {e} ")
print(f"total= {true}")
print(f"The number of l is {l}")
print(f"The number of o is {o}")
print(f"The number of v is {v}")
print(f"The number of e is {e}")
print(f"total= {love}")
total = int(str(true)+str(love))
if total <= 10 or total >= 90:
    print(f"you are great together. your score is {total}")
elif total >= 40 and total <= 50:
    print(f"you are alright  together. your score is {total}")
else:
    print(f"your score is {total}")
