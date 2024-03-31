# to find the sum of even number between 1 and 101
b = 0
for number in range(1, 101):
    if number % 2 == 0:
        b += number

# or
# for number in range(2, 101,2):
#     b+=number

print(f"the multiplication of numbers from 1 to 100 is{b}")
