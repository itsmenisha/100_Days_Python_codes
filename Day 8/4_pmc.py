# prime number checker
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print("it is Prime")
    else:
        print(f" It is Not Prime")


a = int(input("enter a number :"))
prime_checker(number=a)
