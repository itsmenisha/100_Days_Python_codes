# to play fizzbuzz 
b = 0
for number in range(1, 101):
    # because it usually skips the other statements so put hte brachched condition in if
    if number % 5 == 0 and number % 3 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)
