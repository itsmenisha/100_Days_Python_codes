scores = input("enter the list of student scores:").split(",")
a = scores
print("The list of score goes like :")
for n in range(len(a)):
    a[n] = int(a[n])
    print(a[n])
# maxnum = max(a)
# print(f"the maximum of all the input scores is : {maxnum}")
    b = 0
for score in scores:
    if score > b:
        b = score
print(f"the greatest score is :{b}")
