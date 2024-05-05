def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def divide(a, b):
    return a/b


def multiply(a, b):
    return a*b


def power(a, b):
    return a ^ b


def calculator(a, b, fun):
    return fun(a, b)


result = calculator(6, 3, sub)
print(result)
