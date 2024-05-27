from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from turtle import Screen
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()
machine_on = True
def welcome():
    print("""
            /~~~~~~~~~~~~~~~~~~~/|
           /              /######/ / |
          /              /______/ /  |
         ========================= /||
         |_______________________|/ ||
          |  \****/     \__,,__/    ||       WELCOME TO THE COFFEE MACHINE
          |===\**/       __,,__     ||    
          |______________\====/%____||
          |   ___        /~~~~\ %  / |
         _|  |===|===   /      \%_/  |
        | |  |###|     |########| | /
        |____\###/______\######/__|/
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
     
    --------  MENU  --------
        Espresso ($1.50)
        Latte ($2.50)
        Cappuccino ($3.00)
    ------------------------
    To check available resources type 'report'
    To turn off the coffe machine type 'off'""")

while machine_on:
    welcome()
    option = menu.get_items()
    choice = str(input(f"What would you like? {option}"))
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        reporting = coffee_machine.report()
        reporting_2 = money_machine.report()
    else:
        drinks = menu.__init__()
        pick_drink = menu.find_drink(choice)
        resources = coffee_machine.is_resource_sufficient(pick_drink)
        if resources:
            transaction = money_machine.make_payment(pick_drink.cost)
            if transaction:
                go_cofffee = coffee_machine.make_coffee(pick_drink)
