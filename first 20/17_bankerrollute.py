# bankers roullette to see who will pay
import random
name = input("enter names of people participating, seperated by comma?? ")
names = int(name)
namess = random.randint(0, names-1)
print(name[namess])
name1 = (input("enter a name of person who will participate seperated by comma:"))
names = name1.split(",")
name = len(names)

namess = random.randint(0, name-1)
print(names[namess])
