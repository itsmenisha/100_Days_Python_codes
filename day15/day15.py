menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
is_on = True


def is_resourse_sufficient(resourses_drink):
    for items in resourses_drink:
        if resourses_drink[items] >= resources[items]:
            print("The drink cannot be made resources are incomplete{items}.")
            return False
    return True


def process_coins():
    print("please enter your coins!!")
    penny = int(input("how many penny would you like to insert :"))*0.25
    dime = int(input("how many dime would you like to insert :"))*0.1
    nickel = int(input("how many nickel would you like to insert :"))*0.05
    quarter = int(input("how many quarter would you like to insert :"))*0.01
    total = penny+dime+nickel+quarter
    return total


def is_transaction_sucessful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        global profit
        change = round(money_recieved-drink_cost, 2)
        print(f"here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("sorry,insufficient fund")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here is your drink {drink_name}☕")


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while is_on:
    choice = input("What would you like? (latte, espresso, cappuccino): ")
    if choice == "off":
        is_true = False
    elif choice == "report":
        costw = resources["water"]
        costm = resources["milk"]
        costc = resources["coffee"]
        print(f"water ={costw}ml")
        print(f"milk ={costm}ml")
        print(f"coffee ={costc}ml")
        print(f"profit=${profit}")
    else:
        drink = menu[choice]
        print(drink)
        if is_resourse_sufficient(drink["ingredients"]):
            totals = process_coins()
            if is_transaction_sucessful(totals, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        else:
            is_true = False
