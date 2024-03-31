from art import logo


def add(first, second):
    return first+second


def subtract(first, second):
    return first-second


def multiply(first, second):
    return first*second


def divide(first, second):
    return first/second


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    first = (input("enter a number: "))
    for symbols in operation:
        print(symbols)
    calculate = True
    while calculate:
        a = float(first)
        b = input("choose a operator:")
        c = float(input("enter next number: "))
        calc_operator = operation[b]

        e = calc_operator(a, c)
        print(f'''the output is
                        {a}{b}{c}={e}''')
        d = input(f'''
            Type 'ok' to continue calculating with {e}
            'new' to start a new calculation.
            (To end type 'end'):   ''').lower()
        if d == "ok":
            calculate = True
            a = e
            print(f"first number is {a}")
        if d == "new":
            calculate = True
            calculator()
        if d == "end":
            calculate = False


calculator()
