
# set the initial variables and values for the machince resourses
water = 400
milk = 540
ground_coff = 120
cups_d = 9
money = 550


def print_stock(w, m, g, c, mn):
    # a function that prints the current items available
    print(f"The coffee machine has:\n{w} of water\n{m} of milk\n{g} of coffe beans\n{c} of disposable cups\n{mn}\
 of money")


def enough_water(coffee_type, water):
    # a func that checks if there is enough water based on the beverage type:
    if coffee_type == '1':
        if water >= 250:
            return True
        else:
            return False
    if coffee_type == '2':
        if water >= 350:
            return True
        else:
            return False
    if coffee_type == '3':
        if water >= 200:
            return True
        else:
            return False


def enough_milk(coffee_type, milk):
    # a function that checks if there is enough milk
    if coffee_type == '1':
        return True

    if coffee_type == '2':
        if milk >= 75:
            return True
        else:
            return False
    if coffee_type == '3':
        if milk >= 100:
            return True
        else:
            return False


def enough_coffee(coffee_type, gr_coffee):
    # a function that checks if we have enough coffee for the selected beverage
    if coffee_type == '1':
        if gr_coffee >= 16:
            return True
        else:
            return False
    if coffee_type == '2':
        if gr_coffee >= 20:
            return True
        else:
            return False
    if coffee_type == '3':
        if gr_coffee >= 12:
            return True
        else:
            return False


def enough_cups(cups):
    # short func that checks if we have a cup left
    if cups > 0:
        return True
    else:
        return False

while True:
    # take the wanted choice from the customer
    action = input("Write action (buy, fill, take, remaining, exit):\n")

# interface requirements loop
    while action != "buy" and action != 'fill' and action != 'take' and action != 'remaining' and action != 'exit':
        action = input("Write action (buy, fill, take):\n")

# create the actions menu
    if action == 'buy':
    # buy case
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        while choice != '1' and choice != '2' and choice != '3' and choice != 'back':
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
            if choice == 'back':
                break
        if choice == '1':
            if not enough_water(choice, water):
                print("Sorry, not enough water!")
            elif not enough_milk(choice, milk):
                print("Sorry, not enough milk!")
            elif not enough_coffee(choice, ground_coff):
                print("Sorry, not enough ground coffee!")
            elif not enough_cups(cups_d):
                print("Sorry, not enough cups!")
            elif enough_water(choice, water) and enough_milk(choice, milk) and enough_coffee(choice, ground_coff)\
                    and enough_cups(cups_d):
                water -= 250
                ground_coff -= 16
                money += 4
                cups_d -= 1

        elif choice == '2':
            if not enough_water(choice, water):
                print("Sorry, not enough water!")
            elif not enough_milk(choice, milk):
                print("Sorry, not enough milk!")
            elif not enough_coffee(choice, ground_coff):
                print("Sorry, not enough ground coffee!")
            elif not enough_cups(cups_d):
                print("Sorry, not enough cups!")
            elif enough_water(choice, water) and enough_milk(choice, milk) and enough_coffee(choice, ground_coff) \
                    and enough_cups(cups_d):
                water -= 350
                milk -= 75
                ground_coff -= 20
                money += 7
                cups_d -= 1
        elif choice == '3':
            if not enough_water(choice, water):
                print("Sorry, not enough water!")
            elif not enough_milk(choice, milk):
                print("Sorry, not enough milk!")
            elif not enough_coffee(choice, ground_coff):
                print("Sorry, not enough ground coffee!")
            elif not enough_cups(cups_d):
                print("Sorry, not enough cups!")
            elif enough_water(choice, water) and enough_milk(choice, milk) and enough_coffee(choice, ground_coff) \
                    and enough_cups(cups_d):
                water -= 200
                milk -= 100
                ground_coff -= 12
                money += 6
                cups_d -= 1
    elif action == 'fill':
    # takes care of the fill machine option and prints out the currents stock
        water += int(input("Write how many ml of water you want to add:\n"))
        milk += int(input("Write how many ml of milk you want to add\n:"))
        ground_coff += int(input("Write how many grams of coffee beans you want to add:\n"))
        cups_d += int(input("Write how many disposable coffee cups you want to add\n:"))
    elif action == 'take':
        # tells us how much money we took from the machine and removes the quantity from the stock
        print(f"I gave you {money}")
        money -= money
    elif action == 'remaining':
        # prints out the current stock of resources
        print_stock(water, milk, ground_coff, cups_d, money)
    elif action == 'exit':
        # exits the program
        exit()







