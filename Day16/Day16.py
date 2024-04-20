from menu import Menu, MenuItem
from coffee_machine import CoffeeMaker
from moneymachine import MoneyMachine

menu_choice = Menu()
Coffee_Maker = CoffeeMaker()
money_machine = MoneyMachine()


is_true = True
while is_true:
    items = menu_choice.get_items()
    order = (f"hi!What would you like to have {items} :")
    if order == "done":
        is_true = False
    elif order == "report":
        Coffee_Maker.report()
        money_machine.report()
    else:
        drink = menu_choice.find_drink(order)
        if Coffee_Maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                Coffee_Maker.make_coffee(drink)
