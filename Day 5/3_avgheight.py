a = input("enter the list of heights:").split(",")
print("The heights you entered are:")
for n in range(len(a)):
    a[n] = int(a[n])
    print(a[n])
total_sum = sum(a)
length = len(a)
total_avg = total_sum / length
print(F"TOTAL AVERAGE IS :{total_avg}")
